from View.authorization_view import AuthorizationView
from Model.authorization_model import AuthorizationModel
from Presenter.authorization_presenter import AuthorizationPresenter


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

    def open_admin_panel(self):
        self.auth_view.close()
        print("Opening admin panel")

    def open_test_selection_window(self, user: dict):
        self.auth_view.close()
        print(f"Opening test selection for {user['name']}")
