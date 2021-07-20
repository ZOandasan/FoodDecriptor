from django.contrib import admin
from .models import Food, Review, Side


# Register your models here.
admin.site.register(Food)
admin.site.register(Review)
admin.site.register(Side)