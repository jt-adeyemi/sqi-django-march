from django.shortcuts import render
from django.utils import timezone

# Create your views here.
def dtl_syntax_demo(request):
    context = {
        'name': 'Joshua',
        'age': 24,
        'courses': ['Python', 'Django', 'SQL', 'HTML/CSS'],
        'is_logged_in': False,
        'no_of_messages': 3,
        'students_grades': {'Pelumi': 'A', "Olumide": "B", "Joshua": "C", "Francis": "D", "Adil": "E"},
        'library': [
            {"title": "Title 1", "author": "Author 1"},
            {"title": "Title 2", "author": "Author 2"},
            {"title": "Title 3", "author": "Author 3"},
        ]
    }
    return render(request, 'dtl/dtl.html', context) 


def shopping_cart(request):
    context = {
        "customer": "Chinedu",
        "cart_items": [
            {"name": "Laptop", "price": 250000, "quantity": 1},
            {"name": "Headphones", "price": 15000, "quantity": 2},
            {"name": "USB Cable", "price": 2000, "quantity": 3},
        ],
        "has_discount": True,
        "store": {
            "name": "Tech World",
            "city": "Abuja",
        },
        "today": timezone.now(),
    }
    return render(request, "dtl/cart.html", context)