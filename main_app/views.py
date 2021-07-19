from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Food
from .forms import ReviewForm


# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def foods_index(request):
  foods = Food.objects.all()
  return render(request, 'foods/index.html', { 'foods': foods  })

def foods_detail(request, food_id):
  food = Food.objects.get(id=food_id)
  review_form = ReviewForm()
  return render(request, 'foods/detail.html', { 
    'food' :food,
    'review_form' : review_form 
    })

def add_review(request, food_id):
  form = ReviewForm(request.POST)
  if form.is_valid():
    new_review = form.save(commit=False)
    new_review.food_id = food_id
    new_review.save()
  return redirect('detail', food_id=food_id)

class FoodCreate(CreateView):
  model = Food
  fields = '__all__'

class FoodUpdate(UpdateView):
  model = Food
  fields = '__all__'

class FoodDelete(DeleteView):
  model = Food
  success_url = '/foods/'

