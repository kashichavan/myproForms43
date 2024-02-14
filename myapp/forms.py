from django import forms

gender_choice=[
    ('male','MALE'),
    ('female','FEMALE'),
    ('others','OTHERS'),
]

class RegisterForm(forms.Form):
    fName=forms.CharField(max_length=30,label="Enter Your Name",required=True,initial='Ex :Steven')
    lName=forms.CharField(max_length=30,label='Enter The Last Name',required=True,initial='Ex :Smith')
    age=forms.IntegerField(min_value=18,max_value=35,label="Enter the Age",initial="Ex : 25")
    email=forms.EmailField(label="Enter the Email ", initial="Ex : steevSmith49@gmail.com")
    gender=forms.ChoiceField(choices=gender_choice)


