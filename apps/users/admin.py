from django.contrib import admin
from apps.users.models import User,Subscription,Membership
# Register your models here.
admin.site.register(User)
admin.site.register(Subscription)
admin.site.register(Membership)
