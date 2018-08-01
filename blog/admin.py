from django.contrib import admin
#from .models import Post
#admin.site.register(Post)

from  blog import models
myModels = [models.Post]

admin.site.register(myModels)
