from Model.entity import Entity, EntityType, User, Test


class AdminPanelModel:
    def __init__(self):
        pass

    def get_entity(self, entity: Entity):
        """
        Get row from database, it can be done with entity.id and entity.type
        :param entity: contains id and type
        :return: entity dict
        """
        pass

    def create_new_entity(self, entity: Entity, entity_type: EntityType):
        """
        Create new row in database
        :param entity: User/Test object
        :param entity_type: user/test
        :return: new id for this entity
        """
        pass

    def edit_entity(self, entity: Entity, entity_type: EntityType):
        """
        Edit existing entity in database
        :param entity: User/Test object
        :param entity_type: user/test
        :return: None
        """
        pass

    def delete_entity(self, entity: Entity):
        """
        Delete existing row in database, it can be done with entity.id and entity.type
        :param entity: contains id, type
        :return: None
        """
        pass
