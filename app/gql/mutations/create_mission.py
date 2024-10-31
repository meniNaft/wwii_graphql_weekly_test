from graphene import Mutation, String, Int, Field, Date
import app.db.repositories.mission_repository as mission_repo
from app.db.models import Mission
from app.gql.types import MissionType


class CreateMission(Mutation):
    class Arguments:
        mission_date = Date()
        airborne_aircraft = Int()
        attacking_aircraft = Int()
        bombing_aircraft = Int()
        aircraft_returned = Int()
        aircraft_failed = Int()
        aircraft_damaged = Int()
        aircraft_lost = Int()

    mission = Field(MissionType)

    @staticmethod
    def mutate(root, info, mission_date, airborne_aircraft, attacking_aircraft, bombing_aircraft,
               aircraft_returned, aircraft_failed, aircraft_damaged, aircraft_lost):
        new_mission = Mission(
            mission_id=mission_repo.get_max_mission_id() + 1,
            mission_date=mission_date,
            airborne_aircraft=airborne_aircraft,
            attacking_aircraft=attacking_aircraft,
            bombing_aircraft=bombing_aircraft,
            aircraft_returned=aircraft_returned,
            aircraft_failed=aircraft_failed,
            aircraft_damaged=aircraft_damaged,
            aircraft_lost=aircraft_lost)

        mission_repo.insert(new_mission)
        return CreateMission(mission=new_mission)
