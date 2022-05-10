from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

# urls
from cride.users.api.views import UserViewSet
from cride.circles.views import CircleViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("circles", CircleViewSet)



app_name = "api"
urlpatterns = router.urls

