from django.contrib import admin
from .models import Provider, Category, Movie, episode, Historywatch, Viewer, comment

# Register your models here.
admin.site.register(Provider)
admin.site.register(Category)
admin.site.register(Movie)
admin.site.register(episode)
admin.site.register(Historywatch)
admin.site.register(Viewer)
admin.site.register(comment)

