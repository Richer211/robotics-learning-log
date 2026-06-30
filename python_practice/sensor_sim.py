import time
import random

def read_fake_sensor():
    distance = random.uniform(0.1,5.0)
    return distance

def main():
    print("Starting sensor simulation...")
    while True:
        distance = read_fake_sensor()
        print(f"Distance: {distance:.2f} meters")
        time.sleep(1)

if __name__ == "__main__":
    main()