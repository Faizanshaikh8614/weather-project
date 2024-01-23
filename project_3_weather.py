

import tkinter as tk
from PIL import Image, ImageTk
import requests
import bs4
import json

def get_weather():
    city = box1.get()
    url = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=8adf0eeaa8f15ee9bc291b31de74e35e"

    html = requests.get(url)
    soup = bs4.BeautifulSoup(html.text,"html.parser")

    weather =json.loads(soup.text)

    temp = weather["main"]["feels_like"]

    humid = weather["main"]["humidity"]

    wind = round(weather["wind"]["speed"] * 3.6, 2 )

    weather_type =weather["weather"][0]["description"]

    text1.set(str(temp))
    text2.set(str(humid))
    text3.set(str(wind))
    text4.set(weather_type.capitalize())

def kelvinToCelsius(kelvin):
    return kelvin - 273.15
 
 
kelvin = 298.65
celsius = kelvinToCelsius(kelvin)
 
print(celsius)

app = tk.Tk()
app.title("Weather Update")
app.geometry("500x500")
app.resizable(False,False)
app.config(bg="#616161")
app.wm_attributes('-transparentcolor','#ab23ff')

# bg =Image.open ("fall.png")
# #resized_img =bg.resize((50,50))
# zakir = ImageTk.PhotoImage(bg)
# image = tk.Label (image=zakir)
# image.place(x=0,y=0)


box1 =tk.Entry(app,font=("Dubai Medium", 25),bg="#FFFFF0")
# box1.place(x=150,y=20,height=100,width=150)
# box1.focus_set()
box1.pack(pady=30)


img = Image.open("search.png")
resized_img = img.resize((40,40))
icon = ImageTk.PhotoImage(resized_img)
button1 =tk.Button(image= icon,font=("Dubai Medium", 15), command=get_weather)
button1.place(x=430,y=30,height=43,width=40)

text1 = tk.StringVar()
text2 = tk.StringVar()
text3 = tk.StringVar()
text4 = tk.StringVar()

text1.set("")
text2.set("")
text3.set("")
text4.set("")

label1 = tk.Label(app, text="Temperature",font=("Dubai Medium",15),bg="#616161")
label1.place(x=30,y=100)
temp = tk.Label(app,textvariable=text1,font=("Segoe",20),bg="#616161")
temp.place(x=50,y=250)

temp =Image.open ("temp.png")
resized_img =temp.resize((80,80))
Arslan = ImageTk.PhotoImage(resized_img)
image = tk.Label (image=Arslan,bg="orange")
image.place(x=50,y=150)



label2 = tk.Label(app,text="Humidity",font=("Dubai Medium",15),bg="#616161")
hum = tk.Label(app,textvariable=text2,font=("Segoe",20),bg="#616161")
hum.place(x=240,y=250)
label2.place(x=210,y=100)

humidity =Image.open ("humidity.png")
resized_img =humidity.resize((80,80))
Faizan = ImageTk.PhotoImage(resized_img)
image = tk.Label (image=Faizan,bg="#FF6A6A")
image.place(x=210,y=150)

label3 = tk.Label(app,text="Wind",font=("Dubai Medium",15),bg="#616161")
label3.place(x=380,y=100)
wind = tk.Label(app,textvariable=text3,font=("Segoe",20),bg="#616161")
wind.place(x=370,y=250)

wind =Image.open ("wind.png")
resized_img = wind.resize((80,80))
Navid = ImageTk.PhotoImage(resized_img)
image = tk.Label (image=Navid,bg="#8B4C39")
image.place(x=370,y=150)


app.mainloop()