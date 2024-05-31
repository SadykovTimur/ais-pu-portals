from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text_field import TextField

__all__ = ['Container']


class ContainerWrapper(ComponentWrapper):
    title = Component(xpath="//h1[text()='Главная']")
    title_profile = Component(xpath="//h1[text()='Личный кабинет']")
    widget = Components(css='[class*="widget__content"] ')
    footer = Component(css='[class*="footer__bottom"]')
    data = Component(xpath="//div[text()='Мои данные']")
    admin = Component(xpath="//h3[text()='Администратор Сайта']")
    contacts_btn = Button(id="Contacts")
    contacts = Component(xpath="//div[text()='Контакты']")
    mobile = Component(xpath="//label[text()='Мобильный телефон']")
    field_number = TextField(css="[id*='MobilePhone'] span input")
    save = Button(xpath="//button[text()='Сохранить']")
    clear = Button(css='[class*="clear"]')


class Container(Component):
    def __get__(self, instance, owner) -> ContainerWrapper:
        return ContainerWrapper(instance.app, self.find(instance), self._locator)
