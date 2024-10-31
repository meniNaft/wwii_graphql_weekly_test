import app.db.repositories.generic_repository as generic_repo
from app.db.database import session_maker
from app.db.models import Mission, Target, City
from datetime import date
from sqlalchemy.sql.expression import func

current_type = Mission


def find_all():
    return generic_repo.find_all(current_type)


def find_by_id(mission_id: int):
    return generic_repo.find_by_id(current_type, mission_id)


def insert(mission: Mission):
    return generic_repo.insert(mission)


def insert_range(missions: list[Mission]):
    return generic_repo.insert_range(missions)


def update(mission_id: int, updated_mission: Mission):
    return generic_repo.update(current_type, mission_id, updated_mission)


def delete(mission_id: int):
    return generic_repo.delete(current_type, mission_id)


def find_between_dates(start_date: date, end_date: date):
    with session_maker() as session:
        return session.query(current_type).filter(current_type.mission_date.between(start_date, end_date)).all()


def find_missions_by_country(country_id: int):
    with session_maker() as session:
        return (
            session.query(current_type)
            .join(current_type.target)
            .join(Target.city)
            .filter(City.country_id == country_id)
        )


def find_by_target_industry(target_industry):
    with session_maker() as session:
        return (
            session.query(current_type)
            .join(current_type.target)
            .filter(Target.target_industry == target_industry)
        )


def find_missions_by_target_type_id(target_type_id: int):
    with session_maker() as session:
        return (
            session.query(current_type)
            .join(current_type.target)
            .filter(Target.target_type_id == target_type_id)
        )


def get_max_mission_id():
    with session_maker() as session:
        return session.query(func.max(current_type.mission_id)).scalar()