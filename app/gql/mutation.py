from graphene import ObjectType
from app.gql.mutations import CreateMission, CreateTarget, DeleteMission


class Mutation(ObjectType):
    create_mission = CreateMission.Field()
    create_target = CreateTarget.Field()
    delete_mission = DeleteMission.Field()

