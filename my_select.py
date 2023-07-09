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


def select_
