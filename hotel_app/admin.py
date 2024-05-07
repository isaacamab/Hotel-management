from django.contrib import admin

# Register your models here.
from .models import Room, Guest, Reservation, Staff, Billing

admin.site.register(Room)
admin.site.register(Guest)
admin.site.register(Reservation)
admin.site.register(Staff)
admin.site.register(Billing)
