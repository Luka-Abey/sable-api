from django.db import migrations, models
from django.db.models.fields import TextField


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('banner', models.CharField(max_length=100)),
                ('chunk_one', models.TextField()),
                ('image_one', models.CharField(max_length=100, editable=True, blank=True)),
                ('chunk_two', models.TextField(editable=True, blank=True)),
                ('image_two', models.CharField(max_length=100, editable=True, blank=True)),
                ('chunk_three', models.TextField(editable=True, blank=True)),
                ('image_three', models.CharField(max_length=100, editable=True, blank=True)),
                ('chunk_four', models.TextField(editable=True, blank=True)),
                ('image_four', models.CharField(max_length=100, editable=True, blank=True)),
                ('chunk_five', models.TextField(editable=True, blank=True)),
                ('image_five', models.CharField(max_length=100, editable=True, blank=True)),
                ('chunk_six', models.TextField(editable=True, blank=True)),
                ('image_six', models.CharField(max_length=100, editable=True, blank=True)),
                ('author', models.CharField(max_length=100, editable=True, blank=True)),
                ('post_type', models.CharField(max_length=100, editable=True, blank=True)),
                ('date', models.CharField(max_length=100, editable=True, blank=True)),
            ],
        ),
    ]