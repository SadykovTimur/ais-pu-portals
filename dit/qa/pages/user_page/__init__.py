from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component.button import Button
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.main_page.component.container import Container
from dit.qa.pages.main_page.component.menu import Menu

__all__ = ['UserPage']


class UserPage(Page):
    page = Container(id="page-container")
    menu = Menu(class_name="sidebar__content")
    exit_modal = Button(xpath="//span[text()='Выйти']/ancestor::button")

    def wait_for_loading_user_profile(self) -> None:
        def condition() -> bool:
            try:
                assert self.page.title_profile.visible
                assert self.page.data.visible

                return self.page.admin.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def wait_for_loading_profile_contact(self) -> None:
        def condition() -> bool:
            try:
                assert self.page.contacts.visible
                assert self.page.field_number.visible

                return self.page.mobile.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def wait_for_loading_check_phone_number(self, phone_number: str) -> None:
        def condition() -> bool:
            try:
                return phone_number == self.page.field_number.value

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
