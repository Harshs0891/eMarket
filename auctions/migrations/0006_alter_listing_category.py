# Generated by Django 4.2.1 on 2023-07-27 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_alter_listing_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(blank=True, choices=[('EnG', 'Electronics & Gadgets'), ('FnA', 'Fashion & Apparel'), ('HnL', 'Home & Living'), ('BnP', 'Beauty & Personal Care'), ('SnF', 'Sports & Fitness'), ('BnS', 'Books & Stationery'), ('TnG', 'Toys & Games'), ('HnW', 'Health & Wellness'), ('KnD', 'Kitchen & Dining'), ('JnA', 'Jewelry & Accessories')], max_length=3),
        ),
    ]
