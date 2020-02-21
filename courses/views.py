from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Courses, Notions, EnrollingRequirements, GearRequirements


@login_required()
def CourseList(request):

    courses = Courses.objects.all()

    return render(
        request, "courses/courses.html", {"title": "Courses", "courses": courses}
    )


@login_required()
def CourseDetail(request, pk):

    course = get_object_or_404(Courses, pk=pk)
    notions = Notions.objects.filter(course_id=course.pk).all()
    enrollReq = EnrollingRequirements.objects.filter(course_id=course.pk).all()
    gearReq = GearRequirements.objects.filter(course_id=course.pk).all()

    return render(
        request,
        "courses/course_details.html",
        {
            "course": course,
            "notions": notions,
            "enrollReq": enrollReq,
            "gearReq": gearReq,
        },
    )

