from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import HowWeWork, HowWeWorkCheckList, Faq
# Register your models here.

admin.site.register(HowWeWork)
admin.site.register(HowWeWorkCheckList)
admin.site.register(Faq)
