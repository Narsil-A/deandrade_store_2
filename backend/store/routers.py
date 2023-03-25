from rest_framework.routers import DefaultRouter

from product.viewsets import ProductViewSet
router = DefaultRouter()
router.register('product', ProductViewSet, basename='product')
urlpatterns = router.urls