from django.urls import path, include
from . import views
urlpatterns = [
    path('qrDisplay/', views.qrDisplay, name = "qrDisplay"),
    path('resAfterLogin/',views.resAfterLogin, name="resAfterLogin"),
    path('resAfterLogin/resQrDisplay',views.resQrDisplay, name="resQrDisplay"),
    path('resAfterLogin/resRequestedVisit',views.resRequestedVisit,name="resRequestedVisit"),
    path('visAfterLogin/',views.visAfterLogin,name="visAfterLogin"),
    path('visAfterLogin/visitForm',views.visitForm, name="visitForm"),
    path('visAfterLogin/visPermittedVisit',views.visPermittedVisit, name="visPermittedVisit"),
    path('visAfterLogin/visQrDisplay', views.visQrDisplay,name="visQrDisplay"),
]