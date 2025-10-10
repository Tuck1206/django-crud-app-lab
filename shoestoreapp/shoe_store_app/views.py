from django.shortcuts import render

# Create your views here.

# Import HttpResponse to send text-based responses
from django.http import HttpResponse

# Define the home view function
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')



class shoe:
    def __init__(self, name, make, description, price, color, size, gender):
        self.name = name
        self.make = make
        self.description = description
        self.price = price
        self.color = color
        self.size = size
        self.gender = gender


shoes = [
    shoe('Flex Control 4', 'Nike', 'Emphasizing lightweight comfort and stability, ' \
    'the Nike Flex Control 4 is tailored to explosive workouts. ' \
    'Its lightweight, flexible upper has a midfoot strap for stability, ' \
    'while the sole has deep flex grooves to let your foot move naturally.', 45.97, 'Shown: Black/Dark Smoke Grey/Smoke Grey/White', 11.5, 'Male'),
    shoe('Black Suede Lace Up Heels', 'Brooke', 'Lace up heels are a season must have this summer.' \
   ' Style these with one of our stunning bodycon dresses '
   'and match accessories for that classy look that every girl is looking for. Heel approximately 5 inches ', 45, 'Black', '3 True to size', 'Women'),
    shoe('Retro High OG “UNC”', 'Nike Air Jordan 1', 'The women’s Air Jordan 1 High “UNC Patent Leather” is another appealing look for the women’s collection of Michael Jordan’s first signature shoe. ' \
   'The colorway is inspired by Jordan’s college career at the University of North Carolina, and the striking women’s Jordan 1 features a full patent leather build that shines in tones of Blue Chill,' \
   ' Obsidian, and white across the upper with more of the Carolina blue tone for the outsole. It also features the Air Jordan wings logo embossed onto the ankle for an even cleaner look to the glossy colorway. ' \
   'The women’s Air Jordan 1 High “UNC Patent Leather” released in February 2019.', 650, ' obsidian, blue chill-white', 9.5, 'Women'),
    shoe('1948 Mid Brown High Top', 'PUMA', 'The PUMA 1948 Mid Brown High Top is a mid-top sneaker that gives a blend of casual and sporty vibes' \
   ' — elevated above a regular low-top but not quite as tall as a full boot.', 78.40, 'Brown', 10, 'Unisex')
]


def shoe_index(request):
    return render(request, 'shoes/index.html', {'shoes': shoes})
