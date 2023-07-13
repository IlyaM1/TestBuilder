from Presenter.presenter import Presenter
from Model.authorization_model import LoginStatus, EmptyFieldLoginException, IncorrectAuthInfoLoginException
from View.ui_utils import UiUtils


class AuthorizationPresenter(Presenter):
    def __init__(self, view, model) -> None:
        super().__init__(view, model)
        self.view.signals.login_clicked.connect(self.login)

    def login(self) -> None:
        auth_info = self.view.get_auth_info()
        try:
            login_status = self.model.login(auth_info)
        except EmptyFieldLoginException:
            UiUtils.call_error_window("Остались пустые поля ввода")
        except IncorrectAuthInfoLoginException:
            UiUtils.call_error_window("Неправильное имя или пароль пользователя")
        else:
            from window_manager import WindowManager
            if login_status == LoginStatus.ADMIN:
                WindowManager.get_instance().open_admin_panel(self.model.get_users(), self.model.get_tests())
            elif login_status == LoginStatus.USER:
                user = self.model.get_user_by_auth_info(auth_info)
                WindowManager.get_instance().open_test_selection_window(user, self.model.get_tests())
