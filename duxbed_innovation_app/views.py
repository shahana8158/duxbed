from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CareerForm,ProductForm,AppointmentForm
from django.contrib import messages
from .models import SubCategory, Product,fill_your_cart,CartItem, Category, CustomerReview,Appointment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
import mimetypes
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.conf import settings






# def homefn(request):
#     products=fill_your_cart.objects.all()

#     return render(request, 'home.html', {'products': products})






# ✅ REGISTER VIEW
def registerfn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('register')
        else:
            user = User.objects.create_user(username=username, password=password1)
            user.save()
            messages.success(request, 'Registration successful. Please login.')
            return redirect('login')
    return render(request, 'register.html')


# ✅ LOGIN VIEW
def loginfn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome, {user.username}!")
            return redirect('/')  # 🔄 change 'home' to your home page name
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')
    return render(request, 'login.html')


# ✅ LOGOUT VIEW
def logoutfn(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')







def homefn(request):
    reviews = CustomerReview.objects.all()
    return render(request, 'home.html', {'reviews': reviews})



def stores_view(request):

    
    return render(request, 'stores.html')







def languagesfn(request):
    selected_lang = request.GET.get('lang')
    if selected_lang:
        request.session['language'] = selected_lang
        return redirect('/')  # Or change to any page you prefer
    return render(request, 'languages.html')




def whyduxfn(request):
    
    return render(request, 'whydux.html')




def morefn(request):
    
    return render(request, 'more.html')






def cartfn(request):
    cart_items = CartItem.objects.all()  # Or filter for specific user/session
    total = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total': total})





def searchfn(request):
    query = request.GET.get('query')
    results = []

    if query:
        results = Product.objects.filter(name__icontains=query)  # Update 'Product' model as per your app

    return render(request, 'search.html', {'results': results})







# def careerfn(request):
#     if request.method == 'POST':
#         form = CareerForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Your application has been submitted successfully!')
#             return redirect('career')  # URL name for career page
#     else:
#         form = CareerForm()
#     return render(request, 'career.html', {'form': form})






def careerfn(request):
    if request.method == 'POST':
        form = CareerForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            email_address = form.cleaned_data['email']
            resume = request.FILES['resume']

            # ✅ Read file BEFORE saving the form
            resume_content = resume.read()
            resume_name = resume.name
            resume_type = resume.content_type

            form.save()  # Save after reading file content

            # Send email
            email = EmailMessage(
                subject='New Career Submission',
                body=f"Name: {name}\nEmail: {email_address}",
                from_email='duxbed2025@gmail.com',
                to=['xxxxxxxx@gmail.com'], 
            )
            email.attach(resume_name, resume_content, resume_type)
            email.send()

            messages.success(request, 'Application submitted successfully!')
            return redirect('career')
    else:
        form = CareerForm()

    return render(request, 'career.html', {'form': form})



def solidfurniturefn(request):
    
 subcategory = SubCategory.objects.get(name="Solid Furniture")
 products = Product.objects.filter(subcategory=subcategory)
 return render(request, 'solid furniture.html', {
        'heading': subcategory.name,
        'products': products
    })



# def bedcotfn(request):
#     subcategory = SubCategory.objects.get(name="Bed Cot")
#     products = Product.objects.filter(subcategory=subcategory)
#     return render(request, 'product_page.html', {
#         'heading': subcategory.name,
#         'products': products
#     })




def bedcotfn(request):
    subcategory = SubCategory.objects.get(name="Bed Cot")
    products = Product.objects.filter(subcategory=subcategory)
    return render(request, 'bedcot.html', {
        'heading': subcategory.name,
        'products': products
    })



def sofacomebedfn(request):

 subcategory = SubCategory.objects.get(name="Sofa Cum Bed")
 products = Product.objects.filter(subcategory=subcategory)
 return render(request, 'sofacomebed.html', {
        'heading': subcategory.name,
        'products': products
    })



def storagebedfn(request):
    
 subcategory = SubCategory.objects.get(name="Storage Bed")
 products = Product.objects.filter(subcategory=subcategory)
 return render(request, 'storagebed.html', {
        'heading': subcategory.name,
        'products': products
    })



def bridalsetfn(request):
    
 subcategory = SubCategory.objects.get(name="Bridal Set")
 products = Product.objects.filter(subcategory=subcategory)
 return render(request, 'bridalset.html', {
        'heading': subcategory.name,
        'products': products
    })




def ironboardfn(request):
    
 subcategory = SubCategory.objects.get(name="Iron Board")
 products = Product.objects.filter(subcategory=subcategory)
 return render(request, 'ironboard.html', {
        'heading': subcategory.name,
        'products': products
    })



def shoerackfn(request):
    
 subcategory = SubCategory.objects.get(name="Shoe Rack")
 products = Product.objects.filter(subcategory=subcategory)
 return render(request, 'shoerack.html', {
        'heading': subcategory.name,
        'products': products
    })





def diningtablefn(request):
    
 subcategory = SubCategory.objects.get(name="Dining Table")
 products = Product.objects.filter(subcategory=subcategory)
 return render(request, 'dining.html', {
        'heading': subcategory.name,
        'products': products
    })



def coffeecounterfn(request):
    
 subcategory = SubCategory.objects.get(name="Coffee Counter")
 products = Product.objects.filter(subcategory=subcategory)
 return render(request, 'coffeecounter.html', {
        'heading': subcategory.name,
        'products': products
    })



def studyunitfn(request):
    
 subcategory = SubCategory.objects.get(name="Study Unit")
 products = Product.objects.filter(subcategory=subcategory)
 return render(request, 'studyunit.html', {
        'heading': subcategory.name,
        'products': products
    })




def mirrorunitfn(request):
    
 subcategory = SubCategory.objects.get(name="Mirror Unit")
 products = Product.objects.filter(subcategory=subcategory)
 return render(request, 'mirrorunit.html', {
        'heading': subcategory.name,
        'products': products
    })



def interiorfn(request):
    
 subcategory = SubCategory.objects.get(name="Interior Designing")
 products = Product.objects.filter(subcategory=subcategory)
 return render(request, 'interior.html', {
        'heading': subcategory.name,
        'products': products
    })



def islandkitchenfn(request):
    
 subcategory = SubCategory.objects.get(name="Island Kitchen")
 products = Product.objects.filter(subcategory=subcategory)
 return render(request, 'islandkitchen.html', {
        'heading': subcategory.name,
        'products': products
    })




def lshapekitchenfn(request):
    
 subcategory = SubCategory.objects.get(name="Lshape Kitchen")
 products = Product.objects.filter(subcategory=subcategory)
 return render(request, 'lshapekitchen.html', {
        'heading': subcategory.name,
        'products': products
    })





def ushapekitchenfn(request):
    
 subcategory = SubCategory.objects.get(name="Ushape Kitchen")
 products = Product.objects.filter(subcategory=subcategory)
 return render(request, 'ushapekitchen.html', {
        'heading': subcategory.name,
        'products': products
    })





def parallelkitchenfn(request):
    
 subcategory = SubCategory.objects.get(name="Parallel Kitchen")
 products = Product.objects.filter(subcategory=subcategory)
 return render(request, 'parallelkitchen.html', {
        'heading': subcategory.name,
        'products': products
    })




def straightkitchenfn(request):
    
 subcategory = SubCategory.objects.get(name="Straight Kitchen")
 products = Product.objects.filter(subcategory=subcategory)
 return render(request, 'straightkitchen.html', {
        'heading': subcategory.name,
        'products': products
    })






# Restrict access to superusers (admin)
def is_admin(user):
    return user.is_superuser

@login_required
@user_passes_test(is_admin)
def add_product(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        details = request.POST.get('details')
        image = request.FILES.get('image')
        subcategory_id = request.POST.get('subcategory')

        subcategory = SubCategory.objects.get(id=subcategory_id)

        Product.objects.create(
            name=name,
            price=price,
            details=details,
            image=image,
            subcategory=subcategory
        )
        return redirect('/')  # Change to your category page if needed

    return render(request, 'add_product.html', {'categories': categories})




@login_required
@user_passes_test(is_admin)
def add_review(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        location = request.POST.get('location')
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')

        CustomerReview.objects.create(
            name=name,
            location=location,
            rating=rating,
            comment=comment
        )
        return redirect('/')  # Redirect to home or review section

    return render(request, 'add_review.html')



@login_required
@user_passes_test(is_admin)

def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Product updated successfully.")
            
            # 🔁 Redirect to 'next' page if available
            next_url = request.GET.get('next') or request.POST.get('next')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('/')  # Or fallback page
    else:
        form = ProductForm(instance=product)

    return render(request, 'editproduct.html', {'form': form, 'product': product})


@login_required
@user_passes_test(is_admin)
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.user.is_superuser:
        product.delete()
        messages.success(request, "Product deleted successfully.")
    else:
        messages.error(request, "You do not have permission to delete this product.")

    # Redirect back to 'next' page or home
    next_url = request.GET.get('next')
    if next_url:
        return redirect(next_url)
    return redirect('')  


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})






def submit_booking(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        # Email send
        subject = "New Appointment Booking"
        message = f"Name: {name}\nAddress: {address}\nPhone: {phone}"
        from_email = "duxbed2025@gmail.com"
        to_email = ["xxxxxxxxx@gmail.com"]

        try:
            send_mail(subject, message, from_email, to_email)
            messages.success(request, "Appointment submitted successfully!")
        except:
            messages.error(request, "Something went wrong while sending mail.")

        return redirect('/')

