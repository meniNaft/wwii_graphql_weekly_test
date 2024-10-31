import app.db.repositories.generic_repository as generic_repo
from app.db.models import Target

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
