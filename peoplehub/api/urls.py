from django.urls import path
from .import views

urlpatterns = [
    path('singleobj/<int:id>/', views.SingleObjAPIView.as_view()),
    path('multipleobj/', views.MultipleObjAPIView.as_view()),
]
