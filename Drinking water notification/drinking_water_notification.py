import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title="Drink Water Reminder",
            message="Drinking water is important for your body. Stay hydrated!",
            timeout=5  # Notification will stay for 5 seconds
        )
        time.sleep(900)  # Waits for 15 minutes (900 seconds) before reminding again