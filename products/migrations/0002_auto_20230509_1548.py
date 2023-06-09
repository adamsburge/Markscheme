# Generated by Django 3.2.18 on 2023-05-09 15:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DigitalProduct',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='products.product')),
                ('file', models.FileField(upload_to='media/student_resources/')),
                ('pages', models.IntegerField()),
                ('owners', models.ManyToManyField(blank=True, related_name='resource_owners', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('products.product',),
        ),
        migrations.DeleteModel(
            name='StudentResource',
        ),
    ]
