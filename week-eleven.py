# 📌 Week 11: Automation
# This week focuses on automating repetitive tasks using Python. We will cover:
# ✅ Automating scripts (scheduling tasks)
# ✅ Sending emails and text messages
# ✅ Controlling keyboard and mouse actions
#
# 📌 1. Automating Tasks: Scripting & Scheduling
# Automation can save time by scripting repetitive actions and scheduling them using:
#
# sched (Python's built-in scheduler)
#
# cron (Linux/Mac)
#
# Windows Task Scheduler
#
# 🔹 Automating with Python’s sched Module
# The sched module can be used to run tasks at specific intervals.
#
# Example: Print a message every 10 seconds
import sched
import time

# Create a scheduler
scheduler = sched.scheduler(time.time, time.sleep)

# Function to run
def print_message():
    print("This message appears every 10 seconds.")
    scheduler.enter(10, 1, print_message)

# Schedule the first run
scheduler.enter(10, 1, print_message)
scheduler.run()
# 📝 Explanation:
#
# We create a scheduler that runs every 10 seconds.
#
# The function is scheduled repeatedly using scheduler.enter().
#
# 🔹 Automating Tasks with cron (Linux/Mac)
# Step 1: Open the crontab editor
# Run:

# crontab -e

# Step 2: Add a cron job
# To run a Python script (script.py) every 5 minutes:

# */5 * * * * /usr/bin/python3 /path/to/script.py
# 📝 Explanation:

# */5 → Runs every 5 minutes
#
# * * * * → Runs at all hours, days, and months


# 🔹 Automating with Windows Task Scheduler
# Open Task Scheduler
#
# Click Create Basic Task
#
# Set the trigger (e.g., daily, at startup)
#
# Set Action to Start a program
#
# Select python.exe and enter the path to your script

# 📌 2. Sending Emails and Text Messages
# 🔹 Sending Emails with smtplib
# The smtplib module allows Python to send emails.
#
# Example: Send an Email with Gmail
import smtplib
from email.mime.text import MIMEText

# Email details
sender_email = "your_email@gmail.com"
receiver_email = "receiver@example.com"
password = "your_email_password"

# Email content
msg = MIMEText("Hello! This is an automated email.")
msg["Subject"] = "Automated Email"
msg["From"] = sender_email
msg["To"] = receiver_email

# Sending email
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()  # Secure connection
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())

print("Email sent!")
# 📝 Note: You may need to enable "Less Secure Apps" on your Gmail account.
#
# 🔹 Sending Text Messages with Twilio
# Twilio allows us to send SMS using Python.

# Step 1: Install Twilio
# pip install twilio
# Step 2: Send an SMS

from twilio.rest import Client
import os

# # Twilio credentials
account_sid = os.environ.get("your_twilio_account_sid")
auth_token = os.environ.get("your_twilio_auth_token")
twilio_number = os.environ.get("+1234567890")
recipient_number = "+0987654321"

# Initialize Twilio client
client = Client(account_sid, auth_token)

# Send message
message = client.messages.create(
    body="Hello! This is an automated SMS.",
    from_=twilio_number,
    to=recipient_number
)

print("Message sent! Message SID:", message.sid)

# 📝 Note: You need to sign up for Twilio and get an account SID, auth token, and a Twilio phone number.
#
# 📌 3. Controlling Keyboard and Mouse with pyautogui
# The pyautogui module lets us control the mouse, keyboard, and screen.
#
# 🔹 Install pyautogui

# pip install pyautogui
# 🔹 Move the Mouse

import pyautogui

# Move mouse to (x=500, y=300) in 2 seconds
pyautogui.moveTo(500, 300, duration=2)
# 🔹 Click a Button

import pyautogui

# Move to a location and click
pyautogui.moveTo(500, 300, duration=1)
pyautogui.click()
# 🔹 Type on Keyboard

import pyautogui

# Type text with a delay between each key
pyautogui.write("Hello, this is an automated message!", interval=0.1)
# 🔹 Press a Key

import pyautogui

# Press the "enter" key
pyautogui.press("enter")
# 🔹 Take a Screenshot

import pyautogui

# Take a screenshot and save it
screenshot = pyautogui.screenshot()
screenshot.save("screenshot.png")

# 🎯 Homework/Challenges
# Automate your daily tasks (e.g., open your favorite websites every morning).
#
# Write a script to email yourself reminders using smtplib.
#
# Use Twilio to send an SMS alert (e.g., when your code finishes running).
#
# Use pyautogui to automate filling out a form on a website.
#
# Schedule a Python script to run at a specific time using cron or Task Scheduler.
