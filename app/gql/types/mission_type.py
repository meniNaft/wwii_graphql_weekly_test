from graphene import ObjectType, Int, Date, Field
import app.db.repositories.target_repository as target_repo


class MissionType(ObjectType):
    mission_id = Int()
    mission_date = Date()
    airborne_aircraft = Int()
    attacking_aircraft = Int()
    bombing_aircraft = Int()
    aircraft_returned = Int()
    aircraft_failed = Int()
    aircraft_damaged = Int()
    aircraft_lost = Int()
    target = Field('app.gql.types.TargetType')

    @staticmethod
    def resolve_target(root, info):
        return target_repo.find_one_by_mission_id(root.mission_id).value_or(None)

