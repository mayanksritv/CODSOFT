import tkinter as tk
import random

class RockPaperScissors:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Rock, Paper, Scissors")
        self.window.configure(background="#f0f0f0")

        self.user_score = 0
        self.computer_score = 0

        self.user_choice_label = tk.Label(self.window, text="Your Choice:", font=("Arial", 16), bg="#f0f0f0")
        self.user_choice_label.pack()

        self.computer_choice_label = tk.Label(self.window, text="Computer's Choice:", font=("Arial", 16), bg="#f0f0f0")
        self.computer_choice_label.pack()

        self.result_label = tk.Label(self.window, text="", font=("Arial", 24), bg="#f0f0f0")
        self.result_label.pack()

        self.score_label = tk.Label(self.window, text=f"Score: You - {self.user_score}, Computer - {self.computer_score}", font=("Arial", 16), bg="#f0f0f0")
        self.score_label.pack()

        self.rock_button = tk.Button(self.window, text="Rock", command=lambda: self.play("rock"), font=("Arial", 16), bg="#007bff", fg="white")
        self.rock_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.paper_button = tk.Button(self.window, text="Paper", command=lambda: self.play("paper"), font=("Arial", 16), bg="#007bff", fg="white")
        self.paper_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.scissors_button = tk.Button(self.window, text="Scissors", command=lambda: self.play("scissors"), font=("Arial", 16), bg="#007bff", fg="white")
        self.scissors_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.play_again_button = tk.Button(self.window, text="Play Again", command=self.play_again, font=("Arial", 16), bg="#007bff", fg="white")
        self.play_again_button.pack(padx=10, pady=10)

    def play(self, user_choice):
        computer_choice = random.choice(["rock", "paper", "scissors"])

        self.user_choice_label.config(text=f"Your Choice: {user_choice.capitalize()}")
        self.computer_choice_label.config(text=f"Computer's Choice: {computer_choice.capitalize()}")

        if user_choice == computer_choice:
            self.result_label.config(text="It's a tie!", fg="gray")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            self.result_label.config(text="You win!", fg="green")
            self.user_score += 1
        else:
            self.result_label.config(text="Computer wins!", fg="red")
            self.computer_score += 1

        self.score_label.config(text=f"Score: You - {self.user_score}, Computer - {self.computer_score}")

    def play_again(self):
        self.user_choice_label.config(text="Your Choice:")
        self.computer_choice_label.config(text="Computer's Choice:")
        self.result_label.config(text="")
        self.score_label.config(text=f"Score: You - {self.user_score}, Computer - {self.computer_score}")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = RockPaperScissors()
    game.run()
