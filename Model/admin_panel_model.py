from Model.entity import Entity, EntityType, User, Test


class AdminPanelModel:
    def __init__(self) -> None:
        pass

    def get_entity(self, entity: Entity) -> Entity:
        # TODO: Get row from database, it can be done with entity.id and entity.type and transform to Entity
        pass

    def create_new_entity(self, entity: Entity, entity_type: EntityType) -> int:
        """
        TODO: Create new row in database
        :return: new id for this entity
        """
        pass

    def edit_entity(self, entity: Entity, entity_type: EntityType) -> None:
        # TODO: Edit existing entity in database
        pass

    def delete_entity(self, entity: Entity) -> None:
        # TODO: Delete existing row in database, it can be done with entity.id and entity.type
        pass
