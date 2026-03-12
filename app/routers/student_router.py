from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas import StudentDetail, StudentSummary, DeleteResponse, StudentCreate
from app.database import DataBase
from app.settings import Settings
from app.services import StudentService


app_settings = Settings() # type: ignore

db = DataBase(app_settings.DATABASE_URL)

db_session = db.get_session_db

router = APIRouter(
    prefix='/students',
    tags=['students']
)

@router.get('/', response_model=List[StudentSummary])
def list_students(db: Session = Depends(db_session)):
    return StudentService.list_students(db)


@router.get('/{student_id}', response_model=StudentDetail)
def get_student(
    student_id: int,
    db: Session = Depends(db_session)
):
    student = StudentService.get_student(student_id, db)
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='student not found')
    return student


@router.post('/', response_model=StudentDetail)
def create_student(
    student_data: StudentCreate,
    db: Session = Depends(db_session)
):
    return StudentService.create_student(student_data, db)


# @app.patch(
#     '/students/{student_id}',
#     response_model=schemas.StudentDetail,
#     status_code=status.HTTP_200_OK,
# )
# def update_student(
#     student_id: int,
#     student_update: schemas.StudentUpdate,
#     db: Session = Depends(db.get_session_db)
# ):
#     student = db.get(models.Student, student_id)

#     if not student:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='student not found')
    
#     update_data = student_update.model_dump(exclude_unset=True)

#     if 'profile' in update_data:
#         profile_data = update_data.pop('profile')

#         if student.profile:
#             for attr, value in profile_data.items():
#                 setattr(student.profile, attr, value)
#         else:
#             student.profile = models.Profile(**profile_data)
    
#     for attr, value in update_data.items():
#         setattr(student, attr, value)
    
#     db.commit()
#     db.refresh(student)
#     return student


@router.delete('/{student_id}', response_model=DeleteResponse)
def delete_student(
    student_id: int,
    db: Session = Depends(db_session)
):
    deleted = StudentService.delete_student(student_id, db)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='student not found')
    return {
        'success': True,
        'message': 'student deleted'
    }
