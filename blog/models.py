from django.db import models
from six import python_2_unicode_compatible
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # Watch indent otherwise this will not work and will not show the title in areas like the admin page
    # dunder/magic method = dunder = double underscore
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
