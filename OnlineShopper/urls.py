from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from apps.carshop.views.rest_views import get_user_list, DealerListView, \
    DealerListDetailView, DealerListCreateView, CarListDetailView

from apps.carshop.views.user_view import RegistrationView, LoginView, \
    logout_user, LandingView, CheckoutView, OrderConfirmationView


admin.autodiscover()

router = DefaultRouter()
# router.register(r'dealers', DealersViewSet)
# router.register(r'cars', CarsViewSet)

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

    #router based viewsets
    url(r'^rest/', include(router.urls)),
    # function based view

    url(r'^rest/users/', get_user_list),
    url(r'^rest/dealerslist/', DealerListView.as_view()),
    url(r'^rest/dealersdetail/(?P<pk>[0-9]+)/', DealerListDetailView.as_view()),
    url(r'^rest/dealerscreatelist/(?P<pk>[0-9]+)/', DealerListCreateView.as_view()),
    url(r'^rest/carsdetail/(?P<pk>[0-9]+)/', CarListDetailView.as_view()),
    #authentication url for the rest apis
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^docs/', include('rest_framework_swagger.urls')),

)


