import serial
import time

# Serial port configuration
# COM value needs to be changed according to the port the Arduino is connected to on the Arduino IDE
ser = serial.Serial('COM5', 9600)  

def send_N(N):
    ser.write(str(N).encode())
    time.sleep(0.1)

def receive_primes():
    while True:
        line = ser.readline().decode().strip()
        if line:
            print("Received:", line)
            if line == "Done!":
                print("All prime numbers received.")
                break
            

def main():
    N = int(input("Enter the value of N: ")) 
    send_N(N)
    print("Waiting for prime numbers from the Arduino...")
    receive_primes()
    ser.close()

if __name__ == "__main__":
    main()
