from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, editable=True, blank=False)),
                ('image_url', models.CharField(max_length=150, editable=True, blank=False)),
                ('link_url', models.CharField(max_length=150, editable=True, blank=True)),
            ],
        ),
    ]