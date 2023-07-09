from datetime import datetime, timedelta
from random import randint
from faker import Faker
from my_select import *

fake = Faker('uk-UA')

subjects = [
    "Coding",
    "Math",
    "Geometry",
    "Physics",
    "Philosophy",
    "Chemistry",
    "Sociology",
    "Singing",
    "Aikido"
]

groups = ["XX-23", "YY-11", "ZZ-44"]

NUMBERS_TEACHERS = 5
NUMBERS_STUDENTS = 25

session = Session()


def seed_teacher():
    teachers = [fake.name() for _ in range(NUMBERS_TEACHERS)]
    session.bulk_insert_mappings(
        Teacher, [{'fullname': teacher} for teacher in teachers])
    session.commit()


def seed_groups():
    session.bulk_insert_mappings(Group, [{'name': group} for group in groups])
    session.commit()


def seed_students():
    students = [fake.name() for _ in range(NUMBERS_STUDENTS)]
    list_group_id = [randint(1, len(groups)) for _ in range(NUMBERS_STUDENTS)]
    session.bulk_insert_mappings(Student, [{'fullname': student, 'group_id': group_id}
                                 for student, group_id in zip(students, list_group_id)])
    session.commit()


def seed_subjects():
    list_teacher_id = [randint(1, NUMBERS_TEACHERS)
                       for _ in range(len(subjects))]
    session.bulk_insert_mappings(Subject, [{'name': subject, 'teacher_id': teacher_id}
                                 for subject, teacher_id in zip(subjects, list_teacher_id)])
    session.commit()


def seed_grades():
    start_date = datetime.strptime("2022-09-01", "%Y-%m-%d")
    finish_date = datetime.strptime("2023-05-31", "%Y-%m-%d")

    def get_list_date(start_date, finish_date):
        result = []
        current_day = start_date
        while current_day < finish_date:
            if current_day.isoweekday() < 6:
                result.append(current_day)
            current_day += timedelta(1)
        return result

    list_date = get_list_date(start_date, finish_date)

    grades = []
    for day in list_date:
        random_subject = randint(1, len(subjects))
        random_students = [randint(1, NUMBERS_STUDENTS) for _ in range(7)]
        for student in random_students:
            grades.append({'student_id': student, 'subject_id': random_subject,
                          'grade': randint(1, 12), 'date_of': day.date()})

    session.bulk_insert_mappings(Grade, grades)
    session.commit()


seed_teacher()
seed_groups()
seed_students()
seed_subjects()
seed_grades()

session.close()
