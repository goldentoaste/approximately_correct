from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
import calc.views as views
urlpatterns = [
    path('/<int:coffeeID>/', views.CoffeeTest.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)