import os
import re
import threading
import time
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from turtle import heading

os.system("title Discord Token Format Changer Console - Made by Tettu0530")

window = tk.Tk()

window.config(background="#ffffff")
window.title("Discord Token Format Changer - Made by Tettu0530")
window.geometry("800x400")

title = tk.Label(window, font=("Yu Gothic UI Semibold", 20),
                 text="Discord Token Format Changer", fg='#000000', bg='#ffffff')
title.place(x=200, y=0)


def change_format():
    delay = delay_range.get()
    file_token = filedialog.askopenfilename()
    tokens = open(file_token, "r").read().split("\n")
    print(f"Loaded {len(tokens)} of tokens!")
    for i in tokens:
        tokens2 = i + "\n"
        tokens_text.insert("1.0", tokens2)
        loaded_tokens["text"] = f"Loaded tokens: {len(tokens)}"
    time.sleep(1)
    f_token = open("tokens_changed.txt", "w", encoding="utf-8")
    f_mail = open("mailpass_canged.txt", "w", encoding="utf-8")
    tokens_ = tokens
    count = 0
    failure_count = 0
    for i in tokens_:
        try:
            token_changed = i.split(":")
            f_mail.write(f"{token_changed[0]}:{token_changed[1]}\n")
            f_token.write(f"{token_changed[2]}\n")
            print(f"[Successfully Changed] TOKEN: {token_changed[2]}")
            count += 1
            time.sleep(delay)
        except IndexError:
            print(f"[Failure Changed] TOKEN: {token_changed[0]}")
            failure_count += 1
    success_tokens["text"] = "Success changed: " + str(count)
    fail_tokens["text"] = "Fail changed: " + str(failure_count)
    f_mail.close()
    f_token.close()
    return "break"


def change_format_thread(evnet):
    th1 = threading.Thread(target=change_format)
    th1.start()


file_button = tk.Label(window, text="Made by Tettu0530 お問い合わせは Tettu0530(限定復活)#8084 までどうぞ", font=(
    "Yu Gothic UI Semibold", 10), bg='#ffffff', fg='#000000')
file_button.place(x=20, y=40)

tokens_text = tk.Text(window, width="80", height="20")
tokens_text.place(x="20", y="80", height=290)

loaded_tokens = tk.Label(window, font=("Yu Gothic UI Semibold", 10),
                         text="Loaded tokens: ", fg='#000000', bg='#ffffff')
loaded_tokens.place(x=590, y=80)

success_tokens = tk.Label(window, font=("Yu Gothic UI Semibold", 10),
                          text="Success changed: ", fg='#000000', bg='#ffffff')
success_tokens.place(x=590, y=110)

fail_tokens = tk.Label(window, font=("Yu Gothic UI Semibold", 10),
                       text="Fail changed: ", fg='#000000', bg='#ffffff')
fail_tokens.place(x=590, y=140)

range_label = tk.Label(window, font=("Yu Gothic UI Semibold", 10),
                       text="Delay", fg='#000000', bg='#ffffff')
range_label.place(x=590, y=180)

delay_range = tk.Scale(window, orient=tk.HORIZONTAL, length=190, relief=tk.SUNKEN,
                       bg="#ffffff", from_=0.001, to=10, resolution=0.001)
delay_range.place(x=590, y=210)

start_button = tk.Button(window, text="START TO CHANGE", font=(
    "Yu Gothic UI Semibold", 10), width=24, height=3, bg='#ffffff', fg='#000000', cursor='hand2')
start_button.place(x=590, y=300)
start_button.bind("<Button-1>", change_format_thread)

window.mainloop()
