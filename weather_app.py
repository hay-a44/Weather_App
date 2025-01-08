
import customtkinter as tk
from tkinter import messagebox
from MYSQL import get_weather
import os
from PIL import Image

# Your OpenWeatherMap API key
api_key = "f96804604415a7ca34ee5a5989336d6a"


def weather_info():
    city_name = entry1.get()

    if not city_name:
        messagebox.showerror("Error", "Please enter a valid city name")
        return

    # Fetch weather data
    weather_data = get_weather(city_name, api_key)

    if weather_data:
        # Create a new Toplevel window to display the weather information
        result_window = tk.CTkToplevel(main)
        result_window.title("Weather window")
        result_window.geometry("480x450")
        result_window.config(background='beige')
        image_path1 = os.path.join(os.path.dirname(__file__), "images", "blue.jpg")
        image1 = tk.CTkImage(light_image=Image.open(image_path1), size=(500, 450))
        image_label1 = tk.CTkLabel(result_window, image=image1, text=' ')
        image_label1.place(x=0, y=0)
        image_path3 = os.path.join(os.path.dirname(__file__), "images", "cloud1.jpg")
        image3 = tk.CTkImage(light_image=Image.open(image_path3), size=(80, 80))
        image_label3 = tk.CTkLabel(result_window, image=image3, text=' ')
        image_label3.place(x=20, y=20)
        image_path4 = os.path.join(os.path.dirname(__file__), "images", "rain.jpg")
        image4 = tk.CTkImage(light_image=Image.open(image_path4), size=(80, 80))
        image_label4 = tk.CTkLabel(result_window, image=image4, text=' ')
        image_label4.place(x=410, y=20)
        image_path5 = os.path.join(os.path.dirname(__file__), "images", "sunny.jpg")
        image5 = tk.CTkImage(light_image=Image.open(image_path5), size=(80, 80))
        image_label5 = tk.CTkLabel(result_window, image=image5, text=' ')
        image_label5.place(x=50, y=140)
        image_path6 = os.path.join(os.path.dirname(__file__), "images", "snow.jpg")
        image6 = tk.CTkImage(light_image=Image.open(image_path6), size=(80, 80))
        image_label6 = tk.CTkLabel(result_window, image=image6, text=' ')
        image_label6.place(x=360, y=140)
        image_path7 = os.path.join(os.path.dirname(__file__), "images", "storm.jpg")
        image7 = tk.CTkImage(light_image=Image.open(image_path7), size=(80, 80))
        image_label7 = tk.CTkLabel(result_window, image=image7, text=' ')
        image_label7.place(x=20, y=300)
        image_path8 = os.path.join(os.path.dirname(__file__), "images", "sunup.jpg")
        image8 = tk.CTkImage(light_image=Image.open(image_path8), size=(80, 80))
        image_label8 = tk.CTkLabel(result_window, image=image8, text=' ')
        image_label8.place(x=385, y=290)
        image_path9 = os.path.join(os.path.dirname(__file__), "images", "font_icon.jpg")
        image9 = tk.CTkImage(light_image=Image.open(image_path9), size=(400,80))
        image_label9 = tk.CTkLabel(result_window, image=image9, text=' ')
        image_label9.place(x=0, y=380)
        image_path10 = os.path.join(os.path.dirname(__file__), "images", "font_icon2.jpg")
        image10 = tk.CTkImage(light_image=Image.open(image_path10), size=(80,80))
        image_label10 = tk.CTkLabel(result_window, image=image10, text=' ')
        image_label10.place(x=400, y=380)

        frame2 = tk.CTkFrame(master=result_window, corner_radius=30)
        frame2.pack(padx=30, pady=50)
        lbl1=tk.CTkLabel(frame2,text=f"Weather Update", font=("Helvetica", 30, "bold"), text_color="white")
        lbl1.pack(padx=10, pady=10)

        label2 = tk.CTkLabel(frame2, text=f"City: {weather_data['city']}, {weather_data['country']}",
                         font=("Roboto", 24), text_color="skyblue")
        label2.pack(pady=10)
        weather_label = tk.CTkLabel(frame2, text=f"Temperature: {weather_data['temperature']}°C\n\n"
                                                     f"Weather: {weather_data['weather_description']}\n\n"
                                                        
                                                     f"Humidity: {weather_data['humidity']}%\n\n"
                                                     f"Wind Speed: {weather_data['wind_speed']} m/s",
                                 font=("Roboto", 20), text_color="skyblue")
        weather_label.pack(pady=15, padx=15)
    else:
        messagebox.showerror("Error", "Failed to get weather data. Please try again.")


# Create the main window
main = tk.CTk()
main.geometry("500x470")
main.title("Weather App")
image_path = os.path.join(os.path.dirname(__file__),"images", "sun.jpg")
image= tk.CTkImage(light_image= Image.open(image_path),size=(1000,600))
image_label=tk.CTkLabel(main, image=image, text=' ')
image_label.place(x=0, y=0)
frame = tk.CTkFrame(master=main,corner_radius=10, bg_color="black")
frame.pack( pady=60,padx=60)
frame.place(x=60, y=80)
label= tk.CTkLabel(master=frame,text="Weather Forecasts",font=("Roboto", 28, "bold"))
image_path2 = os.path.join(os.path.dirname(__file__),"images", "cloud.jpg")
image2= tk.CTkImage(light_image= Image.open(image_path2),size=(70,70))
image_label2=tk.CTkLabel(frame, image=image2, text=' ')
image_label2.place(x=150, y=97)
label.pack(pady=60, padx=60)

entry1= tk.CTkEntry(master=frame, placeholder_text="Enter City Here..")
entry1.pack(pady=20, padx= 20)

button1= tk.CTkButton(master=frame, text="Search", command=weather_info)
button1.pack(pady=10, padx=10)


# Start the GUI event loop
main.mainloop()

