

# Помощник сессий, содержит вспомогательные методы, которые относятся к открытию/закрытию сессии
class SessionHelper:

    def __init__(self, app): # конструктор, в качестве параметра принимает ссылку на фикстуру
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page() # обращение к методу перехода на гл.страницу через фикстуру
        wd.find_element_by_name("username").click()
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys(username)
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_css_selector('input[type="submit"]').click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()

    # метод проверяет что произошел выход из системы
    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0 # мы в системе

    def is_logged_in_as(self, username):
        wd = self.app.wd
        nameuser = wd.find_element_by_xpath("/html/body/table[1]/tbody/tr/td[1]/span[1]").text
        return nameuser == username




