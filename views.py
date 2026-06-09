from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import joblib
import pandas as pd

# ================= LOAD DATASET =================

orders_data = pd.read_csv("bakery_orders_200_records.csv")

# ================= ML MODEL =================

model = joblib.load('bakery/model.pkl')
encoder = joblib.load('bakery/encoder.pkl')


def predict_category(price, quantity):

    data = pd.DataFrame(
        [[price, quantity]],
        columns=['price', 'quantity']
    )

    prediction = model.predict(data)

    category = encoder.inverse_transform(prediction)

    return category[0]


# ================= HOME =================

def home(request):
    return render(request, 'home.html')


# ================= AUTH =================

def signup_view(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():

            return render(request, 'signup.html', {
                'error': 'Username already exists'
            })

        User.objects.create_user(
            username=username,
            password=password
        )

        return redirect('login')

    return render(request, 'signup.html')


def login_view(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('home')

        else:

            return render(request, 'login.html', {
                'error': 'Invalid Username or Password'
            })

    return render(request, 'login.html')


def logout_view(request):

    logout(request)

    return redirect('home')


# ================= CATEGORY PAGES =================

def cakes(request):
    return render(request, 'cakes.html')


def cupcakes(request):
    return render(request, 'cupcakes.html')


def bouquets(request):
    return render(request, 'bouquets.html')


def brownies(request):
    return render(request, 'brownies.html')


def pastries(request):
    return render(request, 'pastries.html')


def cookies(request):
    return render(request, 'cookies.html')


def savouries(request):
    return render(request, 'savouries.html')


# ================= ADD TO CART =================

def add_to_cart(request, name, price):

    cart = request.session.get('cart', [])

    found = False

    for item in cart:

        if item['name'] == name:

            item['quantity'] += 1
            found = True
            break

    if not found:

        cart.append({
            'name': name,
            'price': int(price),
            'quantity': 1
        })

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('cart')


# ================= INCREASE =================

def increase_quantity(request, name):

    cart = request.session.get('cart', [])

    for item in cart:

        if item['name'] == name:
            item['quantity'] += 1
            break

    request.session['cart'] = cart

    return redirect('cart')


# ================= DECREASE =================

def decrease_quantity(request, name):

    cart = request.session.get('cart', [])

    for item in cart:

        if item['name'] == name:

            item['quantity'] -= 1

            if item['quantity'] <= 0:
                cart.remove(item)

            break

    request.session['cart'] = cart

    return redirect('cart')


# ================= REMOVE =================

def remove_item(request, name):

    cart = request.session.get('cart', [])

    cart = [
        item for item in cart
        if item['name'] != name
    ]

    request.session['cart'] = cart

    return redirect('cart')


# ================= CART =================

def cart(request):

    items = request.session.get('cart', [])

    total = 0
    total_items = 0

    categories = []

    for item in items:

        qty = item.get('quantity', 1)

        total += item['price'] * qty
        total_items += qty

        lname = item['name'].lower()

        if "cake" in lname and "cupcake" not in lname:
            categories.append("Cake")

        elif "cupcake" in lname:
            categories.append("Cupcake")

        elif "brownie" in lname:
            categories.append("Brownie")

        elif "cookie" in lname:
            categories.append("Cookie")

        elif "pastry" in lname:
            categories.append("Pastry")

        elif "bouquet" in lname:
            categories.append("Bouquet")

        elif "sandwich" in lname or "pizza" in lname:
            categories.append("Savoury")

    # ================= AI PREDICTION =================

    predicted_category = "No Prediction"

    if total_items > 0:
        predicted_category = predict_category(total, total_items)

    # ================= AI RECOMMENDATION =================

    recommendation = "Try our Bestseller Cheesecake 🍰"

    if items:

        cart_products = []

        for item in items:
            cart_products.append(item['name'])

        recommended_products = []

        for product in cart_products:

            similar = orders_data[
                orders_data['product_name'].str.contains(
                    product.split()[0],
                    case=False,
                    na=False
                )
            ]

            for _, row in similar.iterrows():

                pname = row['product_name']

                if pname not in cart_products:
                    recommended_products.append(pname)

        recommended_products = list(set(recommended_products))

        if len(recommended_products) > 0:
            recommendation = "Customers also buy: " + recommended_products[0]

    return render(request, 'cart.html', {

        'items': items,
        'total': total,
        'total_items': total_items,
        'predicted_category': predicted_category,
        'recommendation': recommendation

    })


# ================= ANALYTICS =================

def analytics(request):

    items = request.session.get('cart', [])

    category_count = {
        "Cake": 0,
        "Cupcake": 0,
        "Brownie": 0,
        "Pastry": 0,
        "Cookie": 0,
        "Bouquet": 0,
        "Savoury": 0
    }

    total_sales = 0
    total_items = 0

    product_count = {}

    for item in items:

        qty = item.get('quantity', 1)

        total_sales += item['price'] * qty
        total_items += qty

        name = item['name']

        product_count[name] = product_count.get(name, 0) + qty

        lname = name.lower()

        if "cake" in lname and "cupcake" not in lname:
            category_count["Cake"] += qty

        elif "cupcake" in lname:
            category_count["Cupcake"] += qty

        elif "brownie" in lname:
            category_count["Brownie"] += qty

        elif "pastry" in lname:
            category_count["Pastry"] += qty

        elif "cookie" in lname:
            category_count["Cookie"] += qty

        elif "bouquet" in lname:
            category_count["Bouquet"] += qty

        elif "sandwich" in lname or "pizza" in lname:
            category_count["Savoury"] += qty

    top_item = "No Item"

    if product_count:
        top_item = max(product_count, key=product_count.get)

    top_category = max(category_count, key=category_count.get)

    predicted_category = "No Prediction"

    if total_items > 0:
        predicted_category = predict_category(total_sales, total_items)

    return render(request, 'analytics.html', {

        'category_labels': list(category_count.keys()),
        'category_data': list(category_count.values()),
        'top_item': top_item,
        'top_category': top_category,
        'total_items': total_items,
        'total_sales': total_sales,
        'predicted_category': predicted_category

    })