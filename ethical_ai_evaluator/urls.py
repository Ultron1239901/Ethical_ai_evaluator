from django.contrib import admin
from django.urls import path
from evaluator import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('evaluate/', views.evaluate_prompt, name='evaluate'),
    path('curated-tests/', views.run_curated_tests, name='curated_tests'),
]