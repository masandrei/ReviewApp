from django.db import models

class User(models.Model):
    username = models.CharField(max_length = 255, unique = True)
    email = models.EmailField(max_length = 255, unique = True)
    password_hash = models.CharField(max_length = 255)
    password_salt = models.CharField(max_length = 255)

    def __str__(self):
        return self.username

class Phone(models.Model):
    manufacturer = models.CharField(max_length = 255)
    phone_model = models.CharField(max_length = 255)
    average_rating = models.DecimalField(max_digits = 3, decimal_places = 2, null = True, blank = True)
    year_of_presentation = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields = ["manufacturer", "phone_model"],
                name = "unique_phone_contraint"
            )
        ]
    
    def __str__(self):
        return f"{self.manufacturer} {self.phone_model}"

class Review(models.Model):
    username = models.ForeignKey(User, on_delete = models.CASCADE)
    phone = models.ForeignKey(Phone,  on_delete = models.CASCADE)
    general_descritption = models.CharField(max_length = 300)
    positive_summary = models.CharField(max_length = 40)
    negative_summary = models.CharField(max_length = 40)
    rating = models.IntegerField()
    created_at = models.DateField(auto_now_add = True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields = ["username", "phone"],
                name = "unique_review_constraint"
            )
        ]
