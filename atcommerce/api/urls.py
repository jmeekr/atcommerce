from django.urls import path, include
from rest_framework import routers
from .dashboard import DashboardViewSet, CustomerViewSet, ProductViewSet

"""
This is our api gateway which provides interaction
for users to upload files to the database, and view
rows in the database
"""

router = routers.SimpleRouter()
router.register(r'dashboard', DashboardViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = router.urls
