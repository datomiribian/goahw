# 1)  გადმოგვეცემა რიცხვებით სავსე სია, ჩვენ ამ სიიდან უნდა შევკრიბოთ ყველა ხუთის ჯერადი რიცხვი და დავბეჭდოთ მათი ჯამი

sum = 0
numbers = [5,5]
for i in range(len(numbers)):
    if numbers[i] % 5 == 0 :
        sum += numbers[i]
print(sum) 
  