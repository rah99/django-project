from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")

    def __str__(self):
        return f"{self.user.username} Profile"

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    # def save(self, *args, **kwargs):
    #     try:
    #         this = Profile.objects.get(id=self.id)
    #         if this.image != self.image:
    #             this.image.delete()
    #     except:
    #         pass

    #     # if exists.self.id:
    #     #     old_img = Profile.objects.get(id=self.id)
    #     super().save(*args, **kwargs)

    #     # resize image
    #     new_img = Image.open(self.image.path)

    #     # # deleting old one
    #     # if old_img.image != self.image:
    #     #     old_img.image.delete(save=False)

    #     if new_img.height > 300 or new_img.width > 300:
    #         # 300 X 300 pixel
    #         output_size = (300, 300)

    #         new_img.thumbnail(output_size)
    #         new_img.save(self.image.path)
