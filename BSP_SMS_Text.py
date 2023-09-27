import os
import vonage
import schedule
import time

# Your Plivo Auth ID and Auth Token
vonage_key = os.environ.get("VONAGE_KEY")
vonage_secret = os.environ.get("VONAGE_SECRET")

# Create a Plivo client
client = vonage.Client(key=vonage_key, secret=vonage_secret)
sms = vonage.Sms(client)


# Function that sends message to user
def send_message():
    message = "Rates are lower! Time to water your plants!\n\n"

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
schedule.every().day.at("19:04").do(send_message)

# Loop to run scheduled text the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)
