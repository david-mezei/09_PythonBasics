"""
Kérj be három egész számot, és írd ki, melyik a legnagyobb.
"""

first_num = int(input("Kérem az első számot! "))
second_num = int(input("Kérem az második számot! "))
third_num = int(input("Kérem az harmadik számot! "))

greatest_num = 0

if first_num > second_num and first_num > third_num:
    greatest_num = first_num
elif second_num > first_num and second_num > third_num:
    greatest_num = second_num
else: 
    greatest_num = third_num

print(f"A legnagyobb szám: {greatest_num}")