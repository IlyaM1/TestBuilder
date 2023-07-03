from window_manager import WindowManager
from Presenter.presenter import Presenter
from View.admin_panel_view import Entity, EntityType


class AdminPanelPresenter(Presenter):
    def __init__(self, view, model):
        super().__init__(view, model)
        self.view.signals.creating_clicked.connect(self.create_new_entity)
        self.view.signals.editing_clicked.connect(self.edit_entity)
        self.view.signals.deleting_clicked.connect(self.delete_entity)

    def create_new_entity(self, entity_type: EntityType):
        manager_instance = WindowManager.get_instance()
        presenter = manager_instance.open_test_editor() if entity_type == EntityType.TEST \
            else manager_instance.open_user_editor()
        presenter.finished.connect(lambda entity_dict: self.entity_creating_ended(entity_dict, entity_type)) # hope ``that will work...

    def edit_entity(self, entity: Entity):
        manager_instance = WindowManager.get_instance()
        entity_dict = self.model.get_entity_dict(entity)
        presenter = manager_instance.open_test_editor(entity_dict) if entity.type == EntityType.TEST \
            else manager_instance.open_user_editor(entity_dict)
        presenter.finished.connect(
            lambda new_entity_dict: self.entity_creating_ended(new_entity_dict, entity.type))  # hope that will work...

    def delete_entity(self, entity: Entity):
        self.model.delete_entity(entity)
        self.view.delete_entity_widget(entity)

    def entity_creating_ended(self, entity_dict: dict, entity_type: EntityType):
        id = self.model.create_new_entity(entity_dict, entity_type)
        entity = Entity(id, entity_dict["name"], entity_type)
        self.view.add_new_entity_widget(entity)

    def entity_editing_ended(self, entity_dict: dict, entity_type: EntityType):
        self.model.edit_entity(entity_dict, entity_type)
        entity = Entity(entity_dict["id"], entity_dict["name"], entity_type)
        self.view.edit_entity_widget(entity)
