from django.db import models


# Create your models here.
class CarMake(models.TextChoices):
    PROTON = 'PRO', 'Proton'
    PERODUA = 'PER', 'Perodua'
    HONDA = 'HON', 'Honda'
    TOYOTA = 'TOY', 'Toyota'
    NISSAN = 'NIS', 'Nissan'
    MAZDA = 'MAZ', 'Mazda'
    BMW = 'BMW', 'BMW'
    MERCEDES = 'MER', 'Mercedes-Benz'
    AUDI = 'AUD', 'Audi'
    VOLKSWAGEN = 'VOL', 'Volkswagen'
    HYUNDAI = 'HYU', 'Hyundai'
    KIA = 'KIA', 'Kia'
    FORD = 'FOR', 'Ford'
    CHEVROLET = 'CHE', 'Chevrolet'
    SUBARU = 'SUB', 'Subaru'
    PORSCHE = 'POR', 'Porsche'
    LEXUS = 'LEX', 'Lexus'
    JAGUAR = 'JAG', 'Jaguar'
    LAND_ROVER = 'LR', 'Land Rover'
    MITSUBISHI = 'MIT', 'Mitsubishi'
    PEUGEOT = 'PEU', 'Peugeot'
    RENAULT = 'REN', 'Renault'
    SUZUKI = 'SUZ', 'Suzuki'


class Car(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('sold', 'Sold'),
        ('reserved', 'Reserved'),
        ('repairing', 'Repairing'),
    ]

    make = models.CharField(
        max_length=10,
        choices=CarMake.choices,
        blank=False
    )
    model = models.CharField(max_length=50, blank=False)
    year = models.PositiveIntegerField(blank=False)
    listing_price = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    sold_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Sold price of the car
    cost = models.DecimalField(max_digits=10, decimal_places=2)  # Cost of the car
    mileage = models.PositiveIntegerField(blank=False)
    color = models.CharField(max_length=30)
    plate_number = models.CharField(max_length=15, unique=True)  # Added plate_number field
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='available',
        blank=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True,  # Automatically set when an instance is created
        editable=False  # Do not allow editing this field
    )
    updated_at = models.DateTimeField(
        auto_now=True,  # Automatically update to the current timestamp on every save
        editable=False  # Do not allow editing this field
    )

    def __str__(self):
        return f'{self.year} {self.make} {self.model}'

class CarImage(models.Model):
    car = models.ForeignKey(Car, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='cars', default="", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Image for {self.car}'