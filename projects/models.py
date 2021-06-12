from django.db import models
from django.utils import timezone

# Create your models here.
class Project(models.Model):
    main_image = models.ImageField(upload_to='projects/')
    image1 = models.ImageField(upload_to='projects/')
    image2 = models.ImageField(upload_to='projects/')
    image3 = models.ImageField(upload_to='projects/')
    project_name = models.CharField(max_length=100)
    project_detail = models.TextField(help_text="Describe your project here you can HTML to style your description.")
    project_category = models.CharField(max_length=100, help_text="Technological, Python, Django, Database etc.")
    project_date = models.DateField()
    project_url = models.URLField(help_text="URL to see your project if not any then add github url of your source code.", blank=True, null=True)

    def delete(self, using=None, keep_parents=False):
        self.main_image.storage.delete(self.main_image.name)
        self.image1.storage.delete(self.image1.name)
        self.image2.storage.delete(self.image2.name)
        self.image3.storage.delete(self.image3.name)
        super().delete()

    def __str__(self):
        return self.project_name