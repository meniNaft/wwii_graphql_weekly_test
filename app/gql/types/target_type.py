from graphene import ObjectType, Int, String, Field
import app.db.repositories.city_repository as city_repo
import app.db.repositories.mission_repository as mission_repo
import app.db.repositories.target_type_repositoy as target_type_repo


class TargetType(ObjectType):
    target_id = Int()
    target_industry = String()
    target_priority = Int()
    city_id = Int()
    city = Field('app.gql.types.CityType')
    mission_id = Int()
    mission = Field('app.gql.types.MissionType')
    target_type_id = Int()
    target_type = Field('app.gql.types.TargetTypeType')

    @staticmethod
    def resolve_city(root, info):
        return city_repo.find_by_id(root.city_id).value_or(None)

    @staticmethod
    def resolve_mission(root, info):
        return mission_repo.find_by_id(root.mission_id).value_or(None)

    @staticmethod
    def resolve_target_type(root, info):
        return target_type_repo.find_by_id(root.target_type_id).value_or(None)
