from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('ahput', '0003_add_short_feed_description_to_blog_page'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='blogpage',
            managers=[
                ('extra', django.db.models.manager.Manager()),
            ],
        ),
    ]