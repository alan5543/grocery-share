# Generated by Django 4.2.20 on 2025-04-09 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_shoppinglistitem_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shoppinglist',
            options={'ordering': ['position', 'created_at']},
        ),
        migrations.AddField(
            model_name='shoppinglist',
            name='position',
            field=models.IntegerField(default=0),
        ),
    ]
