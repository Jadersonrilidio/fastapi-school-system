from app.schemas.common import *
from app.schemas.profile_schema import *
from app.schemas.teacher_schema import *
from app.schemas.student_schema import *
from app.schemas.subject_schema import *
from app.schemas.enrollment_schema import *


StudentDetail.model_rebuild()
SubjectDetail.model_rebuild()
TeacherDetail.model_rebuild()
EnrollmentDetail.model_rebuild()
