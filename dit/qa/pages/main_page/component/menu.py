from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['Menu']


class MenuWrapper(ComponentWrapper):
    admin = Button(xpath="//a[text()='Администратор Сайта']")
    chat = Component(css='[class*="chat"]')
    notifications = Component(css='[class*="notifications"]')
    profile = Button(xpath="//button[text()='Профиль']")
    employee = Component(xpath="//span[text()='Сотрудники']")
    organisation = Component(xpath="//span[text()='Организации']")
    map = Component(xpath="//span[text()='Карта рассадки']")
    structure = Component(xpath="//span[text()='Оргструктура']")
    question = Component(xpath="//span[text()='Вопросы и ответы']")
    calendar = Component(xpath="//span[text()='Календарь']")
    report = Component(xpath="//span[text()='Сообщить об ошибке']")
    send = Component(xpath="//span[text()='Перейти в 1С']")
    exit = Button(xpath="//a[text()='Выйти']")

    def is_visible(self) -> bool:
        assert self.admin.visible
        assert self.chat.visible
        assert self.notifications.visible
        assert self.profile.visible
        assert self.employee.visible
        assert self.organisation.visible
        assert self.map.visible
        assert self.structure.visible
        assert self.question.visible
        assert self.calendar.visible
        assert self.report.visible

        return self.send.visible


class Menu(Component):
    def __get__(self, instance, owner) -> MenuWrapper:
        return MenuWrapper(instance.app, self.find(instance), self._locator)
