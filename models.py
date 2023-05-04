from sqlalchemy import ForeignKey, Column, INTEGER, TEXT, DATETIME, BOOLEAN
from sqlalchemy.orm import relationship
from database import Base

class Ambassador(Base):
    __tablename__ = "ambassadors"

    id = Column("id", INTEGER, primary_key = True)
    email = Column("email", TEXT, nullable = False)
    password = Column("password", TEXT, nullable = False)
    school_id = Column("school_id", ForeignKey("schools.id"))
    school = relationship("School", back_populates="ambassadors")

    def __init__(self, email, password, school_id):
        self.email = email
        self.password = password
        self.school_id = school_id
        

class School(Base):
    __tablename__ = "schools"
    id = Column("id", INTEGER, primary_key = True)
    city = Column("city", INTEGER, nullable = False)
    ambassadors = relationship("Ambassador", back_populates = "school")

    def __init__(self, city):
        self.city = city

class Newsletter(Base):
    __tablename__ = "newsletters"
    id = Column("id", INTEGER, primary_key = True)
    is_ambassador = Column("is_ambassador", BOOLEAN, nullable = False)
    email = Column("email", TEXT, nullable = False)

    def __init__(self, is_ambassador, email):
        self.is_ambassador = is_ambassador
        self.email = email
