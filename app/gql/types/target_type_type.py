from graphene import ObjectType, Int, String, List
import app.db.repositories.target_repository as target_repo


class TargetTypeType(ObjectType):
    target_type_id = Int()
    target_type_name = String()
    targets = List('app.gql.types.TargetType')

    @staticmethod
    def resolve_targets(root, info):
        return target_repo.find_many_by_target_type_id(root.target_type_id)

