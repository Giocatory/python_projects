from math import sqrt, acos, degrees

def compute_area(a_1, a_2, a_3):
    """Реализовать функцию для вычисления площади треугольника по трем сторонам a_1, a_2, a_3."""
    p = (a_1 + a_2 + a_3) / 2
    area = sqrt(p * (p - a_1) * (p - a_2) * (p - a_3))
    return area

def compute_angle(a_1, a_2, a_3):
    """Реализовать функцию для вычисления угла треугольника в градусах, если известны длины сторон a_1, a_2, a_3."""
    angle_rad = acos((a_1 ** 2 + a_2 ** 2 - a_3 ** 2)/(2 * a_1 * a_2))
    return degrees(angle_rad)

def compute_len(x_0,y_0,x_1,y_1):
    """ Реализовать функцию для вычисления длины отрезка с координатами концов (x0, y0) и (x1, y1)."""
    len_line = sqrt((x_1 - x_0) ** 2 + (y_1 - y_0) ** 2)
    return len_line

x_a = 0; y_a = 10; x_b =-5; y_b = 0; x_c = 5; y_c = 0

c = compute_len(x_a, y_a, x_b, y_b)
a = compute_len(x_b, y_b, x_c, y_c)
b = compute_len(x_a, y_a, x_c, y_c)

if a + b <= c or b + c <= a or a +c <= b:
    print("Треугольник не существует")
else:     
    s = compute_area(a, b,c)    
    p = a + b + c    
    angle_A = compute_angle(c, b, a)    
    angle_B = compute_angle(c, a, b)    
    angle_C = compute_angle(a, b, c)

print("Стороны : ", round(a, 3), round(b, 3), round(c, 3))
print("Площадь : ", round(s,3))
print("Периметр : ", round(p,3))
print("Углы : ", round(angle_A, 3), round(angle_B, 3), round(angle_C, 3))
