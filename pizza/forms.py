from django import forms
from .models import Pizza,Size
# class PizzaForm(forms.Form):
# 	toppings=forms.MultipleChoiceField(choices=[('Cheese','Cheese'),('Pepperoni','Pepperoni'),('olives','olives')],widget=forms.CheckboxSelectMultiple)
# 	#toppings=forms.MultipleChoiceField(choices=[('Cheese','Cheese'),('Pepperoni','Pepperoni'),('olives','olives')])
# 	#tipping1=forms.CharField(label="tipping1",max_length=100,widget=forms.PasswordInput)
# 	#tipping2=forms.CharField(label="tipping2",max_length=100)
# 	size=forms.ChoiceField(label="size",choices=[('Small','Small'),('Medium','Medium'),('Large','Large')])

class PizzaForm(forms.ModelForm):
	#image=forms.ImageField()
	#siza=forms.ModelChoiceField(queryset=Size.objects,empty_label=None,widget=forms.CheckboxSelectMultiple)
	class Meta:
		model = Pizza
		fields = ['topping1','topping2','size']
		labels={'topping1':'Topping 1','topping2':'Topping 2'} 
		#widgets={'size':forms.CheckboxSelectMultiple} 
class MultiplePizzaForm(forms.Form):
	number=forms.IntegerField(min_value=2,max_value=10)
