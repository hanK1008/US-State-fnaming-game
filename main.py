from turtle import Turtle, Screen
import pandas

screen = Screen()
image = "blank_states_img.gif"
screen.addshape(image)
picture = Turtle()
picture.shape(image)
naming_turtle = Turtle()
naming_turtle.hideturtle()
naming_turtle.penup()


# TODO: Reading csv file and getting hold of the data of the state
def check_answer():
    data = pandas.read_csv("50_states.csv")
    state_list = data.state.tolist()
    answer = data[data.state == user_input]
    if user_input in state_list:
        user_correct_guess.append(user_input)
        x_cord = int(answer.x)
        y_cord = int(answer.y)
        return x_cord, y_cord
    else:
        return "Wrong answer"


user_correct_guess = []
game_on = True
while game_on:
    # TODO: Creating input dialogue box
    user_input = screen.textinput(title=f"{len(user_correct_guess)}/50 State Correct",
                                  prompt="Guess the name of state").title()
    if user_input == "Exit":
        break
    user_answer = check_answer()

    if user_answer == "Wrong answer":
        pass
    else:
        naming_turtle.goto(user_answer)
        naming_turtle.write(user_input)

    if len(user_correct_guess) == 50:
        game_on = False

data = pandas.read_csv("50_states.csv")
state_list = data.state.tolist()
for element in user_correct_guess:
    state_list.remove(element)

user_missed_list = pandas.DataFrame(state_list)
user_missed_list.to_csv("Missed State.csv")

