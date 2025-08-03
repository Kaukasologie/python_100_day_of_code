import turtle
import pandas

def write_state(state_name, x_cor, y_cor):
    """Write name of state on map"""

    cursor = turtle.Turtle()
    cursor.penup()
    cursor.hideturtle()
    cursor.goto(x_cor, y_cor)
    cursor.write(state_name, font=("Arial", 8, "bold"))


def export_unguessed_states(st_list, guessed_st):
    """Create a list of unguessed states and Export it to csv format"""

    unguessed_states = [state for state in st_list if state not in guessed_st]

    new_data = pandas.DataFrame(unguessed_states)
    new_data.to_csv("unguessed_states.csv")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_list = data["state"].to_list()
guessed_states = []

answer_state = ""
while len(guessed_states) < 50 and answer_state is not None:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?")
    if answer_state is not None:
        answer_state.title()

    if answer_state == "Exit":
        break

    if answer_state in states_list:
        if answer_state not in guessed_states:
            x_coordinate = data[data.state == answer_state].x.iat[0]
            y_coordinate = data[data.state == answer_state].y.iat[0]
            # print(data.at[answer_state, "x"])
            # print(x_coordinate)
            # print(y_coordinate)
            write_state(answer_state, x_coordinate, y_coordinate)
            guessed_states.append(answer_state)
    else:
        print(answer_state)

    export_unguessed_states(states_list, guessed_states)

screen.exitonclick()
