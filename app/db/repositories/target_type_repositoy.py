import app.db.repositories.generic_repository as generic_repo
from app.db.models import TargetType

current_type = TargetType


def find_all():
    return generic_repo.find_all(current_type)


def find_by_id(target_type_id: int):
    return generic_repo.find_by_id(current_type, target_type_id)


def insert(target: TargetType):
    return generic_repo.insert(target)


def insert_range(target_types: list[TargetType]):
    return generic_repo.insert_range(target_types)


def update(target_type_id: int, updated_target_type: TargetType):
    return generic_repo.update(current_type, target_type_id, updated_target_type)


def delete(target_type_id: int):
    return generic_repo.delete(current_type, target_type_id)
