from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.db.models import Sum
from .models import Room, Guest, Reservation, Staff, Billing
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


# Logout function
def logout_page(request):
    # Log the user out
    logout(request)
    # Redirect to login page
    return redirect('login')

# View function for the dashboard
@login_required
def dashboard_view(request):
    # Query data
    rooms = Room.objects.all()
    guests = Guest.objects.all()
    reservations = Reservation.objects.all()
    staff = Staff.objects.all()
    billing = Billing.objects.all()

    # Calculate total billing
    total_billing = billing.aggregate(total_amount=Sum('amount'))['total_amount']

    # Prepare context for template
    context = {
        'rooms': rooms,
        'guests': guests,
        'reservations': reservations,
        'staff': staff,
        'billing': billing,
        'total_billing': total_billing,
    }

    # Render the dashboard template
    return render(request, 'hotel_app/dashboard.html', context)

# View function for the rooms page
@login_required
def rooms_page(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'hotel_app/rooms.html', context)

# View function for the guests page
@login_required
def guests_page(request):
    guests = Guest.objects.all()
    context = {'guests': guests}
    return render(request, 'hotel_app/guests.html', context)

# View function for the reservations page
@login_required
def reservations_page(request):
    reservations = Reservation.objects.all()
    context = {'reservations': reservations}
    return render(request, 'hotel_app/reservations.html', context)

# View function for the billing page
@login_required
def billing_page(request):
    billing = Billing.objects.all()
    context = {'billing': billing, 'total_billing': billing.aggregate(total_amount=Sum('amount'))['total_amount']}
    return render(request, 'hotel_app/billing.html', context)

# View function for the staff page
@login_required
def staff_page(request):
    staff = Staff.objects.all()
    
    # Count the number of registered admins (staff with role 'admin')
    admin_count = Staff.objects.filter(role='admin').count()
    
    # Prepare context
    context = {
        'staff': staff,
        'admin_count': admin_count,
    }
    
    # Render the staff template
    return render(request, 'hotel_app/staff.html', context)


# View function for the settings page
@login_required
def settings_page(request):
    return render(request, 'hotel_app/settings.html')

# View function for the signup page
def signup_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page upon successful signup
        context = {'form': form}
    else:
        form = UserCreationForm()
        context = {'form': form}
    return render(request, 'hotel_app/signup.html', context)

# View function for the login page
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            context = {'error': 'Invalid username or password'}
            return render(request, 'hotel_app/login.html', context)
    else:
        return render(request, 'hotel_app/login.html')

# View function for reserving a room
@login_required
def reserve_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    
    if request.method == 'POST':
        # Retrieve date and time from POST data
        date = request.POST.get('date')
        time_of_day = request.POST.get('time')
        
        # Add reservation logic here (e.g., save reservation details to the database)
        
        # After successful reservation, redirect to the dashboard
        return redirect(reverse('dashboard'))
    
    # Handle unexpected request methods
    context = {
        'error': 'Reservation request failed. Please try again later.'
    }
    return render(request, 'reservation_failed.html', context)

@login_required
def billing_page(request):
    # Query all bills and prefetch reservation and guest data for efficiency
    billing = Billing.objects.select_related('reservation__guest')

    # Group bills by guest
    grouped_bills = {}
    for bill in billing:
        guest = bill.reservation.guest
        if guest not in grouped_bills:
            grouped_bills[guest] = []
        grouped_bills[guest].append(bill)

    # Prepare context
    context = {
        'grouped_bills': grouped_bills,
    }
    
    # Render the billing template
    return render(request, 'hotel_app/billing.html', context)