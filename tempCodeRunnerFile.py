import tkinter as tk
from tkinter import messagebox
import requests

def get_weather_data(api_key, city_id):
    api_url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city_id}"
    response = requests.get(api_url)
    data = response.json()
    return data

def get_weather_forecast(api_key, city_id):
    api_url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city_id}&days=5"
    response = requests.get(api_url)
    data = response.json()
    return data

def create_forecast_report(data):
    report = "5-Day Weather Forecast:\n"
    for day in data["forecast"]["forecastday"]:
        date = day["date"]
        day_temp = day["day"]["avgtemp_c"]
        max_temp = day["day"]["maxtemp_c"]
        min_temp = day["day"]["mintemp_c"]
        condition = day["day"]["condition"]["text"]
        report += f"Date: {date}, Avg Temp: {day_temp}°C, Max Temp: {max_temp}°C, Min Temp: {min_temp}°C, Condition: {condition}\n"
    return report

def create_weather_report(data):
    report = "Weather Report:\n"
    city = data["location"]["name"]
    report += f"City: {city}\n"
    temperature = data["current"]["temp_c"]
    report += f"Temperature: {temperature}°C\n"
    humidity = data["current"]["humidity"]
    report += f"Humidity: {humidity}%\n"
    wind_speed = data["current"]["wind_kph"]
    report += f"Wind Speed: {wind_speed} kph\n"
    return report

def get_weather():
    city_id = city_entry.get()
    try:
        data = get_weather_data(api_key, city_id)
        report = create_weather_report(data)
        forecast_data = get_weather_forecast(api_key, city_id)
        forecast_report = create_forecast_report(forecast_data)
        result_text.config(state="normal")
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, report + "\n" + forecast_report)
        result_text.config(state="disabled")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

api_key = "5002584aafa64095be362508241205"


root = tk.Tk()
root.title("Weather App")

label = tk.Label(root, text="Enter Location:")
label.pack()

city_entry = tk.Entry(root)
city_entry.pack()

get_weather_button = tk.Button(root, text="Get Weather", command=get_weather)
get_weather_button.pack()

result_text = tk.Text(root, height=20, width=70)
result_text.config(state="disabled")
result_text.pack()

root.mainloop()
