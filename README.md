**Telegram Stock & Crypto Tracker Bot**
Overview

This repository contains a Python script that tracks the latest stock and cryptocurrency prices using Yahoo Finance and sends periodic reports to a Telegram bot. It calculates the profit or loss based on the initial purchase price and quantity of each asset.

**Features**

-Fetches real-time stock and cryptocurrency prices from Yahoo Finance.

-Calculates profit or loss for each asset based on the initial purchase price and quantity.

-Sends periodic updates to a Telegram chat using a bot.

-Uses schedule to run the job every hour.

**1.**Setup & Installation****

Clone the repository:
git clone "repo-url",
cd "repo-folder"

**2.**Install the required dependencies:****

pip install yfinance requests schedule

****3.**Create and configure your Telegram bot:******

Go to BotFather on Telegram and create a new bot.

Get the API token from BotFather.

Start a chat with your bot and retrieve your chat_id (can be obtained from @RawDataBot on Telegram).

4.**Configure the script:**

Replace TELEGRAM_TOKEN with your bot's API token.

Replace CHAT_ID with your Telegram chat ID.

Modify the stocks dictionary to set your purchase price and quantity.

**5.Run the script:**

python stockTracker.py

**Code Breakdown**

Fetching Stock Prices: Uses yfinance to retrieve the latest closing prices.

Calculating ****Profit or Loss****: Computes the difference between the current and purchase price multiplied by quantity.

Sending Messages to Telegram: Uses requests to send updates via Telegram Bot API.

Automating Execution: The script runs every hour using schedule.

**Example Output**

📈 *Aktuálne ceny akcií a kryptomien:*
NVIDIA: 900 USD
Zisk: +100 USD
Apple: 150 USD
Strata: -50 USD
Bitcoin: 45000 USD
Zisk: +5000 USD****


