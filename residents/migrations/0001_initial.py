from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resident',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('image_url', models.CharField(max_length=100, editable=True)),
                ('show_frequency', models.CharField(max_length=100, editable=True)),
                ('mix_url_one', models.CharField(max_length=100, editable=True)),
                ('mix_url_two', models.CharField(max_length=100, editable=True)),
                ('mix_url_three', models.CharField(max_length=100, editable=True)),
                ('soundcloud_url', models.CharField(max_length=100, editable=True)),
                ('mixcloud_url', models.CharField(max_length=100, editable=True)),
                ('facebook_url', models.CharField(max_length=100, editable=True)),
                ('twitter_url', models.CharField(max_length=100, editable=True)),
                ('instagram_url', models.CharField(max_length=100, editable=True)),
                ('bandcamp_url', models.CharField(max_length=100, editable=True)),
                ('youtube_url', models.CharField(max_length=100, editable=True)),
            ],
        ),
    ]