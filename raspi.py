import RPi.GPIO as GPIO
import requests
import time

# GPIO Pin Configuration
SWITCH1 = 19
BUZZER_PIN = 38
RELAY_PIN = 36

# Server Configuration
LAPTOP_SERVER_URL = "http://192.168.14.9:5000/face_unlock"  # Replace with your laptop's IP

# Authentication
MAX_ATTEMPTS = 3
attempts = 0

def setup_gpio():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(SWITCH1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(BUZZER_PIN, GPIO.OUT)
    GPIO.setup(RELAY_PIN, GPIO.OUT)

def trigger_buzzer():
    GPIO.output(BUZZER_PIN, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(BUZZER_PIN, GPIO.LOW)

def trigger_relay():
    GPIO.output(RELAY_PIN, GPIO.HIGH)
    time.sleep(5)
    GPIO.output(RELAY_PIN, GPIO.LOW)

def send_face_unlock_request():
    try:
        response = requests.post(LAPTOP_SERVER_URL, timeout=10)
        return response.json()
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return {"status": "ERROR"}

def main():
    global attempts
    setup_gpio()

    try:
        while True:
            if GPIO.input(SWITCH1) == GPIO.HIGH:
                print("Face unlock initiated...")
                response = send_face_unlock_request()
                if response.get("status") == "SUCCESS":
                    print("KNOWN PERSON ")
                    trigger_relay()
                    attempts = 0
                else:import RPi.GPIO as GPIO
import requests
import time

# GPIO Pin Configuration
SWITCH1 = 19
BUZZER_PIN = 38
RELAY_PIN = 36

# Server Configuration
LAPTOP_SERVER_URL = "http://192.168.14.9:5000/face_unlock"  # Replace with your laptop's IP

# Authentication
MAX_ATTEMPTS = 3
attempts = 0

def setup_gpio():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(SWITCH1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(BUZZER_PIN, GPIO.OUT)
    GPIO.setup(RELAY_PIN, GPIO.OUT)

def trigger_buzzer():
    GPIO.output(BUZZER_PIN, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(BUZZER_PIN, GPIO.LOW)

def trigger_relay():
    GPIO.output(RELAY_PIN, GPIO.HIGH)
    time.sleep(5)
    GPIO.output(RELAY_PIN, GPIO.LOW)

def send_face_unlock_request():
    try:
        response = requests.post(LAPTOP_SERVER_URL, timeout=10)
        return response.json()
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return {"status": "ERROR"}

def main():
    global attempts
    setup_gpio()

    try:
        while True:
            if GPIO.input(SWITCH1) == GPIO.HIGH:
                print("Face unlock initiated...")
                response = send_face_unlock_request()
                if response.get("status") == "SUCCESS":
                    print("KNOWN PERSON ")
                    trigger_relay()
                    attempts = 0
                else:
                    print("UNKNOWN FACE DETECTED DOORBELL IS ON")
                    trigger_buzzer()
                    attempts += 1
                    if attempts >= MAX_ATTEMPTS:
                        print("System locked! Reset required.")
                        break

    except KeyboardInterrupt:
        print("Shutting down...")
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
                    print("UNKNOWN FACE DETECTED DOORBELL IS ON")
                    trigger_buzzer()
                    attempts += 1
                    if attempts >= MAX_ATTEMPTS:
                        print("System locked! Reset required.")
                        break

    except KeyboardInterrupt:
        print("Shutting down...")
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
