# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-10-25 01:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dinner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('primary_food_group', models.CharField(choices=[('meat', 'meat'), ('grain', 'grain'), ('vegetable', 'vegetable'), ('fruit', 'fruit'), ('dairy', 'dairy')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='DishOpinion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approval', models.CharField(choices=[('like', 'like'), ('dislike', 'dislike'), ('meh', 'meh')], max_length=20)),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opinions', to='dinner.Dish')),
            ],
        ),
        migrations.CreateModel(
            name='Eater',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RestaurantOpinion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approval', models.CharField(choices=[('like', 'like'), ('dislike', 'dislike'), ('meh', 'meh')], max_length=20)),
                ('eater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restaurantopinions', to='dinner.Eater')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opinions', to='dinner.Restaurant')),
            ],
        ),
        migrations.AddField(
            model_name='dishopinion',
            name='eater',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dishopinions', to='dinner.Eater'),
        ),
        migrations.AddField(
            model_name='dish',
            name='ingredients',
            field=models.ManyToManyField(to='dinner.Ingredient'),
        ),
        migrations.AddField(
            model_name='dinner',
            name='dishes',
            field=models.ManyToManyField(to='dinner.Dish'),
        ),
    ]