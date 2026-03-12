from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session, selectinload
from typing import List
from app import models, schemas
from app.database import DataBase
from app.settings import Settings
# from contextlib import asynccontextmanager


app_settings = Settings() # type: ignore

db = DataBase(app_settings.DATABASE_URL)

# https://fastapi.tiangolo.com/advanced/events/#lifespan
# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     db.drop_tables()
#     db.create_tables()
#     yield

app = FastAPI(
    title="School System",
    description="School API",
    version="1.0.0",
    # lifespan=lifespan
)


@app.get(
    '/students/',
    response_model=List[schemas.StudentSummary],
    status_code=status.HTTP_200_OK,
)
def list_students(db: Session = Depends(db.get_session_db)):
    return db.query(models.Student).all()


@app.post(
    '/students/',
    response_model=schemas.StudentDetail,
    status_code=status.HTTP_201_CREATED,
)
def create_student(
    student: schemas.StudentCreate,
    db: Session = Depends(db.get_session_db)
):
    db_student = models.Student(name=student.name)
    if student.profile:
        db_student.profile = models.Profile(**student.profile.model_dump())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


@app.get(
    '/students/{student_id}',
    response_model=schemas.StudentDetail,
    status_code=status.HTTP_200_OK,
)
def get_student(
    student_id: int,
    db: Session = Depends(db.get_session_db)
):
    student = ( 
        db.query(models.Student)
        .options(
            selectinload(models.Student.profile),
            selectinload(models.Student.subjects),
        )
        .filter(models.Student.id == student_id)
        .first()
    )

    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='student not found')

    return student


@app.patch(
    '/students/{student_id}',
    response_model=schemas.StudentDetail,
    status_code=status.HTTP_200_OK,
)
def update_student(
    student_id: int,
    student_update: schemas.StudentUpdate,
    db: Session = Depends(db.get_session_db)
):
    student = db.get(models.Student, student_id)

    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='student not found')
    
    update_data = student_update.model_dump(exclude_unset=True)

    if 'profile' in update_data:
        profile_data = update_data.pop('profile')

        if student.profile:
            for attr, value in profile_data.items():
                setattr(student.profile, attr, value)
        else:
            student.profile = models.Profile(**profile_data)
    
    for attr, value in update_data.items():
        setattr(student, attr, value)
    
    db.commit()
    db.refresh(student)
    return student


@app.delete(
    '/students/{student_id}',
    response_model=schemas.DeleteResponse,
    status_code=status.HTTP_200_OK,
)
def delete_student(
    student_id: int,
    db: Session = Depends(db.get_session_db)
):
    student = db.get(models.Student, student_id)

    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='student not found')
    
    db.delete(student)
    db.commit()

    return {
        'success': True,
        'message': 'student deleted successfully'
    }
