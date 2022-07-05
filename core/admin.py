from django.contrib import admin
from django.shortcuts import render
from django import urls as urlresolvers
from django.utils.html import format_html
from .models import *

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'city', 'phone', 'approved', 'dues_paid')
    list_filter = ('gender', 'city')
    search_fields = ['first_name', 'phone']


class MembershipAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'active')
    list_filter = ('active',)
    search_fields = ['name']


class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('member', 'attendance_time')
    list_filter = ('member__first_name',)


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Membership, MembershipAdmin)
admin.site.register(Attendance, AttendanceAdmin)
