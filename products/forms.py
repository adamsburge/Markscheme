from django import forms
from .models import Workshop, DigitalProduct, Category
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput
from django.contrib.auth.models import User


class CustomMMCF(forms.ModelMultipleChoiceField):
    def label_from_instance(self, User):
        return User.first_name + ' ' + User.last_name


class WorkshopForm(forms.ModelForm):
    date = forms.DateField(label="Date of Workshop ", widget=DatePickerInput())
    time = forms.TimeField(label="Time of Workshop ", widget=TimePickerInput())
    image = forms.ImageField(label="Cover Photo for Workshop Page ")
    name = forms.CharField(label="Name of Workshop ")
    category = forms.ModelChoiceField(
        queryset=Category.objects.filter(name__startswith='w'),
        initial=Category.objects.filter(name__startswith='w').id
    )
    host_creators = CustomMMCF(
        queryset=User.objects.filter(is_superuser=True),
        widget=forms.CheckboxSelectMultiple,
        label="Workshop Instructors "
    )

    class Meta:
        model = Workshop
        fields = ('name', 'description', 'category', 'host_creators', 'date',
                  'time', 'location', 'total_slots', 'price', 'image', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class DigitalProductForm(forms.ModelForm):
    image = forms.ImageField(label="Cover Photo for Digital Product Page ")
    name = forms.CharField(label="Name of Digital Product ")
    pages = forms.IntegerField(label="Page Count ")
    price = forms.DecimalField(label="Price ")
    file = forms.FileField(label="Upload Digital Product File ")
    host_creators = CustomMMCF(
        queryset=User.objects.filter(is_superuser=True),
        widget=forms.CheckboxSelectMultiple,
        label="Creators of the Digital Product "
    )

    class Meta:
        model = DigitalProduct
        fields = ('name', 'description', 'pages', 'host_creators', 'price', 'image', 'file', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
