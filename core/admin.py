from django.contrib import admin
from django.shortcuts import render
from django import urls as urlresolvers
from django.utils.html import format_html
from .models import *

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'city', 'phone', 'membership', 'profile_approved', 'dues_paid')
    list_filter = ('profile_approved', 'dues_paid', 'gender', 'membership', 'city')
    search_fields = ['full_name', 'phone']

    def get_queryset(self, request):
        objects = Profile.objects.all()
        for obj in objects:
            if  obj.membership_updated_on is not None and obj.membership_expires_on is not None:
                if date.today() < obj.membership_expires_on:
                    obj.dues_paid = True
                else:
                    obj.dues_paid = False
        return Profile.objects.all().order_by('id')


class MembershipAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'active')
    list_filter = ('active',)
    search_fields = ['name']

class YearFilter(admin.SimpleListFilter):
    title = "Year"
    parameter_name = "year"

    def lookups(self, request, model_admin):
        qs = model_admin.model.objects.exclude(attendance_time=None).order_by(
            "attendance_time"
        )
        if qs:
            first_year = qs[0].attendance_time.year
            current_year = datetime.now().year
            return [(y, y) for y in range(first_year, current_year + 1)]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(attendance_time__year=self.value())
        else:
            return queryset


class MonthFilter(admin.SimpleListFilter):
    title = "Month"
    parameter_name = "month"

    def lookups(self, request, model_admin):
        return [
            (1, 'January'),
            (2, 'February'),
            (3, 'March'),
            (4, 'April'),
            (5, 'May'),
            (6, 'June'),
            (7, 'July'),
            (8, 'August'),
            (9, 'September'),
            (10, 'Octuber'),
            (11, 'November'),
            (12, 'December'),
            ]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(attendance_time__month=self.value())
        else:
            return queryset

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('member', 'attendance_time')
    list_filter = (MonthFilter, YearFilter, 'member__full_name')
    search_fields = ['member__full_name', 'member__id']


class InvoiceYearFilter(admin.SimpleListFilter):
    title = "Year"
    parameter_name = "year"

    def lookups(self, request, model_admin):
        qs = model_admin.model.objects.exclude(created_at=None).order_by(
            "created_at"
        )
        if qs:
            first_year = qs[0].created_at.year
            current_year = datetime.now().year
            return [(y, y) for y in range(first_year, current_year + 1)]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(created_at__year=self.value())
        else:
            return queryset


class InvoiceMonthFilter(admin.SimpleListFilter):
    title = "Month"
    parameter_name = "month"

    def lookups(self, request, model_admin):
        return [
            (1, 'January'),
            (2, 'February'),
            (3, 'March'),
            (4, 'April'),
            (5, 'May'),
            (6, 'June'),
            (7, 'July'),
            (8, 'August'),
            (9, 'September'),
            (10, 'Octuber'),
            (11, 'November'),
            (12, 'December'),
            ]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(created_at__month=self.value())
        else:
            return queryset



class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('member', 'amount', 'transaction', 'created_at', 'print_invoice')
    search_fields = ['member__full_name', 'member__id']
    list_filter = (InvoiceMonthFilter, InvoiceYearFilter, 'member__full_name')

    def print_invoice(self, obj):
        link = urlresolvers.reverse('invoice_print')
        return format_html(u'<a href="{}?id={}" target="_blank">Print</a>', link, obj.id)


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Membership, MembershipAdmin)
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(Invoice, InvoiceAdmin)
