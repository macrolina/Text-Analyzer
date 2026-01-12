from text_analizer import TextAnalyzer
import tkinter as tk
from tkinter import filedialog
import shutil
import sys
import json

def clean():
    show_answer_label['text']=''

def open_file():
    filepath=filedialog.askopenfilename()
    if filepath!='':
        with open(filepath, 'r', encoding='utf-8') as file:
            text=file.read()
            text_entry.delete("1.0", tk.END)
            text_entry.insert("1.0", text)
def number_of_words():
    text=text_entry.get("1.0", tk.END)
    analyzer=TextAnalyzer(text)
    show_answer_label['text']=analyzer.count()

def popular_words():
    text=text_entry.get("1.0", tk.END)
    analyzer=TextAnalyzer(text)
    directory_path=filedialog.askdirectory()
    with open('popular_words.json', 'w', encoding="utf-8") as file:
        popular_words=analyzer.popular_words()
        json.dump(popular_words, file, ensure_ascii=False, indent=2)
        try:
            this_file=sys.path
            json_path=this_file[0]+r"/popular_words.json"
            shutil.move(json_path, directory_path)
            show_answer_label['text']=f"Success! Path to JSON file {directory_path}"
        except shutil.Error:
            show_answer_label['text'] = f"Success! Path to JSON file {directory_path}"
        except Exception as e:
            show_answer_label['text'] = f"{e}"

def letters_in():
    text=text_entry.get("1.0", tk.END)
    analyzer=TextAnalyzer(text)
    directory_path=filedialog.askdirectory()
    with open("letters_in.json", 'w', encoding='utf-8') as file:
        letters_in=analyzer.letters_in()
        json.dump(letters_in, file, ensure_ascii=False, indent=2)
        try:
            this_file=sys.path
            json_path=this_file[0]+r'/letters_in.json'
            shutil.move(json_path, directory_path)
            show_answer_label['text'] = f"Success! Path to JSON file {directory_path}"
        except shutil.Error:
            show_answer_label['text'] = f"Success! Path to JSON file {directory_path}"
        except Exception as e:
            show_answer_label['text'] = f"{e}"

window=tk.Tk()
window.title("Text Analyzer")
window.geometry("700x600")

text_entry=tk.Text(window, width=50, height=20, font='Calibri 12', bd=3)

show_answer_label=tk.Label(window, font='Calibri 13', text='')

number_of_words_button=tk.Button(window, text='Number of words', font='Calibri 14', command=number_of_words)
popular_words_button=tk.Button(window, text='Popular words', font='Calibri 14', command=popular_words)
letters_in_button=tk.Button(window, text='Letters in text', font='Calibri 14', command=letters_in)
clean_answer_button=tk.Button(window, text='Clean', font='Calibri 14', command=clean)

open_file_menu=tk.Menu()
view_menu=tk.Menu(open_file_menu)
view_menu.add_checkbutton(label="Open file", onvalue=1, offvalue=0, selectcolor='gray', command=open_file)
open_file_menu.add_cascade(label="Idk", menu=view_menu)

text_entry.pack()
show_answer_label.pack()
number_of_words_button.place(x=30, y=425)
popular_words_button.place(x=200, y=425)
letters_in_button.place(x=350, y=425)
clean_answer_button.place(x=500, y=425)

window.config(menu=open_file_menu)
window.mainloop()
