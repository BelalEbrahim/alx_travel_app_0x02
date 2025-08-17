from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Listing(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)]
    )

    def __str__(self):
        return self.title


class Booking(models.Model):
    listing = models.ForeignKey(
        Listing, on_delete=models.CASCADE, related_name="bookings"
    )
    user = models.CharField(max_length=50)
    booking_date = models.DateField()

    def __str__(self):
        return f"{self.user} Booking for {self.listing.title}"


class Review(models.Model):
    listing = models.ForeignKey(
        Listing, on_delete=models.CASCADE, related_name="reviews"
    )
    user = models.CharField(max_length=50)
    comment = models.TextField()
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    def __str__(self):
        return f"{self.user} Review for {self.listing.title} ({self.rating}/5)"


class Payment(models.Model):
    STATUS_PENDING = "pending"
    STATUS_COMPLETED = "completed"
    STATUS_FAILED = "failed"

    STATUS_CHOICES = [
        (STATUS_PENDING, "Pending"),
        (STATUS_COMPLETED, "Completed"),
        (STATUS_FAILED, "Failed"),
    ]

    booking = models.ForeignKey(
        Booking, on_delete=models.CASCADE, related_name="payments"
    )
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)]
    )
    tx_ref = models.CharField(max_length=100, unique=True)
    checkout_url = models.URLField(blank=True, null=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment {self.tx_ref} - {self.status}"
