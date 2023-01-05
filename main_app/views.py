from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth import logout
# from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .models import Restaurant, Favorite, Review
from .forms import UpdateUserForm, UpdateRestaurantForm, ReviewForm
# from .form import FeedingForm
from django import forms
from django.views.generic import ListView
from django import http
from django.db.models import Avg

# Create your views here.

### Home views ###


def front(request):
    return render(request, 'front.html')


def home(request):
    return render(request, 'home.html')
    # return HttpResponse('<h1>Hello</h1>')


def about(request):
    return render(request, 'about.html')

### Restaurants views ###


def all_restaurants_index(request):
    # restaurants = Restaurant.objects.all()
    restaurants = Restaurant.objects.filter(published=True).order_by('id')
    context = {"restaurants": restaurants, "public_page": True}
    return render(request, 'restaurants/index.html', context)


def all_restaurants_detail(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    # print(restaurant)
    context = {"restaurant": restaurant, "public_page": True}
    review_form = ReviewForm()
    return render(request, 'main_app/restaurant_detail.html', context)


@login_required
def restaurants_index(request):
    restaurants = Restaurant.objects.filter(user=request.user).order_by('id')
    # You could also retrieve the logged in user's restaurants like this
    # restaurants = request.user.restaurant_set.all()
    context = {"restaurants": restaurants, "public_page": False}
    return render(request, 'restaurants/index.html', context)


class RestaurantDetail(LoginRequiredMixin, DetailView):
    model = Restaurant
    fields = '__all__'


@login_required
def restaurant_create(request):
    restaurant_form = UpdateRestaurantForm(request.POST)
    if request.method == 'POST':
        if restaurant_form.is_valid():
            # don't save the form to the db until it
            # has the user_id assigned
            new_restaurant = restaurant_form.save(commit=False)
            new_restaurant.user_id = request.user.id
            restaurant_form.save()  # save the valid form instance to the database
            return redirect(to='restaurants_detail', pk=new_restaurant.id)
    else:
        restaurant_form = UpdateRestaurantForm()

    return render(request, 'restaurants/restaurant_form.html', {'restaurant_form': restaurant_form})


@login_required
def restaurant_update(request, restaurant_id):
    # Get the restaurant instance with id = restaurant_id
    restaurant = Restaurant.objects.get(id=restaurant_id)

    # Process the form data if it is a POST request
    if request.method == 'POST':

        # Create form instance for the restaurant instance
        restaurant_form = UpdateRestaurantForm(
            request.POST, instance=restaurant)

        # Check if the form instance is valid
        if restaurant_form.is_valid():
            restaurant_form.save()  # save the valid form instance to the database
            return redirect(to='restaurants_detail', pk=restaurant.id)
    else:
        # Get the form instance for the restaurant instance if it is not a POST request
        # (e.g. it is a GET request)
        restaurant_form = UpdateRestaurantForm(instance=restaurant)
        # print(restaurant_form)

    return render(request, 'restaurants/restaurant_form.html', {
        'restaurant': restaurant,
        'restaurant_form': restaurant_form
    })


class RestaurantDelete(LoginRequiredMixin, DeleteView):
    model = Restaurant
    success_url = '/restaurants/'

### Registration views ###


def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' from object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('restaurants_index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

### User views ###


@login_required
def user_profile(request):
    return render(request, 'users/profile.html')


@login_required
def user_update(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            # message.success(request, 'Your profile is updated successfully')
            return redirect(to='user_profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        print(user_form)
    return render(request, 'users/update.html', {
        'user_form': user_form
    })


class ChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'users/change_password.html'
    # success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('pwd_change_done')


@login_required
def pwd_change_done(request):
    return render(request, 'users/password_change_done.html')


@login_required
def user_delete_confirm(request):
    if request.method == 'POST':
        try:
            u = User.objects.get(username=request.user.username)
            u.delete()
            logout(request)
            # message.success(request, "The user is deleted")

        except User.DoesNotExist:
            # message.error(request, "User does not exist")
            return render(request, 'front.html')

        except Exception as e:
            return render(request, 'front.html', {'err': e.message})

        return render(request, 'front.html')

    return render(request, 'users/user_delete_confirm.html')

### Testing views ###


def testing(request):
    return render(request, 'testing.html')


class ListFavorites(LoginRequiredMixin, ListView):
    model = Favorite


class CreateView(LoginRequiredMixin, CreateView):
    model = Favorite
    fields = ['title']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    success_url = '/favorites/'


class FavoriteDelete(LoginRequiredMixin, DeleteView):
    model = Favorite
    fields = '__all__'
    success_url = '/favorites/'

    def delete(self, request, *args, **kwargs):

        self.object = self.get_object()
        if self.object.User == request.user:
            success_url = self.get_success_url()
            self.object.delete()
            return http.HttpResponseRedirect(success_url)
        else:
            return http.HttpResponseForbidden("Cannot delete other's posts")
# ok we
# def favorite_delete(request, favorite_pk):
#     if request.method == 'POST':
#         u = User.objects.get(id=request.user.id)
#         if u == favorite_pk:
#             u.delete()
#             # return render(request, 'main_app/favorite_confirm_delete/')


class UpdateFavorite(LoginRequiredMixin,  UpdateView):
    model = Favorite
    fields = ["title"]
    success_url = '/favorites/'


def detail_favorites(request, favorite_id):
    each = Favorite.objects.get(id=favorite_id)
    return render(request, 'favourites/detail.html', {'each': each})


### Review views ###

@login_required
def add_review(request, restaurant_id):
    url = request.META.get('HTTP_REFERER')
    form = ReviewForm(request.POST)
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.restaurant_id = restaurant_id
        new_review.user_id = request.user.id
        new_review.save()
    return redirect(url, restaurant_id=restaurant_id)


@login_required
def delete_review(request, restaurant_id, review_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == "POST":
        # delete_review = Review.objects.get()
        delete_review = Review.objects.filter(id=review_id)
        delete_review.delete()
    return redirect(url, restaurant_id=restaurant_id)


def detail_review(request):
    # _avg = Restaurant.objects.aggregate(avg=Avg('rating'))
    _avg = Review.objects.aggregate(avg=Avg('rating'))
    return render(request, 'main_app/restaurant_detail.html', {"avg": _avg})
