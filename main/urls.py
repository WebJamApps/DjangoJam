from django.urls import include, path
# from django.conf.urls import url
from rest_framework import routers
from . import views
router = routers.DefaultRouter()
router.register(r'tutorials', views.TutorialViewSet)
app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("view/", views.homepage, name="homepage"),
    path("register/", views.register, name="register"),
    path("table/", views.ZeroConfigurationDatatableView.as_view(),
         name="datatableview"),
    path('tutorial/new/', views.tutorial_new, name='tutorial_new'),
    path('tutorial/<int:pk>/edit/', views.tutorial_edit, name='tutorial_edit'),
]
