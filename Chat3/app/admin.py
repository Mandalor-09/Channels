from django.contrib import admin

# Register your models here.
from .models import Group,Chat

class Chat_admin(admin.ModelAdmin):
    list_display=['id','content','group','time']
admin.site.register(Chat,Chat_admin)

admin.site.register(Group)