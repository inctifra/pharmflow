from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.db.models import Sum
from django.urls import reverse
from django.utils.text import slugify
from datetime import date
class Drug(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    slug = models.SlugField(max_length=300, blank=True)
    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default="0.00"
    )

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("drug_detail", kwargs={"slug": self.slug, "pk": self.pk})
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    def stocks(self):
        return Stock.objects.filter(drug=self)


class Stock(models.Model):
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE)
    batch_number = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    expiry_date = models.DateField()
    added_on_date = models.DateTimeField(auto_now_add=True)
    def days_until_expiry(self):
        today = date.today()
        return (self.expiry_date - today).days
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['drug', 'batch_number'],
                name='unique_batch_per_drug'
            )
        ]
        ordering = ['expiry_date']

    def __str__(self):
        return f"{self.drug.name} - Batch {self.batch_number}"

    @property
    def is_expired(self):
        return self.expiry_date < timezone.now().date()
    @property
    def total_dispensed(self):
        return self.dispensations.aggregate(total=Sum('quantity'))['total'] or 0

class Dispensed(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name="dispensations")
    quantity = models.PositiveIntegerField()
    recipient = models.CharField(max_length=255)
    dispensed_by = models.CharField(max_length=100)
    dispensed_on = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-dispensed_on']

    def __str__(self):
        return f"{self.quantity} of {self.stock.drug.name} dispensed to {self.recipient}"

    def save(self, *args, **kwargs):
        if self._state.adding:
            if self.quantity > self.stock.quantity:
                raise ValidationError("Not enough stock available to dispense.")
            self.stock.quantity -= self.quantity
            self.stock.save()
        super().save(*args, **kwargs)

