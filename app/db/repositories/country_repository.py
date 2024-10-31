import app.db.repositories.generic_repository as generic_repo
from app.db.models import Country

current_type = Country


def find_all():
    return generic_repo.find_all(current_type)


def find_by_id(country_id: int):
    return generic_repo.find_by_id(current_type, country_id)


def insert(country: Country):
    return generic_repo.insert(country)


def insert_range(countries: list[Country]):
    return generic_repo.insert_range(countries)


def update(country_id: int, updated_country: Country):
    return generic_repo.update(current_type, country_id, updated_country)


def delete(country_id: int):
    return generic_repo.delete(current_type, country_id)
