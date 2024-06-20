from django.db import models

class MusicianModel(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    choice = (
        ('Grid', 'Grid'),
        ('Flute', 'Flute'),
        ('Piano', 'Piano'),
        ('Trumpet', 'Trumpet'),
        ('Banjo', 'Banjo'),
    )
    instrument_type = models.CharField(max_length=10, choices=choice, default='Grid')

    def __str__(self):
        return f"{self.first_name}"