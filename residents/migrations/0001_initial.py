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
                ('image_url', models.CharField(max_length=100, editable=True, required=False)),
                ('show_frequency', models.CharField(max_length=100, editable=True, required=False)),
                ('mix_url_one', models.CharField(max_length=100, editable=True, required=False)),
                ('mix_url_two', models.CharField(max_length=100, editable=True, required=False)),
                ('mix_url_three', models.CharField(max_length=100, editable=True, required=False)),
                ('soundcloud_url', models.CharField(max_length=100, editable=True, required=False)),
                ('mixcloud_url', models.CharField(max_length=100, editable=True, required=False)),
                ('facebook_url', models.CharField(max_length=100, editable=True, required=False)),
                ('twitter_url', models.CharField(max_length=100, editable=True, required=False)),
                ('instagram_url', models.CharField(max_length=100, editable=True, required=False)),
                ('bandcamp_url', models.CharField(max_length=100, editable=True, required=False)),
                ('youtube_url', models.CharField(max_length=100, editable=True, required=False)),
            ],
        ),
    ]