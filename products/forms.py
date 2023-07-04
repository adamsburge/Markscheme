from django import forms
from django.shortcuts import get_object_or_404
from .models import Workshop, DigitalProduct, Category, Updates, Product
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
        initial=Category.objects.get(name__startswith='w').id,
        # The below hidden input for some reason keeps failing to
        # actually fill the input when it is hidden. Consequently,
        # it is disabled for now
        # widget=forms.HiddenInput()
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
    category = forms.ModelChoiceField(
        queryset=Category.objects.filter(name__startswith='d'),
        initial=Category.objects.get(name__startswith='d').id,
    )
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


class ProductNewsUpdateForm(forms.ModelForm):
    subject = forms.CharField(label="Subject Line for Update: ")
    update_description = forms.CharField(widget=forms.Textarea, label="Extended Description for update: ")
    major_update = forms.CharField(initial=False, required=False, widget=forms.CheckboxInput(), label="Will this update affect those who have purchased this product? <br> <br>Note: if this box is checked, those who have purchased this product will be able to see this update.")

    class Meta:
        model = Updates
        fields = ('subject', 'update_description', 'product', 'major_update')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
