from sqlalchemy import ForeignKey, Column, INTEGER, TEXT, DATETIME
from sqlalchemy.orm import relationship
from database import Base

class Ambassador(Base):
    __tablename__ = "ambassadors"

    id = Column("id", INTEGER, primary_key = True)
    email = Column("email", TEXT, nullable = False)
    school_id = Column("school_id", ForeignKey("School.id"))
    school = relationship("School", back_populates="Ambassador")

    def __init__(self, email, school_id):
        self.email = email
        self.school_id = school_id
        

class School(Base):
    id = Column("id", INTEGER, primary_key = True)
    city = Column("city", INTEGER, nullable = False)
    ambassadors = relationship("Ambassador", back_populates = "School")

    def __init__(self, city):
        self.city = city

class Newsletter(Base):
    
    id = Column("id", INTEGER, primary_key = True)
    is_ambassador = Column("is_ambassador", bool, nullable = False)
    email = Column("email", TEXT, nullable = False)

    def __init__(self, is_ambassador, email):
        self.is_ambassador = is_ambassador
        self.email = email
