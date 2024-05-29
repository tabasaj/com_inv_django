from django.shortcuts import render, redirect
from .models import Program, Project, MOD


def home(request):

    return render(request, "base.html", {"url": "home"})


def programs(request):
    loadPrograms = Program.objects.all().order_by("-date_time")

    return render(
        request,
        "programs.html",
        {"url": "programs", "title": "Programs", "loadPrograms": loadPrograms},
    )


def projects(request):
    loadProjects = Project.objects.all().order_by("-date_time")

    return render(
        request,
        "projects.html",
        {"url": "projects", "title": "Projects", "loadProjects": loadProjects},
    )


def program_form(request):

    return render(request, "admin/programs-forms.html", {"url": "program-form"})


def project_form(request):

    return render(request, "admin/projects-forms.html", {"url": "project-form"})


def add_program(request):
    if request.method == "POST":
        Program(request.POST)

        title = request.POST.get("title")
        caption = request.POST.get("caption")
        image_upload = request.FILES.getlist("images")

        for image in image_upload:
            program = Program(
                title=title,
                caption=caption,
                image_upload=image,
            )
            program.save()

    return redirect("program-form")


def add_project(request):
    if request.method == "POST":
        Project(request.POST)

        title = request.POST.get("title")
        caption = request.POST.get("caption")
        image_upload = request.FILES.getlist("images")

        for image in image_upload:
            project = Project(
                title=title,
                caption=caption,
                image_upload=image,
            )
            project.save()

    return redirect("project-form")


def gcash_mode(request):
    if request.method == "POST":
        MOD(request.POST)

        donated = request.POST["title"]
        name = request.POST["name"]
        gcash_number = request.POST["gcash_number"]
        amount = request.POST["amount"]

        donation = MOD(
            donation_type="GCash",
            donated=donated,
            name=name,
            gcash_number=gcash_number,
            amount=amount,
        )

        donation.save()

    return redirect("projects")


def paymaya_mode(request):
    if request.method == "POST":
        MOD(request.POST)

        donated = request.POST["title"]
        name = request.POST["name"]
        paymaya_number = request.POST["paymaya_number"]
        amount = request.POST["amount"]

        donation = MOD(
            donation_type="PayMaya",
            donated=donated,
            name=name,
            paymaya_number=paymaya_number,
            amount=amount,
        )

        donation.save()

    return redirect("projects")


def volunteer_mode(request):
    return redirect("projects")


def reports(request):

    return render(request, "reports.html", {"url": "report"})
