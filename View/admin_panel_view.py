from View.view import View
from Model.entity import Entity, EntityType, User, Test, Question
from config import Config
from PyQt5 import QtCore, QtWidgets
from View.ui_utils import UiUtils


class AdminPanelSignals(QtCore.QObject):
    creating_clicked = QtCore.pyqtSignal(EntityType)
    editing_clicked = QtCore.pyqtSignal(Entity)
    deleting_clicked = QtCore.pyqtSignal(Entity)


class AdminPanelView(View):
    def __init__(self, users: list[User], tests: list[Test]) -> None:
        super().__init__(AdminPanelSignals())
        self.__set_interface_settings()

        self.tab_widget = QtWidgets.QTabWidget()
        self.user_tab_layout = self.__create_tab_widget(users, EntityType.USER)
        self.test_tab_layout = self.__create_tab_widget(tests, EntityType.TEST)

        container = QtWidgets.QVBoxLayout(self)
        container.addWidget(self.tab_widget)

    def add_new_entity_widget(self, entity: Entity) -> None:
        entity_widget = self.__create_entity_widget(entity)
        if entity.type == EntityType.TEST:
            self.test_tab_layout.addWidget(entity_widget)
        elif entity.type == EntityType.USER:
            self.user_tab_layout.addWidget(entity_widget)
        else:
            raise Exception("There are no this entity type")

    def edit_entity_widget(self, entity: Entity) -> None:
        entity_widget = self.__find_widget_in_entity_layout(entity)
        entity_widget.setText(entity.name)

    def delete_entity_widget(self, entity: Entity) -> None:
        layout = self.test_tab_layout if entity.type == EntityType.TEST else self.user_tab_layout
        entity_widget = self.__find_widget_in_entity_layout(entity)
        layout.removeWidget(entity_widget)

    def __set_interface_settings(self) -> None:
        self.setMinimumSize(1280, 720)
        with open(Config.get_path() + '/View/css/admin_panel_view.css') as css:
            self.setStyleSheet(css.read())

    def __create_tab_widget(self, entity_list: list[Entity], entity_type: EntityType) -> QtWidgets.QVBoxLayout:
        """
        Automatically adds itself in tab_widget
        :param entity_list: list of entities (users or solved_tests)
        :param entity_type: type of entities (EntityType.TEST or EntityType.USER)
        :return: layout that shows all entities from entity_list
        """

        entities_layout = self.__generate_entities_layout(entity_list)
        entities_layout_wrapper = UiUtils.generate_widget_with_layout(entities_layout)
        entities_scroll_widget = UiUtils.generate_scroll_widget(entities_layout_wrapper)

        new_entity_button = self.__generate_new_entity_button(entity_type)

        final_widget_layout = UiUtils.generate_vertical_layout(entities_scroll_widget, new_entity_button)
        final_widget = UiUtils.generate_widget_with_layout(final_widget_layout)

        tab_name = self.__get_tab_name(entity_type)
        self.tab_widget.addTab(final_widget, tab_name)
        return entities_layout

    def __generate_entities_layout(self, entity_list: list[Entity]) -> QtWidgets.QVBoxLayout:
        entities_list_layout = QtWidgets.QVBoxLayout()

        for entity in entity_list:
            entity_widget = self.__create_entity_widget(entity)
            entities_list_layout.addWidget(entity_widget)

        return entities_list_layout

    def __generate_new_entity_button(self, entity_type: EntityType) -> QtWidgets.QPushButton:
        button_entity_name = self.__get_button_entity_name(entity_type)
        new_entity_button = QtWidgets.QPushButton(f"Добавить {button_entity_name}")
        new_entity_button.released.connect(lambda: self.__new_entity_button_released(entity_type))
        return new_entity_button

    def __create_entity_widget(self, entity: Entity) -> QtWidgets.QWidget:
        widget = EntityWidget(entity)
        widget.setFixedSize(self.width() - 60, 50)
        widget.clicked.connect(lambda: self.__entity_widget_clicked(entity))
        widget.deleting.connect(lambda: self.__entity_widget_deleting(entity))
        return widget

    def __new_entity_button_released(self, entity_type: EntityType) -> None:
        self.signals.creating_clicked.emit(entity_type)

    def __entity_widget_clicked(self, entity: Entity) -> None:
        self.signals.editing_clicked.emit(entity)

    def __entity_widget_deleting(self, entity: Entity) -> None:
        self.signals.deleting_clicked.emit(entity)

    def __find_widget_in_entity_layout(self, entity: Entity) -> QtWidgets.QWidget:
        layout = self.test_tab_layout if entity.type == EntityType.TEST else self.user_tab_layout
        for i in range(layout.count()):
            widget = layout.itemAt(i).widget()
            if widget.entity.id == entity.id:
                return widget
        raise Exception("Can't find widget that contains this entity")

    @staticmethod
    def __get_button_entity_name(entity_type: EntityType) -> str:
        return "тест" if entity_type == EntityType.TEST else "сотрудника"

    @staticmethod
    def __get_tab_name(entity_type: EntityType) -> str:
        return "Тесты" if entity_type == EntityType.TEST else "Сотрудники"


class EntityWidget(QtWidgets.QLabel):
    clicked = QtCore.pyqtSignal()
    deleting = QtCore.pyqtSignal()

    def __init__(self, entity: Entity, parent=None) -> None:
        super().__init__(entity.name, parent)
        self.entity = entity
        self.menu = QtWidgets.QMenu(self)
        delete_action = QtWidgets.QAction("Удалить", self)
        self.menu.addAction(delete_action)

    def mouseReleaseEvent(self, e) -> None:
        if e.button() == QtCore.Qt.LeftButton:
            super().mouseReleaseEvent(e)
            self.clicked.emit()

    def contextMenuEvent(self, e) -> None:
        super().contextMenuEvent(e)
        menu_position = self.mapToGlobal(e.pos())
        if self.menu.exec(menu_position) is not None:
            self.deleting.emit()


if __name__ == '__main__':
    users = [
        User(1, "24")
    ]
    tests = [
        Test(
            1,
            "MyTest",
            "EGE",
            2,
            [
                Question("Govno?", "Yes", 1, ["Yes", "No"]),
                Question("2 + 2", "4", 1, ["1", "4"])
            ]
        )
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
