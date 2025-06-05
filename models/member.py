from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from models import Base

class Member(Base):
    __tablename__ = 'members'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    join_date = Column(Date)

    workout_sessions = relationship("WorkoutSession", back_populates="member")

    def __repr__(self):
        return f"<Member(id={self.id}, name={self.first_name} {self.last_name}, email={self.email})>"
