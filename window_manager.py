from Model.authorization_model import AuthorizationModel
from Model.admin_panel_model import AdminPanelModel
from Model.entity import User, Test, Question

from View.authorization_view import AuthorizationView
from View.admin_panel_view import AdminPanelView
from View.test_editor_view import TestEditorView

from Presenter.authorization_presenter import AuthorizationPresenter
from Presenter.admin_panel_presenter import AdminPanelPresenter
from Presenter.test_editor_presenter import TestEditorPresenter


class WindowManager:
    __instance = None

    def __init__(self):
        if self.__instance is None:
            self.auth_view = AuthorizationView()
            self.auth_model = AuthorizationModel()
            self.auth_presenter = AuthorizationPresenter(self.auth_view, self.auth_model)
        else:
            raise Exception("WindowManager instance already created")

    @staticmethod
    def get_instance():
        if WindowManager.__instance is None:
            WindowManager.__instance = WindowManager()
        return WindowManager.__instance

    def open_admin_panel(self, users: list, tests: list):
        self.auth_view.close()
        self.admin_panel_view = AdminPanelView(users, tests)
        self.admin_panel_model = AdminPanelModel()
        self.admin_panel_presenter = AdminPanelPresenter(self.admin_panel_view, self.admin_panel_model)

        self.admin_panel_view.show()

    def open_test_selection_window(self, user: User, tests: list):
        self.auth_view.close()
        print(f"Opening test selection for {user['name']}")

    def open_test_editor(self, test: Test = None):
        self.test_editor_view = TestEditorView(test)
        self.test_editor_presenter = TestEditorPresenter(view=self.test_editor_view)
        self.test_editor_view.show()

        return self.test_editor_presenter

    def open_user_editor(self, user: User = None):
        """
        :param user: user object (calls entity_dict in other places)
        :return: UserEditorPresenter instance
        """
        pass
