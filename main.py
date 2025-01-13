import tkinter as tk
from tkinter import messagebox, ttk
import ttkbootstrap
from ttkbootstrap.style import Style
from quiz_data import quiz_data, question_numbers, number_choices
import random

#initialize the current question index
indexes = [i for i in range(question_numbers)]
random.shuffle(indexes)
k = 0
current_question = indexes[k]

#function to display current question and choices
def show_question():
    global current_question
    #get the current question from the quiz_data list
    question = quiz_data[current_question]
    qs_label.config(text = question["question"])
    #display the choices on the buttons
    choices = question["choices"]

    for i in range(number_choices):
        choice_btns[i].config(text = choices[i], state = "normal") #reset button state

    #clear the feedback label and display the next button
    feedback_label.config(text = "")
    next_btn.config(state = "disabled")

#function to check the selected answer and provide feedback
def check_answer(choice):
    #get the current question from the quiz_data list
    question = quiz_data[current_question]
    selected_choice = choice_btns[choice].cget("text")
    #check if the selected choice matches the correct answer
    if selected_choice == question["answer"]:
    #update the score and displaye it
        global score
        score += 1
        score_label.config(text = "Միավոր: {}/{}".format(score, question_numbers))
        feedback_label.config(text = "Ճիշտ է", foreground = "green")
    else:
        feedback_label.config(text = "Սխալ է", foreground = "red")
    #desplay all choice buttons and enable the next button
    for button in choice_btns:
        button.config(state = "disabled")
    next_btn.config(state = "normal")

#function to move the next question
def next_qusetion():
    global k, indexes, current_question
    k += 1
    #if there are more questions, show the next question
    if k < len(indexes):
        current_question = indexes[k]
        show_question()
    else:
        #if all questions have been answered, displaye the final score and quiz end
        messagebox.showinfo("Խաղն ավատրվեց",
                            "Խաղն ավարտվեց։ Միավորների ընդհանուր քանակը՝ {}/{}".format(score, question_numbers))

        root.destroy()


#create the main  window

root = tk.Tk()
root.title("Quiz App")
root.geometry("600x500")
style = Style(theme = "flatly")

#configure the font size for question and choices buttons
style.configure("TLabel", font = ("Helvetica", 20))
style.configure("TButton", front = ("Helvetica", 16))

#create the question label
qs_label = ttk.Label(
    root, 
    anchor = "center",
    wraplength = 500,
    padding = 10
)

qs_label.pack(pady=10)

#create the choice buttons
choice_btns = []
for i in range (number_choices):
    button = ttk.Button(
        root,
        command = lambda i = i: check_answer(i)
    )
    button.pack(pady=5)
    choice_btns.append(button)

#create the feedback label
feedback_label = ttk.Label(
    root,
    anchor = "center",
    padding = 10
)
feedback_label.pack(pady = 10)

#initialize the score
score = 0

#create the score label
score_label = ttk.Label(
    root,
    text = "Միավոր: 0/{}".format(question_numbers),
    anchor = "center",
    padding = 10
)
score_label.pack(pady = 10)
#create next button
next_btn = ttk.Button(
    root,
    text = "Առաջ",
    command = next_qusetion,
    state = "disabled"
)

next_btn.pack(pady = 10)


#show the first question

show_question()

#start the main event loop
root.mainloop()






