from View.view import View
from Model.entity import Entity, EntityType
from config import Config
from PyQt5 import QtCore, QtWidgets


class AdminPanelSignals(QtCore.QObject):
    creating_clicked = QtCore.pyqtSignal(EntityType)
    editing_clicked = QtCore.pyqtSignal(Entity)
    deleting_clicked = QtCore.pyqtSignal(Entity)


class AdminPanelView(View):
    def __init__(self, users: list, tests: list):
        super().__init__(AdminPanelSignals())
        self.__set_interface_settings()

        self.tab_widget = QtWidgets.QTabWidget()
        self.user_tab_layout = self.__create_tab_widget(users, EntityType.USER)
        self.test_tab_layout = self.__create_tab_widget(tests, EntityType.TEST)

        container = QtWidgets.QVBoxLayout(self)
        container.addWidget(self.tab_widget)

    def add_new_entity_widget(self, entity: Entity):
        entity_widget = self.__create_entity_widget(entity)
        if entity.type == EntityType.TEST:
            self.test_tab_layout.addWidget(entity_widget)
        elif entity.type == EntityType.USER:
            self.user_tab_layout.addWidget(entity_widget)
        else:
            raise Exception("There are no this entity type")

    def edit_entity_widget(self, entity):
        entity_widget = self.__find_widget_in_entity_layout(entity)
        entity_widget.setText(entity.name)

    def delete_entity_widget(self, entity):
        layout = self.test_tab_layout if entity.type == EntityType.TEST else self.user_tab_layout
        entity_widget = self.__find_widget_in_entity_layout(entity)
        layout.removeWidget(entity_widget)

    def __set_interface_settings(self):
        self.setMinimumSize(1280, 720)
        with open(Config.get_path() + '/View/css/admin_panel_view.css') as css:
            self.setStyleSheet(css.read())

    def __create_tab_widget(self, entity_list: list, entity_type: EntityType):
        """
        Automatically adds itself in tab_widget
        :param entity_list: list of entities (users or tests)
        :param entity_type: type of entities (EntityType.TEST or EntityType.USER)
        :return: layout that shows all entities from entity_list
        """

        entities_layout = self.__generate_entities_layout(entity_list, entity_type)
        entities_layout_wrapper = self.__create_wrapper_widget(entities_layout)
        entities_scroll_widget = self.__generate_scroll_widget(entities_layout_wrapper)

        new_entity_button = self.__generate_new_entity_button(entity_type)

        final_widget_layout = QtWidgets.QVBoxLayout()
        self.__layout_add_widgets(final_widget_layout, entities_scroll_widget, new_entity_button)
        final_widget = self.__create_wrapper_widget(final_widget_layout)

        tab_name = self.__get_tab_name(entity_type)
        self.tab_widget.addTab(final_widget, tab_name)
        return entities_layout

    def __generate_entities_layout(self, entity_list: list, entity_type: EntityType):
        entities_list_layout = QtWidgets.QVBoxLayout()

        for entity in entity_list:
            entity_object = Entity(entity["id"], entity["name"], entity_type)
            entity_widget = self.__create_entity_widget(entity_object)
            entities_list_layout.addWidget(entity_widget)

        return entities_list_layout

    def __generate_new_entity_button(self, entity_type: EntityType):
        button_entity_name = self.__get_button_entity_name(entity_type)
        new_entity_button = QtWidgets.QPushButton(f"Добавить {button_entity_name}")
        new_entity_button.released.connect(lambda: self.__new_entity_button_released(entity_type))
        return new_entity_button

    @staticmethod
    def __generate_scroll_widget(widget_to_set: QtWidgets.QWidget):
        scroll_widget = QtWidgets.QScrollArea()

        scroll_widget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        scroll_widget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        scroll_widget.setWidgetResizable(True)
        scroll_widget.setWidget(widget_to_set)

        return scroll_widget

    def __create_entity_widget(self, entity: Entity):
        widget = EntityWidget(entity)
        widget.setFixedSize(self.width() - 60, 50)
        widget.clicked.connect(lambda: self.__entity_widget_clicked(entity))
        widget.deleting.connect(lambda: self.__entity_widget_deleting(entity))
        return widget

    def __new_entity_button_released(self, entity_type: EntityType):
        self.signals.creating_clicked.emit(entity_type)

    def __entity_widget_clicked(self, entity: Entity):
        self.signals.editing_clicked.emit(entity)

    def __entity_widget_deleting(self, entity: Entity):
        self.signals.deleting_clicked.emit(entity)

    def __find_widget_in_entity_layout(self, entity: Entity):
        layout = self.test_tab_layout if entity.type == EntityType.TEST else self.user_tab_layout
        for i in range(layout.count()):
            widget = layout.itemAt(i).widget()
            if widget.entity.id == entity.id:
                return widget
        raise Exception("Can't find widget that contains this entity")

    @staticmethod
    def __layout_add_widgets(layout: QtWidgets.QLayout, *widgets: QtWidgets.QWidget):
        for widget in widgets:
            layout.addWidget(widget)

    @staticmethod
    def __create_wrapper_widget(layout: QtWidgets.QLayout):
        wrapper_widget = QtWidgets.QWidget()
        wrapper_widget.setLayout(layout)
        return wrapper_widget

    @staticmethod
    def __get_button_entity_name(entity_type: EntityType):
        return "тест" if entity_type == EntityType.TEST else "сотрудника"

    @staticmethod
    def __get_tab_name(entity_type: EntityType):
        return "Тесты" if entity_type == EntityType.TEST else "Сотрудники"


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
