name = "Mezei Dávid"
age = input("Enter your age: ")
height = float(input("Enter your height: ") )
is_student = True
print(f"Name: {name},\nAge: {age},\nHeight: {height},\nStudent: {is_student}")


# Adattípusok ellenőrzése
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

print(round(height) + 0.1)