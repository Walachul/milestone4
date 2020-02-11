from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from PIL import Image, ImageDraw
import io
from django.core.files.uploadedfile import InMemoryUploadedFile

from .forms import (
    RegisterUserForm,
    ProfileForm,
    UserLoginForm,
    UpdateUserForm,
    UpdateProfileForm,
)


@login_required
def logout(request):
    """Logout the user if he is already authenticated"""
    auth.logout(request)
    messages.success(request, f"You have successfully been logged out!")
    return redirect(reverse("home-home"))


def login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(
                username=request.POST["username"], password=request.POST["password"]
            )
            if user:
                auth.login(user=user, request=request)
                messages.success(request, f"You have successfully logged in!")
                return redirect(reverse("home-home"))
            else:
                form.add_error(None, f"Your username or password is incorrect!")
    else:
        form = UserLoginForm()

    return render(request, "users/login.html", {"form": form})


def register(request):

    """ Return to home page if user is authenticated """
    if request.user.is_authenticated:
        return redirect(reverse("home-home"))
    """Register users view."""
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            messages.success(
                request,
                f"The account for {username} was created successfully! You are now able to login",
            )
            return redirect("login")
    else:
        form = RegisterUserForm()
        profile_form = ProfileForm()
    return render(
        request, "users/register.html", {"form": form, "profile_form": profile_form}
    )


@login_required
def profile(request):
    """User account view"""
    if request.method == "POST":
        updateForm = UpdateUserForm(request.POST, instance=request.user)
        profileUpdateForm = UpdateProfileForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        if updateForm.is_valid() and profileUpdateForm.is_valid():
            updateForm.save()
            profileUpdateForm.save()
            messages.success(request, f"You have successfully updated your acount!")
            return redirect("profile")
    else:
        updateForm = UpdateUserForm(instance=request.user)
        profileUpdateForm = UpdateProfileForm(instance=request.user.profile)
        """Create Membership Card"""

        """Get data from current user and store it for future use"""
        current_user = request.user
        first_name = current_user.first_name
        last_name = current_user.last_name
        address = current_user.profile.homeAddress
        """Get Club's logo"""
        pic = Image.open(
            "static/img/logo/Romanian_Alpine_Club_Logo_transparent.png", "r"
        )
        pic_w, pic_h = pic.size
        """Create new Image with Pillow"""
        img = Image.new("RGB", (600, 350), color="#00AEEF")
        img_w, img_h = img.size
        offset = ((img_w - pic_w) // 2, (img_h - pic_h) // 2)
        """Insert data into the new image"""
        d = ImageDraw.Draw(img)
        d.text((70, 30), first_name, fill=(255, 255, 255))
        d.text((140, 30), last_name, fill=(255, 255, 255))
        d.text((40, 60), "Address      " + address, fill=(255, 255, 255))

        img.paste(pic, offset)
        """Create a file-like object to write img data"""
        img_io = io.BytesIO()
        img.save(img_io, format="JPEG")
        """Create a new Django file-like object to be used 
            in models as ImageField using InMemoryUploadedFile. """
        img_file = InMemoryUploadedFile(
            img_io,
            None,
            first_name + last_name + ".jpg",
            "image/jpeg",
            img_io.tell,
            None,
        )
        membershipCard = current_user.profile.membershipCard
        img_name = first_name + "_" + last_name + ".png"
        """Save the new object in membershipCard ImageField"""
        membershipCard.save(img_name, img_file)

    return render(
        request,
        "users/profile.html",
        {"updateForm": updateForm, "profileUpdateForm": profileUpdateForm},
    )

