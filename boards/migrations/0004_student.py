# Generated by Django 2.2 on 2019-07-02 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('std_id', models.CharField(max_length=7, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('attendance', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('ct1', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('ct2', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('ct3', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('ct4', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('ct', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('secA', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('secB', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('final300', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('final100', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('gpa', models.DecimalField(decimal_places=2, max_digits=5)),
                ('grade', models.CharField(max_length=2)),
            ],
        ),
    ]
