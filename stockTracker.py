import schedule
import time
import yfinance as yf
import requests

TELEGRAM_TOKEN = "" #fill with token
CHAT_ID = "" #fill with chat id from bot 


stocks = {
    "NVIDIA": {"symbol": "NVDA", "purchase_price": 1, "quantity": 1},  
    "Apple": {"symbol": "AAPL", "purchase_price": 1, "quantity": 1},
    "Google": {"symbol": "GOOGL", "purchase_price": 1, "quantity": 1},
    "Alibaba": {"symbol": "BABA", "purchase_price": 1, "quantity": 1},
    "Meta": {"symbol": "META", "purchase_price": 1, "quantity": 1},
    "Warner Bros": {"symbol": "WBD", "purchase_price": 1, "quantity": 1},
    "Cardano": {"symbol": "ADA-USD", "purchase_price": 1, "quantity": 1},  
    "Bitcoin": {"symbol": "BTC-USD", "purchase_price": 1, "quantity": 1}
}


def get_stock_price(symbol):
    stock = yf.Ticker(symbol)
    current_price = stock.history(period="1d")["Close"].iloc[-1]
    return round(current_price, 2)


def calculate_profit_or_loss(current_price, purchase_price, quantity):
    total_current_value = current_price * quantity
    total_purchase_value = purchase_price * quantity
    profit_or_loss = total_current_value - total_purchase_value
    return round(profit_or_loss, 2)


def send_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    params = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        print("✅ Správa úspešne odoslaná na Telegram!")
    else:
        print("❌ Chyba pri odosielaní:", response.json())


def job():
    
    prices = {name: get_stock_price(data["symbol"]) for name, data in stocks.items()}
    
    
    message = "📈 *Aktuálne ceny akcií a kryptomien:*\n"
    for name, data in stocks.items():
        current_price = prices[name]
        purchase_price = data["purchase_price"]
        quantity = data["quantity"]
        profit_or_loss = calculate_profit_or_loss(current_price, purchase_price, quantity)
        
        
        message += f"{name}: {current_price} USD\n"
        if profit_or_loss >= 0:
            message += f"Zisk: +{profit_or_loss} USD\n"
        else:
            message += f"Strata: {profit_or_loss} USD\n"
    
    send_message(message)


job()


schedule.every(1).hour.do(job)

print("Skript beží a čaká na naplánované úlohy...")
while True:
    schedule.run_pending()
    time.sleep(60)  
