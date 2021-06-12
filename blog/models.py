from django.db import models
from django.utils import timezone

# Create your models here.
class BlogPage(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(help_text="Enter your whole blog content here you can use HTML tags to style your blog as you want i.e. <style></style>, <b></b> etc.")
    pub_date = models.DateTimeField()
    author = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(BlogPage, on_delete=models.CASCADE,related_name='comments', null=True, blank=True)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField()
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Comment by {self.name}.'



