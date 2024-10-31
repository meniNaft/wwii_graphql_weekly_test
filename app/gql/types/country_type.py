from graphene import ObjectType, Int, String, List
import app.db.repositories.city_repository as city_repo


class CountryType(ObjectType):
    country_id = Int()
    country_name = String()
    cities = List('app.gql.types.CityType')

    @staticmethod
    def resolve_cities(root, info):
        return city_repo.find_many_by_country_id(root.country_id)

