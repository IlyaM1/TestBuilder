from Presenter.presenter import Presenter
from Model.authorization_model import LoginStatus


class AuthorizationPresenter(Presenter):
    def __init__(self, view, model):
        super().__init__(view, model)
        self.view.signals.login_clicked.connect(self.login)

    def login(self):
        auth_info = self.view.get_auth_info()
        login_status_array = self.model.login(auth_info)
        status = login_status_array[0]
        if status == LoginStatus.EMPTY_FIELDS:
            self.view.call_error_window("Остались пустые поля ввода")
        elif status == LoginStatus.INCORRECT_AUTH_INFO:
            self.view.call_error_window("Неправильное имя или пароль пользователя")
        elif status == LoginStatus.ADMIN:
            from window_manager import WindowManager
            WindowManager.get_instance().open_admin_panel(self.model.get_users(), self.model.get_tests())
        elif status == LoginStatus.USER:
            from window_manager import WindowManager
            user = login_status_array[1]
            WindowManager.get_instance().open_test_selection_window(user, self.model.get_tests())
