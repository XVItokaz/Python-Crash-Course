def  make_sandwich(*toppings):
    print("\nMaking a sandwich with following toppings:")
    for topping in toppings:
        print("- " + topping)

make_sandwich('salami')
make_sandwich('ost', 'skinka', 'tomat')
make_sandwich('räksallad', 'gurka', 'saltgurka')

