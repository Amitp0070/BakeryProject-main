from django.shortcuts import render, redirect
from .models import Product, MenuItem, Order, Category, ContactForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .forms import BookingForm



def home(request):
    return render(request, 'bakery/home.html')

def menu(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'menu.html', {'products': products, 'categoryies': categories})

def order(request):
    if request.method == 'POST':
        produc_id = request.POST.get('menu_item_id')
        quantity = int(request.POST.get('quantity', 0))
        customer_name = request.POST.get('customer_name')
        customer_email = request.POST.get('customer_email')
        customer_phone = request.POST.get('customer_phone')

        menu_item = MenuItem.objects.get(pk=produc_id)
        order = Order.objects.create(
            menu_item=menu_item,
            quantity=quantity,
            customer_name=customer_name,
            customer_email=customer_email,
            customer_phone=customer_phone
        )
        return redirect('order_confirm', order_id=order.pk)
    else:
        menu_items = MenuItem.objects.all()
        return render(request, 'order.html', {'menu_items': menu_items})
    
def order_confirm(request, order_id):
    order = Order.objects.get(pk=order_id)
    return render(request, 'home.html', {'order': order})

def about(request):
    return render(request, 'bakery/about.html')


def contact(request):
    if request.method == 'POST':
        # Process form submission
        # You can access form data using request.POST
        # For example:
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save the form data to the database or perform any other necessary actions

        # Example of saving the form data to a ContactForm model
        ContactForm.objects.create(name=name, email=email, message=message)

        # Display a success message
        messages.success(request, 'Your message has been sent successfully!')
        
        # Redirect to the contact page again or to a thank you page
        return redirect('contact')

    # If the request method is GET, render the contact page template
    return render(request, 'contact.html')

def submit_contact(request):
    if request.method == 'POST':
        # Process the form data
        # Example: Saving the form data to the database
        
        # Redirect to a success page
        return HttpResponseRedirect(reverse('home'))
    else:
        # Handle GET requests or other cases
        # Example: Render a form template
        return render(request, 'contact_form.html', contact)
    
    

def book_table(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_success')
    else:
        form = BookingForm()
    return render(request, 'book_table.html', {'form': form})

