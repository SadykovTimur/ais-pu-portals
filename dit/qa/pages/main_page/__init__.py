from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.main_page.component.container import Container
from dit.qa.pages.main_page.component.menu import Menu

__all__ = ['MainPage']


class MainPage(Page):
    page = Container(id="page-container")
    menu = Menu(class_name="sidebar__content")

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.page.title.visible
                assert self.page.widget[0].visible

                assert self.menu.is_visible

                return self.page.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
