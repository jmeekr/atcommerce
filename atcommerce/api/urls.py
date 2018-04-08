from django.urls import path, include
from rest_framework import routers
from .dashboard import DashboardViewSet

"""
This is our api gateway which provides interaction
for users to upload files to the database, and view
rows in the database
"""

router = routers.SimpleRouter()
router.register(r'dashboard', DashboardViewSet)

urlpatterns = router.urls
