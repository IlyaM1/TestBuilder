from Presenter.presenter import Presenter
from Model.entity import Entity, EntityType


class AdminPanelPresenter(Presenter):
    def __init__(self, view, model) -> None:
        super().__init__(view, model)
        self.view.signals.creating_clicked.connect(self.create_new_entity)
        self.view.signals.editing_clicked.connect(self.edit_entity)
        self.view.signals.deleting_clicked.connect(self.delete_entity)

    def create_new_entity(self, entity_type: EntityType) -> None:
        from window_manager import WindowManager
        manager_instance = WindowManager.get_instance()
        presenter = manager_instance.open_test_editor() if entity_type == EntityType.TEST \
            else manager_instance.open_user_editor()
        presenter.finished.connect(lambda entity_dict: self.entity_creating_ended(entity_dict, entity_type)) # hope ``that will work...

    def edit_entity(self, entity: Entity) -> None:
        from window_manager import WindowManager
        manager_instance = WindowManager.get_instance()
        full_entity_object = self.model.get_entity(entity)
        presenter = manager_instance.open_test_editor(full_entity_object) if entity.type == EntityType.TEST \
            else manager_instance.open_user_editor(full_entity_object)
        presenter.finished.connect(
            lambda new_entity_object: self.entity_creating_ended(new_entity_object))  # hope that will work...

    def delete_entity(self, entity: Entity) -> None:
        self.model.delete_entity(entity)
        self.view.delete_entity_widget(entity)

    def entity_creating_ended(self, entity: Entity) -> None:
        id = self.model.create_new_entity(entity)
        entity = Entity(id, entity.name, entity.type)
        self.view.add_new_entity_widget(entity)

    def entity_editing_ended(self, entity: Entity) -> None:
        self.model.edit_entity(entity)
        entity = Entity(entity.id, entity.name, entity.type)
        self.view.edit_entity_widget(entity)
