from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from cloudinary.models import CloudinaryField

TECHNIQUES = (
    ('sp', 'Screenprint'),
    ('mt', 'Monotype'),
    ('li', 'Lithography'),
    ('co', 'Collagraph'),
    ('dp', 'Drypoint'),
    ('at', 'Aquatint'),
    ('mt', 'Mezzotint'),
    ('et', 'Etching'),
    ('eg', 'Engraving'),
    ('pg', 'Photogravure'),
    ('lc', 'Linocut'),
    ('wc', 'Woodcut'),
    ('mk', 'Mokuhanga'),
    ('cb', 'Carborundum')
)

STATUS = (
    ('ip', 'In Progress'),
    ('c', 'Complete'),
    ('a', 'Archive')
)

EDITION_TYPE = (
    ('lmt', 'Limited'),
    ('op', 'Open'),
    ('va', 'Varied')

)

class Edition(models.Model):
    edition_name = models.CharField(max_length=200)
    image = CloudinaryField('image')
    year = models.PositiveIntegerField(validators=[MinValueValidator(1900)])
    edition_size = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    paper_size = models.CharField(max_length=100)
    plate_size = models.CharField(max_length=100)
    technique = models.CharField(choices=TECHNIQUES, default=TECHNIQUES[0][0])
    margin_upper = models.CharField(max_length=100)
    margin_lower = models.CharField(max_length=100)
    margin_sides = models.CharField(max_length=100)
    available_prints = models.CharField(max_length=50)
    status = models.CharField(choices=STATUS, default=STATUS[0][0])
    edition_type = models.CharField(choices=EDITION_TYPE, default=EDITION_TYPE[0][0])
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.edition_name
    def get_absolute_url(self):
        return reverse("edition_detail", kwargs={"pk": self.id})
    

class Note(models.Model):
    note_date = models.DateField()
    notes = models.TextField()
    edition = models.ForeignKey(Edition, on_delete=models.CASCADE)

    def __str__(self):
        return f'Note Date: {self.note_date}'
  
