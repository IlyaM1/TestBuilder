from View.view import View
from enum import Enum
from config import Config
from PyQt5 import QtCore, QtWidgets


class EntityType(Enum):
    USER = 1
    TEST = 2


class Entity:
    def __init__(self, id: int, name: str, type: EntityType):
        self.id = id
        self.name = name
        self.type = type


class AdminPanelSignals(QtCore.QObject):
    creating_clicked = QtCore.pyqtSignal(EntityType)
    editing_clicked = QtCore.pyqtSignal(Entity)
    deleting_clicked = QtCore.pyqtSignal(Entity)


class AdminPanelView(View):
    def __init__(self, users: list, tests: list):
        super().__init__(AdminPanelSignals())
        self.set_interface_settings()

        self.tab_widget = QtWidgets.QTabWidget()
        self.user_tab_layout = self.create_tab_widget(users, EntityType.USER)
        self.test_tab_layout = self.create_tab_widget(tests, EntityType.TEST)

        container = QtWidgets.QVBoxLayout(self)
        container.addWidget(self.tab_widget)

    def set_interface_settings(self):
        self.setMinimumSize(1280, 720)
        with open(Config.get_path() + '/View/css/admin_panel_view.css') as css:
            self.setStyleSheet(css.read())

    def create_tab_widget(self, entity_list: list, entity_type: EntityType):
        """
        Automatically adds itself in tab_widget
        :param entity_list: list of entities (users or tests)
        :param entity_type: type of entities (EntityType.TEST or EntityType.USER)
        :return: layout that shows all entities from entity_list
        """
        entities_list_layout = QtWidgets.QVBoxLayout()

        for entity in entity_list:
            entity_object = Entity(entity["id"], entity["name"], entity_type)
            entity_widget = self.create_entity_widget(entity_object)
            entities_list_layout.addWidget(entity_widget)

        button_entity_name = "тест" if entity_type == EntityType.TEST else "сотрудника"
        new_entity_button = QtWidgets.QPushButton(f"Добавить {button_entity_name}")
        new_entity_button.released.connect(lambda: self.new_entity_button_released(entity_type))

        entities_list_widget = QtWidgets.QWidget()
        entities_list_widget.setLayout(entities_list_layout)
        scroll_widget = self.generate_scroll_widget(entities_list_widget)

        final_widget_layout = QtWidgets.QVBoxLayout()
        final_widget_layout.addWidget(scroll_widget)
        final_widget_layout.addWidget(new_entity_button)

        final_widget = QtWidgets.QWidget()
        final_widget.setLayout(final_widget_layout)

        tab_name = "Тесты" if entity_type == EntityType.TEST else "Сотрудники"
        self.tab_widget.addTab(final_widget, tab_name)
        return entities_list_layout

    @staticmethod
    def generate_scroll_widget(widget_to_set):
        scroll_widget = QtWidgets.QScrollArea()

        scroll_widget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        scroll_widget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        scroll_widget.setWidgetResizable(True)
        scroll_widget.setWidget(widget_to_set)

        return scroll_widget

    def create_entity_widget(self, entity):
        widget = EntityWidget(entity)
        widget.setFixedSize(self.width() - 60, 50)
        widget.clicked.connect(lambda: self.entity_widget_clicked(entity))
        widget.deleting.connect(lambda: self.entity_widget_deleting(entity))
        return widget

    def new_entity_button_released(self, entity_type):
        self.signals.creating_clicked.emit(entity_type)

    def entity_widget_clicked(self, entity):
        self.signals.editing_clicked.emit(entity)

    def entity_widget_deleting(self, entity):
        self.signals.deleting_clicked.emit(entity)

    def delete_entity_widget(self, entity):
        layout = self.test_tab_layout if entity.type == EntityType.TEST else self.user_tab_layout
        entity_widget = self.__find_widget_in_entity_layout(entity)
        layout.removeWidget(entity_widget)

    def add_new_entity_widget(self, entity: Entity):
        entity_widget = self.create_entity_widget(entity)
        if entity.type == EntityType.TEST:
            self.test_tab_layout.addWidget(entity_widget)
        elif entity.type == EntityType.USER:
            self.user_tab_layout.addWidget(entity_widget)
        else:
            raise Exception("There are no this entity type")

    def edit_entity_widget(self, entity):
        entity_widget = self.__find_widget_in_entity_layout(entity)
        entity_widget.setText(entity.name)

    def __find_widget_in_entity_layout(self, entity: Entity):
        layout = self.test_tab_layout if entity.type == EntityType.TEST else self.user_tab_layout
        for i in range(layout.count()):
            widget = layout.itemAt(i).widget()
            if widget.entity.id == entity.id:
                return widget
        raise Exception("Can't find widget that contains this entity")


class EntityWidget(QtWidgets.QLabel):
    clicked = QtCore.pyqtSignal()
    deleting = QtCore.pyqtSignal()

    def __init__(self, entity: Entity, parent=None):
        super().__init__(entity.name, parent)
        self.entity = entity
        self.menu = QtWidgets.QMenu(self)
        delete_action = QtWidgets.QAction("Удалить", self)
        self.menu.addAction(delete_action)

    def mouseReleaseEvent(self, e):
        if e.button() == QtCore.Qt.LeftButton:
            super().mouseReleaseEvent(e)
            self.clicked.emit()

    def contextMenuEvent(self, e):
        super().contextMenuEvent(e)
        menu_position = self.mapToGlobal(e.pos())
        if self.menu.exec(menu_position) is not None:
            self.deleting.emit()


if __name__ == '__main__':
    users = [
        {
            "id": 0,
            "name": "Anton"
        },
        {
            "id": 1,
            "name": "Sergey"
        },
        {
            "id": 2,
            "name": "Vlad"
        },
    ]
    tests = [
        {
            "id": 0,
            "name": "test1"
        },
        {
            "id": 1,
            "name": "test2"
        },
        {
            "id": 2,
            "name": "test3"
        },
    ]
    app = QtWidgets.QApplication([])
    widget = AdminPanelView(users, tests)

    widget.add_new_entity_widget(Entity(7, "Added", EntityType.USER))
    widget.add_new_entity_widget(Entity(9, "AddedTest", EntityType.TEST))

    widget.edit_entity_widget(Entity(7, "NewNameOfAddedUser", EntityType.USER))
    widget.edit_entity_widget(Entity(9, "NewNameOfAddedTest", EntityType.TEST))

    widget.delete_entity_widget(Entity(7, "NewNameOfAddedUser", EntityType.USER))
    widget.delete_entity_widget(Entity(9, "NewNameOfAddedTest", EntityType.TEST))

    widget.show()
    app.exec_()
