from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.views.generic.edit import CreateView, FormView

from apps.carshop.forms import RegistrationForm, LoginForm

from apps.carshop.models import Car


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')


class RegistrationView(CreateView):
    form_class = RegistrationForm
    template_name = "registration.html"
    success_url = "/"

    def form_valid(self, form):
        user = form.save()
        user.set_password(user.password)
        user.save()
        return super(RegistrationView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegistrationView, self).form_invalid(form)


class LoginView(FormView):
    form_class = LoginForm
    template_name = "landing.html"
    success_url = "/landing"

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            return HttpResponseRedirect(self.get_success_url())
        else:
            form.errors['username'] = form.error_class(
                ["Invalid username or password"])
            return self.form_invalid(form)

    def form_invalid(self, form):
        valid = form.is_valid()
        return super(LoginView, self).form_invalid(form)


class LandingView(ListView):
    template_name = "landing.html"
    model = Car

    def get_queryset(self):
        return super(LandingView, self).get_queryset()


    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LandingView, self).dispatch(*args, **kwargs)


class CheckoutView(ListView):
    template_name = "checkout.html"
    model = Car

    def get(self, request, *args, **kwargs):
        id_list = []
        for key in request.GET.iterkeys():
            value = int(request.GET.get(key))
            if value != 0:
                id_list.append(key)

        cars_list = Car.objects.filter(id__in=id_list)
        new_cars_list = []
        for car in cars_list:
            car.quantity = int(request.GET.get(str(car.pk)))
            new_cars_list.append(car)
            car.price *= car.quantity
        self.object_list = new_cars_list

        return super(CheckoutView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return self.object_list

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CheckoutView, self).dispatch(*args, **kwargs)


class OrderConfirmationView(FormView):
    template_name = "landing.html"
    model = Car

    def post(self, request, *args, **kwargs):
        id_list = {}
        for key in request.POST.iterkeys():
            value = request.POST.get(key)
            if value == 'on':
                id_list[key] = request.POST.get(key+'-'+key)

        cars_list = Car.objects.filter(id__in=id_list.keys())
        for car in cars_list:
            key = str(car.pk)
            car.quantity -= int(request.POST.get(key + '-' + key))
            car.save()

        return  HttpResponseRedirect('/landing')


    def get_queryset(self):
        return self.object_list


    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(OrderConfirmationView, self).dispatch(*args, **kwargs)

