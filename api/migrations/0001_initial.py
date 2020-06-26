# Generated by Django 3.0 on 2020-03-10 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Programmer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick', models.CharField(max_length=16)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('program_lang', models.CharField(choices=[('python', 'Python'), ('c', 'C'), ('java', 'Java'), ('php', 'PHP')], max_length=32)),
            ],
        ),
    ]
