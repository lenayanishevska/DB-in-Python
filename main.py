from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from config import DATABASE_URI
from models.models import Base, Subject, Student, StudentSubject


def main():
    engine = create_engine(DATABASE_URI)
    Base.metadata.create_all(bind=engine)

    with Session(engine) as session:
        english_subject = Subject(name='English')
        music_subject = Subject(name='Music')
        session.add_all([english_subject, music_subject])

        student1 = Student(name='Maria')
        student2 = Student(name='Bob')
        student3 = Student(name='Yana')
        session.add_all([student1, student2, student3])

        session.add(StudentSubject(student=student1, subject=english_subject))
        session.add(StudentSubject(student=student2, subject=music_subject))
        session.add(StudentSubject(student=student3, subject=english_subject))
        session.commit()

    with Session(engine) as session:
        stmt = (
            select(Student.name)
            .join(StudentSubject)
            .join(Subject)
            .filter(Subject.name == 'English')
        )

        result = session.execute(stmt).fetchall()

        print("Students who visited 'English' classes:")
        for row in result:
            print(row[0])


if __name__ == '__main__':
    main()
