from django.views.generic import TemplateView
from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from apps.carshop.views.rest_views import DealersViewSet, CarsViewSet

from apps.carshop.views.user_view import RegistrationView, LoginView, logout, \
    logout_user, LandingView, CheckoutView, OrderConfirmationView


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'OnlineShopper.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', LoginView.as_view(template_name="login.html"), name="login_page"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/', RegistrationView.as_view(), name="registration_page"),
    url(r'^landing/', LandingView.as_view(), name="landing_page"),
    url(r'^checkout/', CheckoutView.as_view(), name="checkout_page"),
    url(r'^confirmorder/', OrderConfirmationView.as_view(), name="order_confirmation_page"),
    url(r'^logout/', logout_user, name="logout_page"),

)

