from django.db import models


class ContactMessage(models.Model):

    INQUIRY_CHOICES = [
        ('freelance',  'Project Inquiry'),
        ('fulltime',   'Job Opportunity'),
        ('collab',     'Collaboration'),
        ('ministry',   'Ministry / Non-Profit'),
        ('general',    'General Question'),
    ]

    BUDGET_CHOICES = [
        ('',           'Select a range (optional)'),
        ('under500',   'Under $500'),
        ('500_2k',     '$500 – $2,000'),
        ('2k_5k',      '$2,000 – $5,000'),
        ('5k_plus',    '$5,000+'),
        ('discuss',    'Let\'s Discuss'),
    ]

    TIMELINE_CHOICES = [
        ('',          'Select a timeline (optional)'),
        ('asap',      'ASAP'),
        ('1month',    'Within 1 Month'),
        ('3months',   'Within 3 Months'),
        ('flexible',  'Flexible'),
    ]

    HEARD_CHOICES = [
        ('',               'Select an option'),
        ('business_card',  'Business Card'),
        ('facebook',       'Facebook'),
        ('instagram',      'Instagram'),
        ('linkedin',       'LinkedIn'),
        ('church',         'Church'),
        ('conference',     'Conference'),
        ('referral',       'Referral'),
        ('friend',         'Friend'),
        ('coach',          'Coach'),
        ('other',          'Other'),
    ]

    name         = models.CharField(max_length=100)
    email        = models.EmailField()
    inquiry_type = models.CharField(max_length=20, choices=INQUIRY_CHOICES, default='general')
    subject      = models.CharField(max_length=200)
    budget       = models.CharField(max_length=20, choices=BUDGET_CHOICES, blank=True, default='')
    timeline     = models.CharField(max_length=20, choices=TIMELINE_CHOICES, blank=True, default='')
    message      = models.TextField()
    heard_from   = models.CharField(max_length=20, choices=HEARD_CHOICES, blank=True, default='')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} — {self.get_inquiry_type_display()} — {self.subject}'

    class Meta:
        ordering = ['-submitted_at']
