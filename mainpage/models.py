from typing import List
from django.db import models

# Create your models here.
class Detail(models.Model):
    name = models.CharField(max_length=30,help_text="Your Name")
    description = models.CharField(max_length=350, help_text="Decribe your current status i.e Python Developer,App Developer etc.(Don't forget to seperate your designations with comma.)", null=True, blank=True)
    background_photo = models.ImageField(upload_to='profile/')
    profile_photo = models.ImageField(upload_to='profile/')
    post = models.CharField(max_length=100, help_text="Your Current Status i.e. Developer, Student, Intern etc.")
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    skill = models.CharField(max_length=2500)
    about_me = models.TextField(help_text="Describe Yourself", null=True, blank=True)
    services = models.TextField(null=True, blank=True, help_text="Services You Provide i.e. Web Developement than write it in this form == Web Developement:Its a very good job to do.:desktop </br> here Web Developement == Title</br>Its a very good job to do == Description</br>desktop == icon label from fontawesome i.e. work to use with fa fa-desktop etc.")
    complete_work = models.CharField(max_length=5, help_text="Works/Projects You have successfully completed.")
    years_experiance = models.CharField(max_length=2, help_text="Years of experience you have.")
    certificates = models.CharField(max_length=4, help_text="Number of certificated you possess related to your field.")
    award_won = models.CharField(max_length=3, help_text="Awards you have won in your field.")
    address = models.CharField(max_length=100)
    facebook = models.URLField()
    instagram = models.URLField()
    github = models.URLField()
    whatsapp = models.URLField(help_text="Enter your whatsapp number i.e. 917990578779")  

    def delete(self, using=None, keep_parents=False):
        self.background_photo.storage.delete(self.background_photo.name)
        self.profile_photo.storage.delete(self.profile_photo.name)
        super().delete()

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    checked = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Message From {self.name}'

class Certificate(models.Model):
    title = models.CharField(max_length=500)
    issuing_authority = models.CharField(max_length=500, help_text="Name Of Issuing Authority.")
    certi_id = models.CharField(max_length=300, help_text="ID of your certificate.")
    image = models.ImageField(upload_to='certificates/')
    url = models.URLField(blank=True, null=True, help_text="URL where one can see your certificate or verify it. It's optional.")

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()

    def __str__(self):
        return self.title