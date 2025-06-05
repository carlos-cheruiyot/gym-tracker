from sqlalchemy.orm import declarative_base

Base = declarative_base()

from .member import Member
from .workout_session import WorkoutSession
