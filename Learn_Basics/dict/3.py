import math

def circle_calc(r):
    area = math.pi*(r**2)
    circumference = 2*math.pi*r
    diameter=2*r
    return area, circumference, diameter

r=input("Enter a radius:")
r=float(r)
area, c, d = circle_calc(r)
print(f"area {area}, circumference {c}, diameter {d}")
