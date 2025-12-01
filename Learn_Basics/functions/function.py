def calculate_area(b, h, shape = 'triangle'):
    if(shape == 'triangle'):
        return (1/2)*b*h
    elif(shape == 'rectangle'):
        return b*h
    else:
        return 0

area = calculate_area(5,10)
area_r = calculate_area(4,5,'rectangle')

print('Area of triangle: ',area)
print('Area of rectangle: ',area_r)

def print_pattern(n=5):
    for r in range(n):
        s =''
        for c in range(r+1):
            s += '*'
        print(s)

n = int(input('Print Pattern: '))

print_pattern(n)
