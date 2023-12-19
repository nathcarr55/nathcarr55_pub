from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Retreat, Attendee

# Register your models here.
admin.site.register(Retreat)
admin.site.register(Attendee)