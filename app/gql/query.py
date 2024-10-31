from graphene import ObjectType, List, Field, Int, Date, String
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

    mission_by_id = Field(MissionType, mission_id=Int())
    missions_between_dates = List(MissionType, start_date=Date(), end_date=Date())
    missions_by_country_id = List(MissionType, country_id=Int())
    missions_by_target_industry = List(MissionType, target_industry=String())
    missions_by_target_type_id = List(MissionType, target_type_id=Int())

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

    @staticmethod
    def resolve_mission_by_id(root, info, mission_id):
        return mission_repo.find_by_id(mission_id).value_or(None)

    @staticmethod
    def resolve_missions_between_dates(root, info, start_date, end_date):
        return mission_repo.find_between_dates(start_date, end_date)

    @staticmethod
    def resolve_missions_by_country_id(root, info, country_id):
        return mission_repo.find_missions_by_country(country_id)

    @staticmethod
    def resolve_missions_by_target_industry(root, info, target_industry):
        return mission_repo.find_by_target_industry(target_industry)

    @staticmethod
    def resolve_missions_by_target_type_id(root, info, target_type_id):
        return mission_repo.find_missions_by_target_type_id(target_type_id)
