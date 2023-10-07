import turtle
import pandas

screen = turtle.Screen()
screen.title("Bharath States Game")
image = "BharathStatesMap.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("49_States.csv")
all_states = data.State.to_list()
guessed_states = []

while len(guessed_states) < 35:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/35 States & Union Territories Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.State == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

if len(guessed_states) == len(all_states):
    print("Congratulation You Won This Game...")
