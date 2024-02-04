from database import Base,SessionLocal,engine
from fastapi import FastAPI,Depends,HTTPException,status
import schemas,models
from typing import List
from sqlalchemy.orm import Session

Base.metadata.create_all(engine)

def get_session():
    session=SessionLocal()
    try:
        yield session
    finally:
        session.close()

app=FastAPI(docs_url="/docs")

@app.get("/")
def index():
    return "Hello World!"

@app.get("/getStudentById/{id}",response_model=schemas.Student)
def getStudentById(id:int,session:Session=Depends(get_session)):
    student=session.query(models.Student).get(id)
    if not student:
        raise HTTPException(status_code=404,detail=f"Student {id} not found!")
    return student

@app.get("/getStudent",response_model=List[schemas.Student])
def getStudentById(session:Session=Depends(get_session)):
    student=session.query(models.Student).all()
    if not student:
        raise HTTPException(status_code=404,detail=f"Students not found!")
    return student

@app.post("/addStudent",response_model=schemas.Student)
def addStudent(newUser:schemas.StudentCreate,session:Session=Depends(get_session)): 
    student=models.Student(name=newUser.name,surname=newUser.surname,age=newUser.age,score=newUser.score)
    session.add(student)
    session.commit()
    session.refresh(student)

    return student

@app.put("/updateStudentById/{id}",response_model=schemas.Student)
def updateStudentbyId(id:int,newUser:schemas.StudentCreate,session:Session=Depends(get_session)):
    student=session.query(models.Student).get(id)
    if not student:
        raise HTTPException(status_code=404,detail=f"Student {id} not found")
    student.name=newUser.name
    student.surname=newUser.surname
    student.age=newUser.age
    student.score=newUser.score

@app.delete("/deleteStudentbyId/{id}")
def deleteStudentById(id:int,session:Session=Depends(get_session)):
    student=session.query(models.Student).get(id)

    if not student:
        raise HTTPException(status_code=404,detail=f"Student {id} not found!")

    session.delete(student)
    session.commit()
    session.refresh(student)
    return f"Student {id} successfully deleted"




@app.get("/getTeacherById/{id}",response_model=schemas.Teacher)
def getTeacherById(id:int,session:Session=Depends(get_session)):
    teacher=session.query(models.Teacher).get(id)
    if not teacher:
        raise HTTPException(status_code=404,detail=f"Teacher {id} not found!")
    return teacher

@app.get("/getTeacher",response_model=List[schemas.Teacher])
def getTeacherById(session:Session=Depends(get_session)):
    teacher=session.query(models.Teacher).all()
    if not teacher:
        raise HTTPException(status_code=404,detail=f"Teachers not found!")
    return teacher

@app.post("/addTeacher",response_model=schemas.Teacher)
def addTeacher(newTeacher:schemas.TeacherCreate,session:Session=Depends(get_session)): 
    teacher=models.Teacher(name=newTeacher.name,surname=newTeacher.surname,subject=newTeacher.subject,age=newTeacher.age,experience=newTeacher.experience)
    session.add(teacher)
    session.commit()
    session.refresh(teacher)

    return teacher

@app.put("/updateTeacherById/{id}", response_model=schemas.Teacher)
def updateTeacherById(id: int, newTeacher: schemas.TeacherCreate, session: Session = Depends(get_session)):
    teacher = session.query(models.Teacher).get(id)
    if not teacher:
        raise HTTPException(status_code=404, detail=f"Teacher {id} not found")
    teacher.name = newTeacher.name
    teacher.surname = newTeacher.surname
    teacher.subject = newTeacher.subject
    teacher.age = newTeacher.age
    teacher.experience = newTeacher.experience
    session.commit()
    return teacher

@app.delete("/deleteTeacherbyId/{id}")
def deleteTeacherById(id:int,session:Session=Depends(get_session)):
    teacher=session.query(models.Teacher).get(id)

    if not teacher:
        raise HTTPException(status_code=404,detail=f"Teacher {id} not found!")

    session.delete(teacher)
    session.commit()
    session.refresh(teacher)
    return f"teacher {id} successfully deleted"