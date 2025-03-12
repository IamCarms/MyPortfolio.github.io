from tkinter import *
import tkinter as tk
from geopy import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests 
import pytz 
import apis

#definine function
def getWeather():
    city = textfield.get()
    geolocator = Nominatim(user_agent = "geoapiExcercises")
    location = geolocator.geocode(city)
    obj =TimezoneFinder()
    result = obj.timezone_at(lng = location.longitude, lat = location.latitude)
    
    #Display Location & Current Time
    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("Time: %I:%M %p")
    clock.config(text = current_time)
    name.config(text = f"Current Weather in {home}")

    #Get weather using API
    api =  "https://api.openweathermap.org/data/2.5/weather?q=" + city + f"&appid={apis.nde}"
    
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    description = json_data['weather'][0]['description']
    temp = int(json_data['main']['temp']-273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']

    t.config(text = (temp, "°"))
    c.config(text = (condition, "|", "FEELS", "LIKE", temp, "°"))

    w.config(text = wind)
    h.config(text = humidity)
    d.config(text = description)
    p.config(text = pressure)

root = Tk()
root.title("Weather App")
root.geometry("800x500+300+200")
root.resizable(False, False)
#search box 
Search_image = PhotoImage(file="search.png")
myimage = Label(image=Search_image)
myimage.place(x = 20, y = 20)
textfield = tk.Entry(root, justify="center", width=17, font=("montserrat", 25, "bold"), bg = "#404040", border = 0, fg = "white")
textfield.place(x = 50, y = 40)
textfield.focus()
Search_icon = PhotoImage(file = "search_icon.png")
myimage_icon = Button(image = Search_icon, borderwidth = 0, cursor = "hand2", bg = "#404040", command = getWeather)
myimage_icon.place(x = 400, y = 34)

#Background Image
background = PhotoImage(file = "logo.png")
background_img = Label(image = background)
background_img.place(x = 150, y = 120)

#Bottom Box
bottom_box = PhotoImage(file = "box.png")
box = Label(image = bottom_box)
box.pack(padx = 5, pady = 5, side = "bottom")

#Time
name = Label(root, font = ("arial", 15, "bold"))
name.place(x = 30, y = 100)
clock = Label(root, font = ("poppins", 15))
clock.place(x = 30, y = 130)
#Labels
label = Label(root, text = "WIND", font = ("poppins", 15, "bold"), fg = "white", bg = "#1ab5ef")
label.place(x = 45, y = 400)

label1 = Label(root, text = "HUMIDITY", font = ("poppins", 15, "bold"), fg = "white", bg = "#1ab5ef")
label1.place(x = 250, y = 400)

label2 = Label(root, text = "DESCRIPTION", font = ("poppins", 15, "bold"), fg = "white", bg = "#1ab5ef")
label2.place(x = 430, y = 400)

label3 = Label(root, text = "PRESSURE", font = ("poppins", 15, "bold"), fg = "white", bg = "#1ab5ef")
label3.place(x = 650, y = 400)

t = Label(font = ("arial", 70, "bold"), fg = "#ee666d")
t.place(x = 400, y = 150)
c = Label(font = ("arial", 15, "bold"))
c.place(x = 400, y = 250)

w = Label(text = "", font = ("arial", 20, "bold"), bg = "#1ab5ef")
w.place(x = 55, y = 430)
h = Label(text = "", font = ("arial", 20, "bold"), bg = "#1ab5ef")
h.place(x = 280, y = 430)
d = Label(text = "", font = ("arial", 20, "bold"), bg = "#1ab5ef")
d.place(x = 400, y = 430)
p = Label(text = "", font = ("arial", 20, "bold"), bg = "#1ab5ef")
p.place(x = 650, y = 430)
root.mainloop()