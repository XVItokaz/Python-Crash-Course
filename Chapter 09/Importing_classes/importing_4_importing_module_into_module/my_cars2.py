from car import Car as CA
from electric_car import ElectricCar as EC

my_mustang = CA('ford', 'mustang', 2014)
print(my_mustang.get_descriptive_name())

my_leaf =   EC('nissan', 'leaf', 2022)
print(my_leaf.get_descriptive_name())