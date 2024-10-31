import app.db.repositories.generic_repository as generic_repo
from app.db.models import Mission

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
