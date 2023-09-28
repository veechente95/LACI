import os
import vonage
import schedule
import time

# Your Vonage Auth ID and Auth Token
vonage_key = os.environ.get("VONAGE_KEY")
vonage_secret = os.environ.get("VONAGE_SECRET")

# Create a Vonage client
client = vonage.Client(key=vonage_key, secret=vonage_secret)
sms = vonage.Sms(client)


# Function that sends message to user
def send_message():
    message = "ENTER YOUR MESSAGE HERE"

    response_data = sms.send_message({
        "from": "YOUR VONAGE NUMBER",
        "to": "YOUR PHONE NUMBER",
        "text": message,
    })

    if response_data["messages"][0]["status"] == "0":
        print("Message sent successfully.")
    else:
        print(f"Message failed with error: {response_data['messages'][0]['error-text']}")


# Schedule when to send the message (e.g., daily at 9:00 AM)
schedule.every().day.at("09:00").do(send_message)

# Loop to run scheduled texts
while True:
    schedule.run_pending()
    time.sleep(1)
