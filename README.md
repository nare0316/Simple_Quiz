💡 Simple Quiz Application

A fun and interactive quiz game built using Python's Tkinter library for the graphical user interface (GUI). This project allows users to answer multiple-choice questions and tracks the score as they progress through the quiz. The questions and answers are predefined in a separate data file (quiz_data.py).

    🔖 Features
1. Multiple-choice questions with 4 answer options.
2. Real-time score display.
3. Immediate feedback on correct or incorrect answers.
4. Questions are shuffled for a unique quiz experience every time.
5. The app ends when all questions are answered, showing the final score.

    🔖 Requirements
To run this project, you will need:
1. Python 3.x installed on your machine.
2. ttkbootstrap module for improved styling (install via pip install ttkbootstrap).

    🔖 Files Overview
📕 main.py
The main file that runs the quiz application. It uses the Tkinter GUI library and ttkbootstrap for styling to display questions, answer choices, and feedback. It also tracks the score and handles user input.
📕 quiz_data.py
Contains the list of quiz questions, multiple-choice answers, and correct answers. Each question is represented as a dictionary containing:
  "question": The quiz question.
  "choices": A list of multiple-choice answers.
  "answer": The correct answer.

    🔖 How to Run the Quiz App

⚙️ Clone this repository
    git clone https://github.com/yourusername/quiz-app-python.git
    cd quiz-app-python
    
⚙️ Install Dependencies
    If you haven't installed ttkbootstrap yet, run the following:
    pip install ttkbootstrap
    
⚙️ Run the Application
    python main.py
