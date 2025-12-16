import requests
from twilio.rest import Client
import os

STOCK = "STOCK_TICKER_SYMBOL"
COMPANY_NAME = "COMPANY_TO_TRACK"

STOCK_ENDPOINT = "STOCK_ENDPOINT_HERE"
NEWS_ENDPOINT = "NEWS_ENDPOINT_HERE"

STOCK_API = os.environ.get("STOCK_API_KEY")
NEWS_API = os.environ.get("NEWS_API_KEY")

ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_PHONE = os.environ.get("TWILIO_PHONE")
RECEIVER_PHONE = os.environ.get("RECEIVER_PHONE")

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API,
}

stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_response.raise_for_status()

stock_json = stock_response.json()
daily_prices = stock_json["Time Series (Daily)"]

# Convert the daily prices to a list sorted by date (latest first)
daily_price_list = [data for (date, data) in daily_prices.items()]

# Closing prices
latest_close = float(daily_price_list[0]["4. close"])
previous_close = float(daily_price_list[1]["4. close"])

# Calculate absolute difference and percentage change
price_diff = latest_close - previous_close

if price_diff > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

price_diff_percent = round((price_diff / latest_close) * 100)

# If price moved more than 1%, fetch news
if abs(price_diff_percent) > 1:
    news_params = {
        "qInTitle": COMPANY_NAME,
        "pageSize": 3,
        "language": "en",
        "apiKey": NEWS_API
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()

    news_articles = news_response.json()["articles"]
    top_articles = news_articles[:3]

    formatted_articles = [f"{STOCK} {up_down} {price_diff_percent}%\nHeadline: {article["title"]} \nBrief: {article["description"]}" for article in top_articles]

    for article in formatted_articles:
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        message = client.messages.create(
            body=article,
            from_=TWILIO_PHONE,
            to=RECEIVER_PHONE,
        )
        print(message.status)

