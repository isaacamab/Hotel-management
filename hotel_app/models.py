from django.db import models
class Room(models.Model):
    """
    Represents a room in the hotel.
    """
    room_number = models.CharField(max_length=5, unique=True)
    room_type = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=[
        ('available', 'Available'),
        ('occupied', 'Occupied'),
        ('maintenance', 'Under Maintenance')
    ])
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Room {self.room_number} - {self.room_type} - {self.status}"

class Guest(models.Model):
    """
    Represents a guest staying at the hotel.
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Reservation(models.Model):
    """
    Represents a reservation for a room in the hotel.
    """
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()

    def __str__(self):
        return f"Reservation for {self.guest} in room {self.room.room_number} from {self.check_in_date} to {self.check_out_date}"

class Staff(models.Model):
    """
    Represents a staff member at the hotel.
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.role})"

class Billing(models.Model):
    """
    Represents billing information for a reservation.
    """
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=20, choices=[
        ('paid', 'Paid'),
        ('unpaid', 'Unpaid')
    ])

    def __str__(self):
        return f"Billing for reservation {self.reservation}: {self.amount} ({self.payment_status})"
