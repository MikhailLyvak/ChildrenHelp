from django.db import models
from test_app.models import CustomUser


class ReqList(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="owner")
    helpers = models.ManyToManyField(CustomUser, blank=True)
    is_done = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date']
        verbose_name = 'Request'
        verbose_name_plural = 'Requests'

    def __str__(self) -> str:
        return f"{self.title}"
