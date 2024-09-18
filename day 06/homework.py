1
user_name = input("what is your age ? :")
user_name = input("what is your name?:")
user_name = input ("what isyour surname?:")



print(user_name  "your name is" + user_surname + "your surname is " + user_name + "and you are " + user_age )


#2


from turtle import *
print("hello world")

width(7)
speed(30)


color("purple")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)


#end of square

#add a door

begin_fill()
forward(70)
color("yellow")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

begin_fill()
color('red')
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#and 

#add window

width(3)
penup()
goto(15, 160)
pendown()

begin_fill()
color("blue")
left(30)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()

penup()
goto(180, 160)
pendown()

begin_fill()
color("blue")
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()




exitonclick()