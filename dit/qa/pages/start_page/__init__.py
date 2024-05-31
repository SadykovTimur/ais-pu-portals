from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text_field import TextField
from selenium.common.exceptions import NoSuchElementException

__all__ = ['StartPage']


class StartPage(Page):
    logo = Component(css='[class*="logo"]')
    login = TextField(id="login")
    password = TextField(css='[placeholder="Пароль"]')
    checkbox = Component(css='[class*="checkbox"]')
    submit = Button(xpath="//span[text()=' Войти ']")
    footer = Component(css='[class*="footer"]')

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.logo.visible
                assert self.login.visible
                assert self.password.visible
                assert self.submit.visible
                assert self.checkbox.visible

                return self.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
