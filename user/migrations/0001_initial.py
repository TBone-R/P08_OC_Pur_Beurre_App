# Generated by Django 3.1.1 on 2020-09-22 09:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_by_1', models.CharField(choices=[('name', 'name'), ('nova', 'nova'), ('nutri_score', 'nutri_score'), ('label_score', 'label_score')], default='name', max_length=11)),
                ('order_by_2', models.CharField(choices=[('name', 'name'), ('nova', 'nova'), ('nutri_score', 'nutri_score'), ('label_score', 'label_score')], default='nova', max_length=11)),
                ('order_by_3', models.CharField(choices=[('name', 'name'), ('nova', 'nova'), ('nutri_score', 'nutri_score'), ('label_score', 'label_score')], default='nutri_score', max_length=11)),
                ('order_by_4', models.CharField(choices=[('name', 'name'), ('nova', 'nova'), ('nutri_score', 'nutri_score'), ('label_score', 'label_score')], default='label_score', max_length=11)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SavedSubstitute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='originals', to='product.product')),
                ('substitute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='substitutes', to='product.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
