# 📈 Stock News Alert

A Python automation script that monitors stock price changes and sends related news headlines via SMS when a significant price movement occurs.

## ✨ Technologies

- `Python`
- `Requests`
- `API`
- `Twilio`
- `Environment Variables`

## 🚀 Features

- Fetches daily stock price data using a public API
- Calculates percentage price change between trading days
- Retrieves related news articles when a threshold is crossed
- Sends SMS alerts with price movement and headlines
- Secure handling of API keys using environment variables

## 📍 The Process

This project was built as **Day 36 of the 100 Days of Python Code** course and serves as an application of concepts learned across multiple previous days.

The script fetches stock price data and compares the latest closing price with the previous day’s close to calculate the percentage change. If the change exceeds a predefined threshold, the program retrieves relevant news articles related to the company using a news API.

The price movement indicator (up or down) and top headlines are then formatted into messages and sent to the user via the Twilio SMS service. This project reinforced working with multiple APIs, conditional logic, data parsing, and secure credential management using environment variables.

The script is designed to be deployed on a cloud platform such as **PythonAnywhere** to run automatically.

## 🚦 Running the Project

1. Clone the repository  
2. Set required environment variables:
   - `STOCK_API_KEY`
   - `NEWS_API_KEY`
   - `TWILIO_ACCOUNT_SID`
   - `TWILIO_AUTH_TOKEN`
   - `TWILIO_PHONE`
   - `RECEIVER_PHONE`
3. Install dependencies: `pip install requests twilio`
4. Run the script: `python main.py`
5. (Optional) Deploy for scheduled execution
