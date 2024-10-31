from graphene import ObjectType
from graphene import Int, String, Float, Field, List
import app.db.repositories.target_repository as target_repo
import app.db.repositories.country_repository as country_repo


class CityType(ObjectType):
    city_id = Int()
    city_name = String()
    latitude = Float()
    longitude = Float()
    country_id = Int()
    country = Field('app.gql.types.CountryType')
    targets = List('app.gql.types.TargetType')

    @staticmethod
    def resolve_country(root, info):
        return country_repo.find_by_id(root.country_id).value_or(None)

    @staticmethod
    def resolve_targets(root, info):
        return target_repo.find_many_by_city_id(root.city_id)
