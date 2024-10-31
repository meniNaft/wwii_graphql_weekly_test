from graphene import ObjectType, List, Field, Int
import app.db.repositories.city_repository as city_repo
import app.db.repositories.country_repository as country_repo
import app.db.repositories.mission_repository as mission_repo
import app.db.repositories.target_type_repositoy as target_type_repo
import app.db.repositories.target_repository as target_repo
from app.gql.types import CityType, CountryType, MissionType, TargetTypeType, TargetType


class Query(ObjectType):
    cities = List(CityType)
    countries = List(CountryType)
    missions = List(MissionType)
    target_types = List(TargetTypeType)
    targets = List(TargetType)

    @staticmethod
    def resolve_cities(root, info):
        return city_repo.find_all()

    @staticmethod
    def resolve_countries(root, info):
        return country_repo.find_all()

    @staticmethod
    def resolve_missions(root, info):
        return mission_repo.find_all()

    @staticmethod
    def resolve_target_types(root, info):
        return target_type_repo.find_all()

    @staticmethod
    def resolve_targets(root, info):
        return target_repo.find_all()
