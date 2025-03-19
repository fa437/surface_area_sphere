#Surface Area of Sphere = 4πr²

#Approach 1
def surface_area_sphere():
	pi = 3.14
	r = 2 #the unit is metre
	surface_area = 4 * pi * r**2 #Return the calculated area
	return (surface_area)
print("The Surface Area of a Sphere is {:.2f} m²".format(surface_area_sphere()))

#Approach 2
from math import pi

r = 2
surface_area = 4 * pi * r**2 #Return the calculated area
print(f"The Surface Area of a Sphere is {surface_area:.2f} m²")

#Approach 3
def surface_area_sphere(r):
    pi = 3.14
    surface_area = 4 * pi * r**2
    return (surface_area)  #Return the calculated area

print("The surface area of a sphere is", surface_area_sphere(2), "m²") # Calling the function with a radius
