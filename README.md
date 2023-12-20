В файле locators.py описаны все используемые локаторы в проекте.

Тесты по регистрации находятся в папке tests_registration:
1. Тест по успешной регистрации - test_successful_registration.py (тут подключила генерацию логина и пароля из доп задания)
2. Тест по ошибке некорректного пароля - test_registration_with_incorrect_password.py

Тесты по входу в личный кабинет находятся в папке tests_login_to_account:
1. Тест входа по кнопке «Войти в аккаунт» на главной странице - test_login_through_account_button_on_main_page.py
2. Тест входа через кнопку «Личный кабинет» - test_login_through_private_office_button.py
3. Тест входа через кнопку в форме регистрации - test_login_through_registration_form.py
4. Тест входа через кнопку в форме восстановления пароля - test_login_through_regeneration_password_form.py

Тесты по работе в личном кабинете находятся в папке tests_work_in_private_account:
1. Тест по переходу в личный кабинет - test_go_to_private_account.py
2. Тест по переходу из личного кабинета в конструктор - test_move_from_private_account_to_constructor.py
3. Тест по переходу из личного кабинета на логотип Stellar Burgers - test_move_from_private_account_to_logo.py
4. Тест выхода из аккаунта - test_exit_from_private_account.py

Тесты по Конструктору находятся в папке tests_for_section_constructor:
1. Тест по переходу к разделу «Булки» - test_for_section_buns.py
2. Тест по переходу к разделу «Соусы» - test_for_section_sauces.py
3. Тест по переходу к разделу «Начинки» - test_for_section_fillings.py


# Sprint_5
