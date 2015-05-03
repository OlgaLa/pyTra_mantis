__author__ = 'Властелин Вселенной'
from model.project import Project


def test_delete_project(app):
    app.session.login("administrator", "root")
    app.project.open_project_page()
    k= app.project.check_project_names(Project(name="delete"))
    if k !=1 :
        project = Project(name="delete", status="release", view="private", description="desc")
        app.project.create_project(project)

    old_projects = app.project.get_project_list()
    app.project.delete_project(project)
    new_projects = app.project.get_project_list()
    assert len(old_projects)-1+9 == len(new_projects)