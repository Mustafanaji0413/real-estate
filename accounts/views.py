from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact
from .forms import listingForm
from listings.models import Listing


def register(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
            # Check Username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is already taken.')
                return redirect(register)
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That Email is already in use.')
                    return redirect(register)
                else:
                    # Evrything is avalible
                    user = User.objects.create_user(username=username,
                                                    password=password,
                                                    email=email,
                                                    first_name=first_name,
                                                    last_name=last_name)
                    user.save()
                    messages.success
                    (request, 'You have succesfully registered!')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        # login User
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You have succesfully logged in!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You have logged out')
        return redirect('index')


def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)

    context = {
        'contacts': user_contacts
    }
    return render(request, 'accounts/dashboard.html', context)


# listingForm

def createListing(request):
    form = listingForm()
    if request.method == 'POST':
        form = listingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/listings')
    context = {'form': form}
    return render(request, 'accounts/create_listing.html', {'form': form})


def UpdateListing(request, pk):
    listing = Listing.objects.get(id=pk)
    form = listingForm(instance=listing)

    if request.method == 'POST':
        form = listingForm(request.POST, request.FILES, instance=listing)
        if form.is_valid():
            form.save()
            return redirect('listings')

    context = {'form': form}
    return render(request, 'accounts/create_listing.html', {'form': form})


def deleteListing(request, pk):
    listing = Listing.objects.get(id=pk)
    if request.method == 'POST':
        listing.delete()
        return redirect('listings')
    context = {'item': listing}
    return render(request, 'accounts/delete.html', context)
