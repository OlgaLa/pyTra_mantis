__author__ = 'Властелин Вселенной'
import random
import string
from model.project import Project


def gen_name(prefix="pro", maxlen=10):
    sym = string.ascii_letters + string.digits
    return prefix+"".join([random.choice(sym) for i in range(maxlen)])


def test_add_project(app):
    username = app.config["webadmin"]["username"]
    password = app.config["webadmin"]["password"]
    old_projects = app.soap.get_projects_list(username, password)
    name = gen_name()
    project = Project(name=name, status="release", view="private", description="desc")
    app.project.create_project(project)
    new_projects = app.soap.get_projects_list(username, password)
    assert len(old_projects) == len(new_projects)-1
    app.project.check_project_names(Project(name=name))


