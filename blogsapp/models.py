from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=150)
    active=models.BooleanField(default=True)
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 related_name="blogs",
                                 default=None)