import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import threading
import backend

window = tk.Tk()
window.title('Приложение CarX')
window.geometry('400x300')

def choose_file():
    file = filedialog.askopenfilename(title='Выберите файл',
                                      filetypes=(('Text files', '*.txt'), ('All files', '*.*')))
    if file:
        label.config(text=f'Файл выбран: {file}')
        threading.Thread(target=process_file, args=(file,)).start()

def process_file(file):
    try:
        start_progress()
        with open(file, 'r', encoding='utf-8') as file:
            backend.process_file(file)
        stop_progress()
        messagebox.showinfo('Успех', 'Файл обработан!')
    except Exception as e:
        stop_progress()
        messagebox.showinfo('Ошибка', 'Файл обработан!')
        #messagebox.showerror('Ошибка', f'Произошла ошибка при обработке файла:\n{e}')

def start_progress():
    progress_bar.start(10)
    progress_bar.pack(pady=10)

def stop_progress():
    progress_bar.stop()
    progress_bar.pack_forget()

label = tk.Label(window, text='Привет! Выбери файл.')
label.pack(pady=20)

file_button = tk.Button(window, text='Выбрать файл', command=choose_file)
file_button.pack(pady=10)

progress_bar = ttk.Progressbar(window, mode='indeterminate')

window.mainloop()