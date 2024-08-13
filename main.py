import turtle
import pandas

screen = turtle.Screen()
screen.title("Guess U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
bg = turtle.Turtle()
bg.shape(image)

guessed_state = []
is_on = True

data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()
print(all_states)

while is_on:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States Correct", prompt="What's another state's "
                                                                                              "name?").title()
    print(answer_state)

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_state]
        # for state in all_states:
        #     if state not in guessed_state:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_state.append(answer_state)
        state_data = data[data.state == answer_state]
        state, x, y = state_data["state"], state_data["x"], state_data["y"]

        temp = turtle.Turtle()
        temp.hideturtle()
        temp.penup()
        temp.goto(x.item(), y.item())
        temp.write(state.item())

screen.exitonclick()
