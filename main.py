from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.setup(height=500, width=400)
screen.textinput(title="Faça a sua aposta", prompt="Qual tartaruga vencerá a corrida? Escreva a cor: ")


screen.exitonclick()