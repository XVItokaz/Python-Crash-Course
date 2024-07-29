# Store information about a pizza being ordered.

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# Summarize the order

print("You ordered a " + pizza['crust'] + "-crust pizza " +
      "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)


    """
    
    Så för att förklara ovan steg på Svenska
    
    1. Vi har en dictionary i variabel pizza, med två innhåll, dvs key (nycklar). Dessa är crust och toppings
    2. Vi har i dictornay och variabel pizza också värden (value) för dessa nycklar, för crust har vi värde thick och för toppings har vi värden mushrooms och extra cheese
    3. Vi printar ut att kunden från variabel pizza och nyckel crust vill ha en thick -crust pizza, då nyckeln har just värde thick. Samt avslutar med texten önskade toppings
    4. i kommande rad kör vi en for loop med påhittat varaibel "topping" men loopar igenom variable pizza och inom parantes specifkt bara nyckel toppings och de två värden 
       (mushroom och extra cheese)

    """