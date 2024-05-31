from typing import Callable

import allure
import pytest
from _pytest.fixtures import FixtureRequest
from coms.qa.fixtures.application import Application
from coms.qa.frontend.constants import CLIENT_BROWSERS, CLIENT_DEVICE_TYPE

from tests.steps import (
    check_delete_phone_number,
    check_input_phone_number,
    open_contact,
    open_main_page,
    open_start_page,
    open_user_profile,
    sign_in,
)


@allure.label('owner', 't.sadykov')
@allure.label('component', 'DIT')
@allure.epic('AIS-PU-PORTALS')
@allure.story('Cтраница профиля пользователя')
@allure.title('Удаление номера телефона')
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.parametrize('browser', CLIENT_BROWSERS)
@pytest.mark.parametrize('device_type', CLIENT_DEVICE_TYPE)
def test_delete_number_phone(
    request: FixtureRequest, make_app: Callable[..., Application], browser: str, device_type: str
) -> None:

    app = make_app(browser, device_type)

    open_start_page(app)

    sign_in(app, request.config.option.username, request.config.option.password)
    open_main_page(app)

    open_user_profile(app)

    open_contact(app)
    check_input_phone_number(app, '1111111111', '+7 (111) 111-1111')
    check_delete_phone_number(app, '')
