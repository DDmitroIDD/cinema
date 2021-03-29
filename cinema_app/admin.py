from django.contrib import admin

# Register your models here.
from cinema_app.models import CustomUser, CinemaHall, MovieSeance, Buying

admin.site.register(CustomUser)
admin.site.register(CinemaHall)
admin.site.register(MovieSeance)
admin.site.register(Buying)
