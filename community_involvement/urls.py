from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("programs/", views.programs, name="programs"),
    path("projects/", views.projects, name="projects"),
    path("reports/", views.reports, name="reports"),
    # Forms
    path("program-form/", views.program_form, name="program-form"),
    path("project-form/", views.project_form, name="project-form"),
    # Add Program
    path("program-form/add_program/", views.add_program, name="add_program"),
    path("program-form/add_project/", views.add_project, name="add_project"),
    # Mode
    path("projects/gcash-mode", views.gcash_mode, name="gcash-mode"),
    path("projects/paymaya-mode", views.paymaya_mode, name="paymaya-mode"),
]
