from sqlalchemy import func, desc


def select_1(session):
    return session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
                  .join(Grade) \
                  .group_by(Student.id) \
                  .order_by(desc('avg_grade')) \
                  .limit(5) \
                  .all()


def select_2(session, subject_name):
    return session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
                  .join(Grade) \
                  .join(Subject) \
                  .filter(Subject.name == subject_name) \
                  .group_by(Student.id) \
                  .order_by(desc('avg_grade')) \
                  .first()


def select_3(session, subject_name):
    return session.query(Group.name, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
                  .join(Student) \
                  .join(Grade) \
                  .join(Subject) \
                  .filter(Subject.name == subject_name) \
                  .group_by(Group.id) \
                  .all()


def select_4(session):
    return session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
                  .scalar()


def select_5(session, teacher_name):
    return session.query(Subject.name) \
                  .join(Teacher) \
                  .filter(Teacher.fullname == teacher_name) \
                  .all()


def select_6(session, group_name):
    return session.query(Student.fullname) \
                  .join(Group) \
                  .filter(Group.name == group_name) \
                  .all()


def select_7(session, group_name, subject_name):
    return session.query(Student.fullname, Grade.grade) \
                  .join(Group) \
                  .join(Grade) \
                  .join(Subject) \
                  .filter(Group.name == group_name, Subject.name == subject_name) \
                  .all()


def select_8(session, teacher_name):
    return session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
                  .join(Subject) \
                  .join(Teacher) \
                  .filter(Teacher.fullname == teacher_name) \
                  .scalar()


def select_9(session, student_name):
    return session.query(Subject.name) \
                  .join(Grade) \
                  .join(Student) \
                  .filter(Student.fullname == student_name) \
                  .all()


def select_10(session, student_name, teacher_name):
    return session.query(Subject.name) \
                  .join(Teacher) \
                  .join(Grade) \
                  .join(Student) \
                  .filter(Student.fullname == student_name, Teacher.fullname == teacher_name) \
                  .all()
