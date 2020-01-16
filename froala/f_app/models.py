from django.db import models
from froala_editor.fields import FroalaField

# Create your models here.
class Page2(models.Model):
    temat = models.TextField()
    content = FroalaField()