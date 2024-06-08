import serial
import time

# Serial port configuration
# COM value needs to be changed according to the port the Arduino is connected to on the Arduino IDE
ser = serial.Serial('COM5', 9600)  

def send_N(N):
    ser.write(str(N).encode())
    time.sleep(0.5)


# Function to calculate the checksum of a number
def calculate_checksum(number):
    sum = 0
    while number:
        sum += number & 0xFFFF
        number >>= 16
    while sum >> 16:
        sum = (sum & 0xFFFF) + (sum >> 16)
    return ~sum & 0xFFFF


def receive_primes():
    count = 0
    while True:
        # Read a line from the serial port
        line = ser.readline().decode().strip()
        if line:
            print("Received:", line)
            # Check if the line is the end of the transmission
            if line == "Done!":
                print("All prime numbers received.")
                break
            # Check whenever a number is received , so it calcs the checksum and compares it with the received checksum
            # Also this block only runs on the arduino code that sends his checksum to the receiver
            # Otherwise it will stop at the block above at break
            if line.startswith("Number: "):
                try:
                    parts = line.split()
                    number_str = parts[1]
                    checksum_str = parts[3]
                    number = int(number_str)
                    checksum = int(checksum_str)

                    count += 1
                    if count % 5 == 0:
                        number += 1
                    
                    calculated_checksum = calculate_checksum(number)

                    # This block of code is used to force a checksum mismatch every 5
                    

                    if calculated_checksum == checksum:
                        print(f"Received: {number} with valid checksum {checksum}")
                    else:
                        print(f"Checksum mismatch for number {number}: received {checksum}, calculated {calculated_checksum}")
                
                except (ValueError, IndexError):
                    print("Invalid input received")
                    
def main():
    N = int(input("Enter the value of N: ")) 
    # To make sure the Arduino is ready
    time.sleep(2)
    send_N(N)
    print("Waiting for prime numbers from the Arduino...")
    receive_primes()
    ser.close()

if __name__ == "__main__":
    main()
