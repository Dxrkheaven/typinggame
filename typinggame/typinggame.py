from tkinter import *
import random
import time
import keyboard

score = 0
randomwords = ""
start_time = 0
total_attempts = 0
correct_attempts = 0
on = False

words = [
    "apple", "river", "shadow", "clock", "thunder",
    "mirror", "forest", "lantern", "silver", "whisper",
    "mountain", "window", "pencil", "sunshine", "keyboard",
    "ocean", "planet", "butterfly", "diamond", "blanket"
]

def toggle():
    global on
    on = not on
    print("Cheat mode:", on)

    if on:
        cheat()

def cheat():
    if on:
        entry1.delete(0, END)
        entry1.insert(0, randomwords)
        check()

        # repeat every 1 millisecond
        window.after(1, cheat)

def gen():
    global randomwords, start_time

    randomwords = " ".join(random.choice(words) for i in range(5))
    label_words.config(text=randomwords)

    if start_time == 0:
        start_time = time.time()

def check():
    global score, total_attempts, correct_attempts

    user_text = entry1.get()
    total_attempts += 1

    if user_text == randomwords:
        score += 1
        correct_attempts += 1
        label_score.config(text=f"Score: {score}")

    accuracy = (correct_attempts / total_attempts) * 100
    label_accuracy.config(text=f"Accuracy: {accuracy:.1f}%")

    elapsed_minutes = (time.time() - start_time) / 60

    if elapsed_minutes > 0:
        wpm = (correct_attempts * 5) / elapsed_minutes
        label_wpm.config(text=f"WPM: {int(wpm)}")

    entry1.delete(0, END)
    gen()

keyboard.add_hotkey("F6", toggle)

window = Tk()
window.title("Typing Game")
window.geometry("500x300")

label_words = Label(window, text="-", font=("Arial", 14))
entry1 = Entry(window, width=50)

button_generate = Button(window, text="Generate Words", command=gen)
button_check = Button(window, text="Submit", command=check)

label_score = Label(window, text="Score: 0")
label_wpm = Label(window, text="WPM: 0")
label_accuracy = Label(window, text="Accuracy: 0%")

label_words.pack(pady=10)
entry1.pack(pady=10)
button_generate.pack()
button_check.pack(pady=5)

label_score.pack()
label_wpm.pack()
label_accuracy.pack()

gen()
window.mainloop()