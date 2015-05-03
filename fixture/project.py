from selenium.webdriver.support.ui import Select


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def create_project(self, project):
        wd = self.app.wd
        wd.get("http://localhost/mantisbt-1.2.19/manage_proj_create_page.php")
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project.name)
        dropdown = wd.find_element_by_name('status')
        select = Select(dropdown)
        select.select_by_visible_text(project.status)
        wd.find_element_by_name("inherit_global").click()
        dropdown = wd.find_element_by_name('view_state')
        select = Select(dropdown)
        select.select_by_visible_text(project.view)
        wd.find_element_by_name("description").click()
        wd.find_element_by_name("description").clear()
        wd.find_element_by_name("description").send_keys(project.name)
        wd.find_element_by_css_selector('input[value="Add Project"]').click()

    def open_project_page(self):
        wd = self.app.wd
        wd.get("http://localhost/mantisbt-1.2.19/manage_proj_page.php")

    def get_project_list(self):
        wd = self.app.wd
        self.open_project_page()
        projects = wd.find_elements_by_css_selector('tr[class="row-1"]') + wd.find_elements_by_css_selector('tr[class="row-2"]')
        return projects

    def check_project_names(self, project):
        wd = self.app.wd
        project_names_list = wd.find_elements_by_xpath("//a[text()='{0}']")
        if project.name in project_names_list:
            k = 1
            return k


    def delete_project(self, project):
        wd = self.app.wd
        wd.find_element_by_link_text(project.name).click()
        wd.find_element_by_css_selector('input[value="Delete Project"]').click()
        wd.find_element_by_css_selector('input[value="Delete Project"]').click()
