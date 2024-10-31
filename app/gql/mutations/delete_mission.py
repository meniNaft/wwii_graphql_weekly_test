from graphene import Mutation, String, Int, Field, Date
import app.db.repositories.mission_repository as mission_repo
from returns.result import Success


class DeleteMission(Mutation):
    class Arguments:
        mission_id = Int()

    message = String()

    @staticmethod
    def mutate(root, info, mission_id):
        res = mission_repo.delete(mission_id)
        if isinstance(res, Success):
            return DeleteMission(message=f"the mission {mission_id} deleted successfully")
        else:
            return DeleteMission(message=res.failure())
