from django.contrib import admin
from django.shortcuts import render
from django import urls as urlresolvers
from django.utils.html import format_html
from .models import *

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'city', 'phone', 'profile_approved', 'dues_paid')
    list_filter = ('profile_approved', 'dues_paid', 'gender', 'city')
    search_fields = ['full_name', 'phone']

    def get_queryset(self, request):
        objects = Profile.objects.all()
        for obj in objects:
            if  obj.membership_updated_on is not None and obj.membership_expires_on is not None:
                if date.today() < obj.membership_expires_on:
                    obj.dues_paid = True
                else:
                    obj.dues_paid = False
        return Profile.objects.all()


class MembershipAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'active')
    list_filter = ('active',)
    search_fields = ['name']


class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('member', 'attendance_time')
    list_filter = ('member__full_name',)


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Membership, MembershipAdmin)
admin.site.register(Attendance, AttendanceAdmin)
