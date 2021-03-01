from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(height=500, width=500)
user_choice = screen.textinput(title="Faça a sua aposta", prompt="Qual tartaruga vencerá a corrida? Escreva a cor: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
position = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y= position[turtle_index])
    all_turtles.append(new_turtle)

while user_choice:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 238:
            is_race_on = False
            wining_color = turtle.pencolor()
            if wining_color == user_choice:
                print(f"Você venceu! {wining_color} é o vencedor!")
            else:
                print(f"Você perdeu! {wining_color} é o vencedor!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()