# Generated by Django 4.2 on 2024-04-16 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse_platform', '0003_remove_report_item_remove_report_reported_by_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='image',
        ),
        migrations.AddField(
            model_name='item',
            name='area',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='item',
            name='camera_monitoring',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='contract_type',
            field=models.CharField(choices=[('weekly', 'Weekly'), ('monthly', 'Monthly'), ('yearly', 'Yearly')], default='monthly', max_length=20),
        ),
        migrations.AddField(
            model_name='item',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='thumbnails/'),
        ),
        migrations.AddField(
            model_name='item',
            name='warehouse_type',
            field=models.CharField(choices=[('industrial', 'Industrial'), ('personal', 'Personal'), ('food_products', 'Food Products'), ('online_sellers', 'Online Sellers Storage'), ('archiving', 'Archiving Storage')], default='Industrial', max_length=50),
        ),
        migrations.CreateModel(
            name='ItemImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='items/')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='warehouse_platform.item')),
            ],
        ),
    ]
