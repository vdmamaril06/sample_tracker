from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Meal
from django.urls import reverse_lazy
from .forms import MealForm

# Create your views here.
def index(request):
	if request.user.is_authenticated:
		template = 'list.html'
		meals = Meal.objects.all()
		context = {
			'meals': meals,
		}
		return render(request, template, context)
	else:
		return HttpResponseRedirect(reverse_lazy('auth_login'))

def add_meal(request):
	if request.user.is_authenticated:
		template = "add_meal.html"

		if request.method == "POST":
			form = MealForm(request.POST)
			if form.is_valid():
				form.save()
			return HttpResponseRedirect(reverse_lazy('food:index'))
		else:
			context = {
				'meal_form': MealForm(),
			}
			return render(request, template, context)
	else:
		return HttpResponseRedirect(reverse_lazy('auth_login'))

def delete_meal(request, meal_id):
	if request.user.is_authenticated:
		meal = Meal.objects.get(id=int(meal_id))
		meal.delete()
		return HttpResponseRedirect(reverse_lazy('food:index'))
	else:
		return HttpResponseRedirect(reverse_lazy('auth_login'))

def update_meal(request, meal_id):
	if request.user.is_authenticated:
		template = "update_meal.html"
		meal = Meal.objects.get(id=int(meal_id))

		if request.method == "POST":
			form = MealForm(request.POST, instance=meal)
			if form.is_valid():
				form.save()
			return HttpResponseRedirect(reverse_lazy('food:index'))
		else:
			context = {
				'meal_form': MealForm(instance=meal),
			}
			return render(request, template, context)
	else:
		return HttpResponseRedirect(reverse_lazy('auth_login'))

def login(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect(reverse_lazy('food:index'))
	else:
		return HttpResponseRedirect(reverse_lazy('auth_login'))


