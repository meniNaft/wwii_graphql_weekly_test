from graphene import Mutation, String, Int, Field, Date
import app.db.repositories.target_repository as target_repo
import app.db.repositories.city_repository as city_repo
import app.db.repositories.target_type_repositoy as target_type_repo
import app.db.repositories.mission_repository as mission_repo
from app.db.models import Target
from app.gql.types import TargetType


class CreateTarget(Mutation):
    class Arguments:
        target_industry = String()
        target_priority = Int()
        city_id = Int()
        mission_id = Int()
        target_type_id = Int()

    target = Field(TargetType)
    error_message = String()

    @staticmethod
    def mutate(root, info, target_industry, target_priority, city_id, mission_id, target_type_id):
        found_city = city_repo.find_by_id(city_id).value_or(None)
        found_mission = mission_repo.find_by_id(mission_id).value_or(None)
        found_target_type = target_type_repo.find_by_id(target_type_id).value_or(None)
        if found_city and found_mission and found_target_type:
            new_target = Target(
                target_id=target_repo.get_max_target_id() + 1,
                target_industry=target_industry,
                target_priority=target_priority,
                city_id=city_id,
                mission_id=mission_id,
                target_type_id=target_type_id)

            target_repo.insert(new_target)
            return CreateTarget(target=new_target)

        elif not found_city:
            return CreateTarget(error_message=f"city_id '{city_id}' not found")

        elif not found_mission:
            return CreateTarget(error_message=f"mission_id '{mission_id}' not found")

        else:
            return CreateTarget(error_message=f"target_type_id '{target_type_id}' not found")
