from django.urls import path,include

from rest_framework.routers import DefaultRouter

from users_api import views

router=DefaultRouter()
router.register('profile',views.UserProfileViewSet)
router.register('packaging_line',views.PackagingLineViewSet)
router.register('line_control',views.Line_control_detailsViewSet)
router.register('batch',views.Batch_detailsViewSet)
router.register('results',views.Batch_Test_resultsViewSet)

urlpatterns=[
    path('login/', views.UserLoginApiView.as_view()),
    path('states/', views.states),
    path('userLength/', views.lenUser),

    path('',include(router.urls)),
]