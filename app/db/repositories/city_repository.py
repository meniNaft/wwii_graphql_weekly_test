import app.db.repositories.generic_repository as generic_repo
from app.db.models import City

current_type = City


def find_all():
    return generic_repo.find_all(current_type)


def find_by_id(city_id: int):
    return generic_repo.find_by_id(current_type, city_id)


def insert(city: City):
    return generic_repo.insert(city)


def insert_range(cities: list[City]):
    return generic_repo.insert_range(cities)


def update(city_id: int, updated_city: City):
    return generic_repo.update(current_type, city_id, updated_city)


def delete(city_id: int):
    return generic_repo.delete(current_type, city_id)
