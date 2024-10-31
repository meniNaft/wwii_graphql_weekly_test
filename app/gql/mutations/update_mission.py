from email.policy import default

from graphene import Mutation, String, Int, Field, Date
import app.db.repositories.mission_repository as mission_repo
from returns.result import Success
from app.gql.types import MissionType


class UpdateMission(Mutation):
    class Arguments:
        mission_id = Int()
        mission_date = Date(default_value=None)
        airborne_aircraft = Int(default_value=None)
        attacking_aircraft = Int(default_value=None)
        bombing_aircraft = Int(default_value=None)
        aircraft_returned = Int(default_value=None)
        aircraft_failed = Int(default_value=None)
        aircraft_damaged = Int(default_value=None)
        aircraft_lost = Int(default_value=None)

    mission = Field(MissionType)
    error_message = String()

    @staticmethod
    def mutate(root, info, mission_id, mission_date=None, airborne_aircraft=None, attacking_aircraft=None, bombing_aircraft=None,
               aircraft_returned=None, aircraft_failed=None, aircraft_damaged=None, aircraft_lost=None):
        found_mission = mission_repo.find_by_id(mission_id).value_or(None)
        if found_mission:
            found_mission.mission_date = mission_date if mission_date else found_mission.mission_date
            found_mission.airborne_aircraft = airborne_aircraft if airborne_aircraft else found_mission.airborne_aircraft
            found_mission.attacking_aircraft = attacking_aircraft if attacking_aircraft else found_mission.attacking_aircraft
            found_mission.bombing_aircraft = bombing_aircraft if bombing_aircraft else found_mission.bombing_aircraft
            found_mission.aircraft_returned = aircraft_returned if aircraft_returned else found_mission.aircraft_returned
            found_mission.aircraft_failed = aircraft_failed if aircraft_failed else found_mission.aircraft_failed
            found_mission.aircraft_damaged = aircraft_damaged if aircraft_damaged else found_mission.aircraft_damaged
            found_mission.aircraft_lost = aircraft_lost if aircraft_lost else found_mission.aircraft_lost

            res = mission_repo.update(mission_id, found_mission)

            if isinstance(res, Success):
                return UpdateMission(mission=found_mission)
            else:
                return UpdateMission(error_message=res.failure())

        else:
            return UpdateMission(error_message=f"mission_id '{mission_id}' not found")
