from django.contrib import admin
from user_app.models import CustomUser,Project,Customer
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Customer)
admin.site.register(Project)