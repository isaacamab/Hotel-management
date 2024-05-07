from django.contrib import admin
from django.urls import path
from hotel_app import views

urlpatterns = [
    # URL pattern for the Django admin site
    path('admin/', admin.site.urls),
    
    # URL pattern for the dashboard page
    path('dashboard/', views.dashboard_view, name='dashboard'),
    
    # URL pattern for rooms page
    path('rooms/', views.rooms_page, name='rooms_page'),
    
    # URL pattern for guests page
    path('guests/', views.guests_page, name='guests_page'),
    
    # URL pattern for reservations page
    path('reservations/', views.reservations_page, name='reservations_page'),
    
    # URL pattern for billing page
    path('billing/', views.billing_page, name='billing_page'),
    
    # URL pattern for staff page
    path('staff/', views.staff_page, name='staff_page'),
    
    # URL pattern for settings page
    path('settings/', views.settings_page, name='settings_page'),
    
    # URL pattern for signup page
    path('signup/', views.signup_page, name='signup'),
    
    # URL pattern for login page
    path('login/', views.login_page, name='login'),
    
    # URL pattern for logout page
    path('logout/', views.logout_page, name='logout'),
    
    # URL pattern for reserving a room
    path('reserve/<int:room_id>/', views.reserve_room, name='reserve_room'),
]
