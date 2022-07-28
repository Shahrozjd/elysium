from core.views import *
from rest_framework import routers

router =routers.DefaultRouter()
router.register('profiles', ProfileViewSet)
router.register('membserships', MembershipViewSet)
router.register('attendance', AttendanceViewSet)
router.register('invoice', InoiceViewSet)
