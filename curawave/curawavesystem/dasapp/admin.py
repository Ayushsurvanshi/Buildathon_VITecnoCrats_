<<<<<<< HEAD

from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin



# Register your models here.
class UserModel(UserAdmin):
    list_display =['username','email','user_type']
admin.site.register(CustomUser,UserModel)
admin.site.register(Specialization)
admin.site.register(DoctorReg)
admin.site.register(Appointment)
admin.site.register(Page)
=======

from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin



# Register your models here.
class UserModel(UserAdmin):
    list_display =['username','email','user_type']
admin.site.register(CustomUser,UserModel)
admin.site.register(Specialization)
admin.site.register(DoctorReg)
admin.site.register(Appointment)
admin.site.register(Page)
>>>>>>> aa4a07f314bd78359b974f32a3cf9dbabf421c1e
