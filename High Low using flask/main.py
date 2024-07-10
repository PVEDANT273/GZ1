from flask import Flask
from random import randint

generated_number = randint(0, 9)
print(generated_number)

app = Flask(__name__)




def make_bold(function):
    def wrapper():
        return "<b>" + function() + '</b>'

    return wrapper


@app.route('/')
@make_bold
def question():
    return (f"<h1>Guess a number between 0 to 9</h1>"
            f"<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>")


@app.route('/<int:guess>')
#@make_bold
def guess_number(guess):
    if guess < generated_number:
        return ("<h1 style='color:Red'>Too low, try again</h1>"
                f"<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>")
    elif guess > generated_number:
        return ("<h1 style='color:Red'>Too High, try again</h1>"
                f"<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>")
    else:
        return ("<h1 style='color:Green'>Baazooka!!! Correct guess</h1>"
                f"<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>")


if __name__ == "__main__":
    app.run(debug=True)
