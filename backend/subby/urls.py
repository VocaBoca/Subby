from rest_framework.routers import DefaultRouter
from .views import SubscriptionViewSet

router = DefaultRouter()
router.register("subby", SubscriptionViewSet)

urlpatterns = router.urls