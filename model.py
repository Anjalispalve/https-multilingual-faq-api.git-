from django.db import models
from ckeditor.fields import RichTextField

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()  # WYSIWYG editor support
    language = models.CharField(max_length=10, choices=[
        ('en', 'English'),
        ('hi', 'Hindi'),
        ('bn', 'Bengali'),
    ], default='en')

    def __str__(self):
        return self.question
