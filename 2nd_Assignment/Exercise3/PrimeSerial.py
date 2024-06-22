import serial
import time

ser = serial.Serial('COM5', 9600)

def send_N(N):
    ser.write(str(N).encode())
    time.sleep(0.5)

def calculate_checksum(data):
    sum = 0
    for number in data:
        sum += number
        while sum >> 16:
            sum = (sum & 0xFFFF) + (sum >> 16)
    return ~sum & 0xFFFF

def receive_primes():
    primes = []
    while True:
        line = ser.readline().decode().strip()
        if line:
            print("Received:", line)
            if line == "Done!":
                print("All prime numbers received.")
                break
            elif line.startswith("Checksum: "):
                received_checksum = int(line.split()[1])
                calculated_checksum = calculate_checksum(primes)
                if received_checksum == calculated_checksum:
                    print(f"Checksum valid: {received_checksum}")
                else:
                    print(f"Checksum mismatch: received {received_checksum}, calculated {calculated_checksum}")
                primes = []
            else:
                try:
                    number = int(line)
                    primes.append(number)
                except ValueError:
                    print("Invalid input received")

def main():
    N = int(input("Enter the value of N: ")) 
    time.sleep(2)
    send_N(N)
    print("Waiting for prime numbers from the Arduino...")
    receive_primes()
    ser.close()

if __name__ == "__main__":
    main()
