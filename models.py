from sqlalchemy import Column, Integer, String, ForeignKey, Date, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    fullname = Column(String)

    group_id = Column(Integer, ForeignKey('groups.id'))
    group = relationship("Group", back_populates="students")


class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    students = relationship("Student", back_populates="group")


class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True)
    fullname = Column(String)

    subjects = relationship("Subject", back_populates="teacher")


class Subject(Base):
    __tablename__ = 'subjects'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    teacher_id = Column(Integer, ForeignKey('teachers.id'))
    teacher = relationship("Teacher", back_populates="subjects")


class Grade(Base):
    __tablename__ = 'grades'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    grade = Column(Integer)
    date_of = Column(Date)

    student = relationship("Student", back_populates="grades")
    subject = relationship("Subject", back_populates="grades")


Student.grades = relationship(
    "Grade", order_by=Grade.id, back_populates="student")
Subject.grades = relationship(
    "Grade", order_by=Grade.id, back_populates="subject")

engine = create_engine('sqlite:///hw06.sqlite')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
