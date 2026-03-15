from django.contrib import admin
from django.urls import path
from evaluator import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('ethical-metrics-dashboard/', views.ethical_metrics_dashboard, name='ethical_metrics_dashboard'),
    path('api/ethical-metrics', views.ethical_metrics_api, name='ethical_metrics_api'),
    path('evaluate/', views.evaluate_prompt, name='evaluate'),
    path('curated-tests/', views.run_curated_tests, name='curated_tests'),
]
