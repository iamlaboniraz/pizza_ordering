from django.shortcuts import render
from .forms import PizzaForm,MultiplePizzaForm
from django.forms import formset_factory
from .models import Pizza
def home(request):
	return render(request,'pizza/home.html')
def order(request):
	Multiple_form=MultiplePizzaForm()
	if request.method=='POST':
		filled_form=PizzaForm(request.POST)
		if filled_form.is_valid():
			created_pizza = filled_form.save()
			created_pizza_pk = created_pizza.id
			note='Thanks for ordering!! Your %s %s and %s pizza is on the way!!'%(filled_form.cleaned_data['size'],
			filled_form.cleaned_data['topping1'],
			filled_form.cleaned_data['topping2'])
			filled_form=PizzaForm()
		else:
			created_pizza_pk=None
			note="Pizza order has failed.Try again!!"
		return render(request,'pizza/order.html',{'created_pizza_pk':created_pizza_pk,'PizzaForm':filled_form,'note':note,'Multiple_form':Multiple_form})

	else:
		form=PizzaForm()
		return render(request,'pizza/order.html',{'PizzaForm':form,'Multiple_form':Multiple_form})

def pizzas(request):
	number_of_pizzas=2
	filled_multiple_pizza_form=MultiplePizzaForm(request.GET)
	if filled_multiple_pizza_form.is_valid():
		number_of_pizzas=filled_multiple_pizza_form.cleaned_data["number"]
	pizzaFormSet=formset_factory(PizzaForm,extra=number_of_pizzas)
	formSet=pizzaFormSet()
	if request.method=='POST':
		filled_formset=pizzaFormSet(request.POST)
		if filled_formset.is_valid():
			for form in filled_formset:
				print(form.cleaned_data['topping1'])
			note='pizza has been Ordered'
		else:
			note='Order was not created!! Try again!!'
		return render(request,'pizza/pizzas.html',{'note':note,'formSet':formSet})
	else:
		return render(request,'pizza/pizzas.html',{'formSet':formSet})

def edit_order(request,pk):
	pizza = Pizza.objects.get(pk=pk)
	form=PizzaForm(instance=pizza)
	if request.method=='POST':
		filled_form=PizzaForm(request.POST,instance=pizza)
		if filled_form.is_valid():
			filled_form.save()
			form=filled_form
			note='order has been updated'
			return render(request,'pizza/edit_order.html',{'pizza':pizza,'form':form,'note':note})
	return render(request,'pizza/edit_order.html',{'pizza':pizza,'form':form,})