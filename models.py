from sqlalchemy import Integer,String,Column,Float
from database import Base

class Student(Base):
    __tablename__ = "Students"
    id=Column(Integer,primary_key=True)
    name=Column(String(256))
    surname=Column(String(256))
    age=Column(Integer)
    score=Column(Float)

class Teacher(Base):
    __tablename__ = "Teachers"
    id=Column(Integer,primary_key=True)
    name=Column(String(256))
    surname=Column(String(256))
    subject=Column(String(256))
    age=Column(Integer)
    experience=Column(Float)