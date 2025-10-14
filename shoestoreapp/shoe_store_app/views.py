from django.shortcuts import render
from shoe_store_app.models import Shoe
# Create your views here.

# Import HttpResponse to send text-based responses
from django.http import HttpResponse

# Define the home view function
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')



# class shoe:
#     def __init__(self, name, make, description, price, color, size, gender, product_url):
#         self.name = name
#         self.make = make
#         self.description = description
#         self.price = price
#         self.color = color
#         self.size = size
#         self.gender = gender
#         self.product_url = product_url


# shoes = [
#     shoe('Flex Control 4', 'Nike', 'Emphasizing lightweight comfort and stability, ' \
#     'the Nike Flex Control 4 is tailored to explosive workouts. ' \
#     'Its lightweight, flexible upper has a midfoot strap for stability, ' \
#     'while the sole has deep flex grooves to let your foot move naturally.', 45.97, 'Shown: Black/Dark Smoke Grey/Smoke Grey/White', 11.5, 'Male','https://static.nike.com/a/images/t_PDP_1728_v1/f_auto,q_auto:eco/b032abc3-ec58-4857-a216-81b36a9f8fdd/NIKE+FLEX+CONTROL+TR4.png'),
#     shoe('Black Suede Lace Up Heels', 'Brooke', 'Lace up heels are a season must have this summer.' \
#    ' Style these with one of our stunning bodycon dresses '
#    'and match accessories for that classy look that every girl is looking for. Heel approximately 5 inches ', 45, 'Black', '3 True to size', 'Women','https://rebelliousfashion.com/cdn/shop/products/Brooke-Black-Suede-Lace-Up-Heels-3_4b193289-a1a4-4155-b759-ec510261acef.jpg?v=1629612013'),
#     shoe('Retro High OG “UNC”', 'Nike Air Jordan 1', 'The women’s Air Jordan 1 High “UNC Patent Leather” is another appealing look for the women’s collection of Michael Jordan’s first signature shoe. ' \
#    'The colorway is inspired by Jordan’s college career at the University of North Carolina, and the striking women’s Jordan 1 features a full patent leather build that shines in tones of Blue Chill,' \
#    ' Obsidian, and white across the upper with more of the Carolina blue tone for the outsole. It also features the Air Jordan wings logo embossed onto the ankle for an even cleaner look to the glossy colorway. ' \
#    'The women’s Air Jordan 1 High “UNC Patent Leather” released in February 2019.', 650, ' obsidian, blue chill-white', 9.5, 'Women','https://mysportsshoe.com/wp-content/uploads/2019/02/806667_01-768x768.jpg'),
#     shoe('1948 Mid Brown High Top', 'PUMA', 'The PUMA 1948 Mid Brown High Top is a mid-top sneaker that gives a blend of casual and sporty vibes' \
#    ' — elevated above a regular low-top but not quite as tall as a full boot.', 78.40, 'Brown', 10, 'Unisex','https://cdna.lystit.com/300/375/tr/photos/kickscrew/219ca748/puma-BROWN-1948-Mid-High-Top.jpeg')
# ]


def shoe_index(request):
    shoes= Shoe.objects.all()
    return render(request, 'shoes/index.html', {'shoes': shoes})


def shoe_detail(request, shoe_id):
    shoe = Shoe.objects.get(id=shoe_id)
    return render(request, 'shoes/detail.html', {'shoe': shoe})


