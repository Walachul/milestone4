from django.db import models
from django.contrib.auth.models import User
from PIL import Image, ImageDraw


class Profile(models.Model):
    """Extending the user profile by adding additional information.
        On delete argument CASCADE > when the user is deleted, his profile is deleted also,
        but if profile is deleted, user is not."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Additional information required for registration
    birthDate = models.DateField(blank=True, null=True)
    homeAddress = models.CharField(
        blank=True, max_length=200, default="Your home address"
    )
    phoneNumber = models.CharField(blank=True, max_length=20, default="0766 xxx xxx")
    profileImage = models.ImageField(default="default.jpg", upload_to="profile_images")

    """Implementing generation of card ID per user """
    cardID = models.ImageField(
        default="default_card.png", upload_to="profile_images/card_ID"
    )

    def __str__(self):
        return f"{self.user.username} Profile"

    """Override save function in order to resize the image,
        so that the file system will not get loaded with big files,
        affecting performance."""

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        imgProfile = Image.open(self.profileImage.path)
        if imgProfile.height > 300 or imgProfile.width > 300:
            outputSize = (300, 300)
            imgProfile.thumbnail(outputSize)
            imgProfile.save(self.profileImage.path)
        imgProfile_w, imgProfile_h = imgProfile.size
        imgCard = Image.new("RGB", (600, 400), color="#00AEEF")
        imgCard_w, imgCard_h = imgCard.size
        offset = ((imgCard_w - imgProfile_w) // 2, (imgCard_h - imgProfile_h) // 2)

        """
        Write user info on the new created image
        """
        d = ImageDraw.Draw(imgCard)

        d.text((40, 30), User.first_name, fill=(255, 255, 255))
        d.text((70, 30), User.last_name, fill=(255, 255, 255))
        d.text((40, 40), "Address      " + Profile.homeAddress, fill=(255, 255, 255))
        d.text(
            (40, 60), "Phone number      " + Profile.phoneNumber, fill=(255, 255, 255)
        )

        imgCard.paste(imgProfile)
        imgCard.save(self.cardID.path)

