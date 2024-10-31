import app.db.repositories.generic_repository as generic_repo
from app.db.database import session_maker
from app.db.models import Target
from returns.maybe import Maybe

current_type = Target


def find_all():
    return generic_repo.find_all(current_type)


def find_by_id(target_id: int):
    return generic_repo.find_by_id(current_type, target_id)


def insert(target: Target):
    return generic_repo.insert(target)


def insert_range(targets: list[Target]):
    return generic_repo.insert_range(targets)


def update(target_id: int, updated_target: Target):
    return generic_repo.update(current_type, target_id, updated_target)


def delete(target_id: int):
    return generic_repo.delete(current_type, target_id)


def find_many_by_city_id(city_id):
    with session_maker() as session:
        return session.query(Target).filter(Target.city_id == city_id).limit(100).all()


def find_many_by_target_type_id(target_type_id):
    with session_maker() as session:
        return session.query(Target).filter(Target.target_type_id == target_type_id).limit(100).all()


def find_one_by_mission_id(mission_id):
    with session_maker() as session:
        return Maybe.from_optional(session.query(Target).filter(Target.mission_id == mission_id).first())
