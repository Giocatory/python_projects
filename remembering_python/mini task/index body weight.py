age = int(input())
height = float(input())
weight = float(input())
description = ""

if age < 10 or height <= 0 or weight <= 0 or weight > 500:
    print("Ошибочные входные данные")
else:
    bmi = weight / height ** 2
    bmi = round(bmi, 2)

    if (bmi < 18.5 and age < 45) or (bmi < 22 and age >= 45):
        description = "недостаточной массой тела."
    elif (18.5 <= bmi <= 24.99 and age < 45) or (22 <= bmi <= 26.99 and age >= 45):
        description = "нормальной массой тела."
    elif (25 <= bmi <= 29.99 and age < 45) or (27 <= bmi <= 31.99 and age >= 45):
        description = "избыточной массой тела."
    elif (bmi >= 30 and age < 45) or (bmi >= 32 and age >= 45):
        description = "ожирением."

    print("bmi=", bmi, "Вы относитесь к группе людей с", description)
