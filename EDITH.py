from datetime import datetime

def greet_user():
    hour = datetime.now().hour
    if 5 <= hour < 12:
        return "Good morning!"
    elif 12 <= hour < 18:
        return "Good afternoon!"
    else:
        return "Good evening!"
def get_date_time():
    now = datetime.now()
    return now.strftime("%A, %d %B %Y %H:%M:%S")
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_email(subject, body, to_email):
    from_email = os.getenv('EMAIL_USER')
    password = os.getenv('EMAIL_PASS')

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.close()
        return "Email sent successfully!"
    except Exception as e:
        return f"Error: {str(e)}"
import requests

def get_weather(city):
    api_key = os.getenv('WEATHER_API_KEY')
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    weather_data = response.json()
    if weather_data.get('cod') != 200:
        return "City not found."
    main = weather_data['main']
    return f"Temperature: {main['temp']}°C, Humidity: {main['humidity']}%"
import pyttsx3
import speech_recognition as sr

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return "Could not understand audio."
        except sr.RequestError:
            return "Could not request results."
from bs4 import BeautifulSoup

def search_web(query):
    url = f"https://www.google.com/search?q={query}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    results = soup.find_all('div', class_='BNeawe')
    return results[0].get_text() if results else "No results found."
from PIL import Image
import io

def get_image(url):
    response = requests.get(url)
    img = Image.open(io.BytesIO(response.content))
    img.show()
import os

def open_pdf(file_path):
    os.system(f'xdg-open {file_path}')
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyAssistant(QMainWindow):
    def __init__(self):
        super(MyAssistant, self).__init__()
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("Personal AI Assistant")

    def greet(self):
        greeting = greet_user()
        self.label.setText(greeting)

    def show_date_time(self):
        date_time = get_date_time()
        self.label.setText(date_time)

    # Add more methods for other features

app = QApplication(sys.argv)
win = MyAssistant()
win.show()
sys.exit(app.exec_())
