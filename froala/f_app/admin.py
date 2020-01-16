from django.contrib import admin
from f_app.models import *

# Register your models here.
@admin.register(Page2)
class Page2Admin(admin.ModelAdmin):
    model = Page2
