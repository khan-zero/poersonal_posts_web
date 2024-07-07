from django.contrib import admin
from .models import *


admin.site.register(User)
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Liked)
admin.site.register(Comment)
admin.site.register(Shared)
admin.site.register(Blog_area_single_post)
