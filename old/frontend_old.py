# no animation

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

import backend
from backend import *

window = tk.Tk()
window.title('CarX')
window.geometry('400x300')

def choose_file():
    file = filedialog.askopenfilename(title='Выберите файл',
                                           filetypes=(('Text files', '*.txt'), ('All files', '*.*')))
    if file:
        label.config(text=f'Файл выбран: {file}')
        process_file(file)

def process_file(file):
    try:
        with open(file, 'r', encoding='utf-8') as file:
            backend.process_file(file)
        messagebox.showinfo('Успех', 'Файл успешно обработан!')
    except Exception as e:
        messagebox.showerror('Ошибка', f'Произошла ошибка при обработке файла:\n{e}')

label = tk.Label(window, text='Привет! Выбери файл.')
label.pack(pady=20)

file_button = tk.Button(window, text='Выбрать файл', command=choose_file)
file_button.pack(pady=10)

window.mainloop()