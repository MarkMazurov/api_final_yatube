# Generated by Django 2.2.16 on 2022-03-24 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20220323_1930'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='unique_following',
        ),
        migrations.RemoveConstraint(
            model_name='follow',
            name='prevent_self_following',
        ),
    ]
