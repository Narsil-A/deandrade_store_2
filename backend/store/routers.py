from rest_framework.routers import DefaultRouter

from product.viewsets import ProductViewSet


router = DefaultRouter()
router.register('product-v2', ProductViewSet, basename='product')

urlpatterns = router.urls