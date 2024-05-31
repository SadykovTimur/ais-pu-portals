import allure
from coms.qa.fixtures.application import Application
from coms.qa.frontend.helpers.attach_helper import screenshot_attach
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.main_page import MainPage
from dit.qa.pages.start_page import StartPage
from dit.qa.pages.user_page import UserPage

__all__ = [
    'open_start_page',
    'sign_in',
    'open_main_page',
    'open_user_profile',
    'open_contact',
    'check_input_phone_number',
    'check_delete_phone_number',
    'logout',
]


def open_start_page(app: Application) -> None:
    with allure.step('Opening Start page'):
        try:
            page = StartPage(app)
            page.open()

            page.wait_for_loading()

            screenshot_attach(app, 'start_page')
        except Exception as e:
            screenshot_attach(app, 'start_page_error')

            raise TimeoutError('Start page was not loaded') from e


def sign_in(app: Application, login: str, password: str) -> None:
    with allure.step(f'{login} signing in'):
        try:
            auth_form = StartPage(app)

            auth_form.login.send_keys(login)
            auth_form.password.send_keys(password)

            screenshot_attach(app, 'auth_data')
        except Exception as e:
            screenshot_attach(app, 'auth_data_error')

            raise NoSuchElementException('Entering data exception') from e

        auth_form.submit.click()


def open_main_page(app: Application) -> None:
    with allure.step('Opening Main page'):
        try:
            MainPage(app).wait_for_loading()

            screenshot_attach(app, 'main_page')
        except Exception as e:
            screenshot_attach(app, 'main_page_error')

            raise TimeoutError('Main page was not loaded') from e


def open_user_profile(app: Application) -> None:
    with allure.step('Opening User profile page'):
        try:
            page = MainPage(app)
            page.menu.admin.click()

            user = UserPage(app)
            user.wait_for_loading_user_profile()

            screenshot_attach(app, 'user_profile_page')
        except Exception as e:
            screenshot_attach(app, 'user_profile_page_error')

            raise TimeoutError('User profile page was not loaded') from e


def open_contact(app: Application) -> None:
    with allure.step('Opening profile contact'):
        try:
            page = UserPage(app)
            page.page.contacts_btn.click()

            page.wait_for_loading_profile_contact()

            screenshot_attach(app, 'profile_contact')
        except Exception as e:
            screenshot_attach(app, 'profile_contact_error')

            raise TimeoutError('Profile contact was not loaded') from e


def check_input_phone_number(app: Application, number: str, phone_number: str) -> None:
    with allure.step('Checking Input phone number'):
        try:
            phone = UserPage(app)
            phone.page.field_number.send_keys(number)
            phone.page.save.click()

            UserPage(app).wait_for_loading_check_phone_number(phone_number)

            screenshot_attach(app, 'input_phone_number')
        except Exception as e:
            screenshot_attach(app, 'input_phone_number_error')

            raise TimeoutError('Input phone number was not shown') from e


def check_delete_phone_number(app: Application, phone_number: str) -> None:
    with allure.step('Checking Delete phone number'):
        try:
            phone = UserPage(app)
            app.move_to_element(phone.page.field_number.webelement)
            phone.page.clear.click()
            phone.page.save.click()

            UserPage(app).wait_for_loading_check_phone_number(phone_number)

            screenshot_attach(app, 'delete_phone_number')
        except Exception as e:
            screenshot_attach(app, 'delete_phone_number_error')

            raise TimeoutError('Phone number was not deleted') from e


def logout(app: Application) -> None:
    with allure.step('Logout page'):
        try:
            user_page = UserPage(app)
            user_page.menu.profile.click()
            user_page.menu.exit.click()
            user_page.exit_modal.click()

            StartPage(app).wait_for_loading()

            screenshot_attach(app, 'logout_page')
        except Exception as e:
            screenshot_attach(app, 'logout_page_error')

            raise TimeoutError('Logout was not loaded') from e
