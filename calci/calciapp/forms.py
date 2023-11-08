from django import forms 

class Fields(forms.Form):
    Choices=(('Add','Add(Addition)'),('Sub','Sub(Substraction)'),('Mul','Mul(Multiplication)'),('Div','Div(Division)'))
    num1=forms.IntegerField()
    num2=forms.IntegerField()
    operation=forms.ChoiceField(choices=Choices)
    
    
    