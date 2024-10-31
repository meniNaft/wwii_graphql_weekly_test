from email.policy import default

from graphene import Mutation, String, Int, Field, Date
import app.db.repositories.mission_repository as mission_repo
from returns.result import Success

from app.db.models import Mission
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
    def mutate(root, info, mission_id, **kwargs):
        new_mission = Mission(mission_id=mission_id)

        for field, value in kwargs.items():
            if value is not None:
                setattr(new_mission, field, value)

        res = mission_repo.update(mission_id, new_mission)
        if isinstance(res, Success):
            return UpdateMission(mission=new_mission)
        return UpdateMission(error_message=res.failure())
