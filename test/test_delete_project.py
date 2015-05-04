__author__ = 'Властелин Вселенной'
from model.project import Project


def test_delete_project(app):
 #   app.session.login("administrator", "root")
    username = app.config["webadmin"]["username"]
    password = app.config["webadmin"]["password"]
    app.project.open_project_page()
#    k= app.project.check_project_names(Project(name="delete"))
    if  app.project.check_project_names(Project(name="delete")) != True:
        project = Project(name="delete", status="release", view="private", description="desc")
        app.project.create_project(project)

    old_projects = app.soap.get_projects_list(username, password)
    app.project.delete_project(project)
    new_projects = app.soap.get_projects_list(username, password)
    assert len(old_projects)-1 == len(new_projects)
