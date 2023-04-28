import requests
import tkinter as tk
from datetime import datetime


def trackbitcoin():
  url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR"
  response = requests.get(url).json()
  price = response["USD"]
  time = datetime.now().strftime("%H:%M:%S")

  labelPrice.configure(text = "$" + str(price))
  labelTime.configure(text ="Updated at:" + time)



canvas = tk.Tk()
canvas.geometry("400x300")
canvas.title('Bitcoin Tracker')

f1= ("poppins", 24, "bold")
f2= ("poppins", 50, "bold")
f3= ("poppins", 18, "italic")

label= tk.Label(canvas, text= "Bitcoin Price", font= f1)
label.pack(pady= 20)

labelPrice = tk.Label(canvas, font= f2)
labelPrice.pack(pady= 20)

labelTime = tk.Label(canvas, font= f3)
labelTime.pack(pady = 20)
canvas.after(100, trackbitcoin)

canvas.mainloop()