from sqlalchemy import ForeignKey, Column, INTEGER, TEXT, DATETIME, BOOLEAN
from sqlalchemy.orm import relationship
from database import Base

class Ambassador(Base):
    __tablename__ = "ambassadors"

    id = Column("id", INTEGER, primary_key = True)
    email = Column("email", TEXT, nullable = False)
    password = Column("password", TEXT, nullable = False)
    application = relationship("Application", back_populates="ambassadors")

    def __init__(self, email, password, school_id):
        self.email = email
        self.password = password
        self.school_id = school_id
        
class Application(Base):
    __tablename__ = "applications"

    id = Column("id", INTEGER, primary_key = True)
    first_name = Column("fname", TEXT, nullable = False)
    last_name = Column("lname", TEXT, nullable = False)
    gender = Column("gender", TEXT, nullable = False)
    email = Column("email", TEXT, nullable = False)
    school = Column("school", TEXT, nullable = False)
    social_programs = Column("programs", TEXT, nullable = False)
    SA_1 = Column("SA_1", TEXT, nullable = False)
    SA_2 = Column("SA_2", TEXT, nullable = False)
    SA_3 = Column("SA_3", TEXT, nullable = False)
    ambassador_id = Column("ambassador_id", INTEGER, ForeignKey(Ambassador.id))
    ambassadors = relationship("Ambassador", back_populates = "application")
    
    def __init__(self, fname, lname, gender, email, school, programs, SA1, SA2, SA3):
        self.first_name = fname
        self.last_name = lname
        self.gender = gender
        self.email = email
        self.school = school
        self.social_programs = programs
        self.SA_1 = SA1
        self.SA_2 = SA2
        self.SA_3 = SA3

class School(Base):
    __tablename__ = "schools"
    id = Column("id", INTEGER, primary_key = True)
    city = Column("city", INTEGER, nullable = False)
    def __init__(self, city):
        self.city = city

class Newsletter(Base):
    __tablename__ = "newsletters"
    id = Column("id", INTEGER, primary_key = True)
    email = Column("email", TEXT, nullable = False)

    def __init__(self, email):
        self.email = email
