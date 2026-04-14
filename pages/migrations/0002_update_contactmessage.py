from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmessage',
            name='inquiry_type',
            field=models.CharField(
                max_length=20,
                choices=[
                    ('freelance', 'Freelance Project'),
                    ('fulltime',  'Full-Time Opportunity'),
                    ('collab',    'Collaboration'),
                    ('ministry',  'Ministry / Non-Profit'),
                    ('general',   'General Question'),
                ],
                default='general',
            ),
        ),
        migrations.AddField(
            model_name='contactmessage',
            name='budget',
            field=models.CharField(max_length=20, blank=True, default=''),
        ),
        migrations.AddField(
            model_name='contactmessage',
            name='timeline',
            field=models.CharField(max_length=20, blank=True, default=''),
        ),
        migrations.AddField(
            model_name='contactmessage',
            name='heard_from',
            field=models.CharField(max_length=20, blank=True, default=''),
        ),
    ]
