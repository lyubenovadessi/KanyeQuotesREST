import json
from tkinter import *
import requests
from tkinter import messagebox


def get_quote():
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    # print(data)
    quote = data["quote"]
    canvas.itemconfig(quote_text, text=quote)
    if len(quote) > 150:
        canvas.itemconfig(quote_text, text=quote, font=("Ariel", 10, "bold"))
    elif len(quote) > 70:
        canvas.itemconfig(quote_text, text=quote, font=("Ariel", 20, "bold"))


def on_save():
    quote = canvas.itemcget(quote_text, "text")
    try:
        with open("favourite.json", "r", encoding="utf-8") as favourite_file:
            data = json.load(favourite_file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    if quote not in data:
        data.append(quote)
        with open("favourite.json", "w", encoding="utf-8") as favourite_file:
            json.dump(data, favourite_file, indent=4, ensure_ascii=False )
        messagebox.showinfo(title="SAVED", message="✔️Quote added to Favourites😃")
    else:
        messagebox.showinfo(title="INFO", message="✔️Quote already in Favourites😃")


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="", width=250, font=("Arial", 30, "bold"), fill="black")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

save_button = Button(text="Save", highlightthickness=0, font=("Arial", 30, "normal"),command=on_save)
save_button.grid(row=1, column=1)

window.mainloop()