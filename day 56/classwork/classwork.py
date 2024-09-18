def check_age(age):
    my_age = 3  
    if age == my_age:
        return age
    else:
        return "თქვენი ასაკი არ ემთხვევა"


user_age = 3 
print(check_age(user_age))

def get_my_age():
    return 3  


print(get_my_age())




def rectangle_area(length, height):
    """
    გამოთვლის მართკუთხედის ფართობს.
    
    :param length: მართკუთხედის სიგრძე
    :param height: მართკუთხედის სიმაღლე
    :return: მართკუთხედის ფართობი
    """
    return length * height


length = 5  
height = 3   
area = rectangle_area(length, height)
print(f"მართკუთხედის ფართობი: {area}")




def print_min_max(numbers):
    """
    განიხილავს სიის რიცხვებს და დაბეჭდავს მინიმალურ და მაქსიმალურ რიცხვებს.
    
    :param numbers: სია რიცხვების
    """
    if not numbers:
        print("სია ცარიელია.")
        return
    
  
    min_value = numbers[0]
    max_value = numbers[0]
    
  
    for number in numbers:
        if number < min_value:
            min_value = number
        elif number > max_value:
            max_value = number
    
   
    print(f"მინიმალური რიცხვი: {min_value}")
    print(f"მაქსიმალური რიცხვი: {max_value}")


numbers_list = [10, 2, 37, 4, -5, 22]
print_min_max(numbers_list)


def add(a, b):
    """
    რიცხვების დამატება.
    
    :param a: პირველი რიცხვი
    :param b: მეორე რიცხვი
    :return: რიცხვების ჯამი
    """
    return a + b

def subtract(a, b):
    """
    პირველი რიცხვის გამოკლება მეორე რიცხვისგან.
    
    :param a: პირველი რიცხვი
    :param b: მეორე რიცხვი
    :return: პირველი რიცხვისგან მეორე რიცხვის გამოკლებილი მნიშვნელობა
    """
    return a - b

def multiply(a, b):
    """
    რიცხვების გამრავლება.
    
    :param a: პირველი რიცხვი
    :param b: მეორე რიცხვი
    :return: რიცხვების ნამრავლი
    """
    return a * b

def divide(a, b):
    """
    პირველი რიცხვის გაყოფა მეორე რიცხვზე.
    
    :param a: პირველი რიცხვი (მამოძრავებელი)
    :param b: მეორე რიცხვი (განყოფილი)
    :return: პირველი რიცხვის გაყოფილი მნიშვნელობა
    :raises ZeroDivisionError: თუ მეორე რიცხვი არის 0
    """
    if b == 0:
        raise ZeroDivisionError("გაყოფა არ შეიძლება 0-ით.")
    return a / b

x = 10
y = 5

print(f"{x} + {y} = {add(x, y)}")        
print(f"{x} - {y} = {subtract(x, y)}")
print(f"{x} * {y} = {multiply(x, y)}")   
print(f"{x} / {y} = {divide(x, y)}")     


for number in range(1, 51):
    if number % 5 == 0:
        print(number)




       
for number in range(2, 21):
    if number % 2 == 0:
        print(number)


product = 1

for number in range(5, 11):
    product *= number 


print(f"5-დან 10-ის ჩათვლით რიცხვების ნამრავლი:{product} ")


number = int(input("შეიყვანეთ რიცხვი: "))


if number % 2 == 0:
   
    result = number / 2
else:
 
    result = number * 3 + 1


print(f"გახდომილი მნიშვნელობა: {result}")