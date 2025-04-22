import allure


def test_google_auth():
    with allure.step("Открываем главную страницу"):
        pass
    with allure.step("Выбираем способ авторизации Google"):
        pass
    with allure.step("Авторизуемая как пользователь Mr.Random"):
        with allure.step("Вводим логин random@gmail.com"):
            pass
        with allure.step("Вводим пароль random-pass"):
            pass
        with allure.step("Нажимаем кнопку Войти"):
            pass
    with allure.step("Проверяем что авторизовались успешно"):
        pass
    with allure.step("Проверяем что данные профиля обновились из Google"):
        with allure.step("Имя Mr.Random"):
            pass
        with allure.step("Email random@gmail.com"):
            pass