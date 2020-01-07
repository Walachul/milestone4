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
    birthDate = models.DateField(blank=True, null=True)
    homeAddress = models.CharField(
        blank=True, max_length=200, default="Your home address"
    )
    phoneNumber = models.CharField(blank=True, max_length=20, default="0766 xxx xxx")
    profileImage = models.ImageField(default="default.jpg", upload_to="profile_images")
    cardID = models.ImageField(
        default="profile_images/card_ID/default_card.png",
        upload_to="profile_images/card_ID",
    )
    # # Saving the stripe_id/token in order to use it later for renewing/cancelling subscription
    # stripe_id = models.CharField(max_length=40, default="")
    # plan = models.CharField(max_length=60, default="")

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

        # imgProfile_w, imgProfile_h = imgProfile.size
        # logoImg = Image.open(
        #     "static/img/logo/Romanian_Alpine_Club_Logo_transparent.png", "r"
        # )
        # logoImg_w, logoImg_h = logoImg.size
        # imgCard = Image.new("RGB", (600, 350), color="#00AEEF")
        # imgCard_w, imgCard_h = imgCard.size
        # offsetlogo = (40, 10)
        # offset = (40, 190)

        # """
        # Write user info on the new created image
        # """
        # d = ImageDraw.Draw(imgCard)
        # firstName = User.first_name
        # lastName = User.last_name
        # Address = Profile.homeAddress
        # phone = Profile.phoneNumber
        # d.text((90 + imgProfile_w, -20 + imgProfile_h), firstName, fill=(255, 255, 255))
        # d.text((130 + imgProfile_w, -20 + imgProfile_h), lastName, fill=(255, 255, 255))
        # d.text((90 + imgProfile_w, -5 + imgProfile_h), Address, fill=(255, 255, 255))

        # imgCard.paste(logoImg, offsetlogo)
        # imgCard.paste(imgProfile, offset)

        # imgCard.save(
        #     "media/profile_images/card_ID/" + user.first_name + user.last_name + ".png"
        # )
        imgProfile_read.close()


# """ Implementing generation of card ID per user """


# class Card(models.Model):
#     profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

#     cardID = models.ImageField(
#         default="profile_images/card_ID/default_card.png",
#         upload_to="profile_images/card_ID",
#     )

#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)
#         imgProfile_w, imgProfile_h = imgProfile.size
#         logoImg = Image.open(
#             "static/img/logo/Romanian_Alpine_Club_Logo_transparent.png", "r"
#         )
#         logoImg_w, logoImg_h = logoImg.size
#         imgCard = Image.new("RGB", (600, 350), color="#00AEEF")
#         imgCard_w, imgCard_h = imgCard.size
#         offsetlogo = (40, 10)
#         offset = (40, 190)

#         """
#         Write user info on the new created image
#         """
#         d = ImageDraw.Draw(imgCard)
#         firstName = User.first_name
#         lastName = User.last_name
#         Address = Profile.homeAddress
#         phone = Profile.phoneNumber
#         d.text((90 + imgProfile_w, -20 + imgProfile_h), firstName, fill=(255, 255, 255))
#         d.text((130 + imgProfile_w, -20 + imgProfile_h), lastName, fill=(255, 255, 255))
#         d.text((90 + imgProfile_w, -5 + imgProfile_h), Address, fill=(255, 255, 255))

#         imgCard.paste(logoImg, offsetlogo)
#         imgCard.paste(imgProfile, offset)

#         imgCard.save(
#             "media/profile_images/card_ID/" + user.first_name + user.last_name + ".png"
#         )
