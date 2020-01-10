import io
from django.core.files.storage import default_storage as storage
from django.db import models
from django.contrib.auth.models import User
from PIL import Image, ImageDraw


class Profile(models.Model):
    """Extending the user profile by adding additional information.
        On delete argument CASCADE > when the user is deleted, his profile is deleted also,
        but if profile is deleted, user is not."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Additional information required for registration
    homeAddress = models.CharField(
        blank=True, max_length=200, default="Your home address"
    )
    profileImage = models.ImageField(default="default.jpg", upload_to="profile_images")

    def __str__(self):
        return f"{self.user.username} Profile"

    """Override save function in order to resize the image,
        so that the file system will not get loaded with big files,
        affecting performance. The resized image is now saved also on S3 Amazon"""

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        imgProfile_read = storage.open(self.profileImage.name, "r")
        imgProfile = Image.open(imgProfile_read)
        if imgProfile.height > 300 or imgProfile.width > 300:
            outputSize = (180, 135)
            imgProfile.thumbnail(outputSize)
            in_mem_file = io.BytesIO()
            imgProfile.save(in_mem_file, format="JPEG")
            img_write = storage.open(self.profileImage.name, "w+")
            img_write.write(in_mem_file.getvalue())
            img_write.close()

        imgProfile_read.close()

