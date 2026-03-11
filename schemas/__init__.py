from .common import *
from .profile_schema import *
from .teacher_schema import *
from .student_schema import *
from .subject_schema import *
from .enrollment_schema import *


StudentDetail.model_rebuild()
SubjectDetail.model_rebuild()
TeacherDetail.model_rebuild()
EnrollmentDetail.model_rebuild()
