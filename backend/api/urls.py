from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path("user/register", views.CreateUserView.as_view(), name="register"),
    path("car/", views.CreateListCar.as_view(), name="car-list"),
    path("car/update/<int:pk>", views.UpdateDeleteCar.as_view(), name="car-update"),
    path("car/available/", views.ListAvailableCars.as_view(), name="available-list"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
