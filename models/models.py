from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

    def __str__(self):
        return f"Student {self.id}: {self.name}"


class Subject(Base):
    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)


class StudentSubject(Base):
    __tablename__ = 'student_subjects'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    student = relationship('Student', back_populates='subjects')
    subject = relationship('Subject', back_populates='students')


Student.subjects = relationship('StudentSubject', back_populates='student')
Subject.students = relationship('StudentSubject', back_populates='subject')