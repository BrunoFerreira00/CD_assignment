// Verify if it's prime
bool isPrime(int num){
  if (num == 1) return false;
  for(int i = 2; i < num; i++){
    if(num % i == 0) return false;
  }
  return true;
}

unsigned int calculateChecksum(int number) {
  unsigned long sum = 0;
  while (number) {
    sum += number & 0xFFFF;
    number >>= 16;
  }
  while (sum >> 16) {
    sum = (sum & 0xFFFF) + (sum >> 16);
  }
  return ~sum & 0xFFFF;
}

void setup() {
  Serial.begin(9600);
  while(!Serial){
    ;
  }
  Serial.println("Arduino is ready");
}

void loop() {
  static bool user_input_received = false;
  static int N;

  if (!user_input_received) {
    // Read the input
    if (Serial.available() > 0) {
      N = Serial.parseInt();
      Serial.print("Received N: ");
      Serial.println(N);
      user_input_received = true;
    }
  } else {
    // Start at the first number
    static int current_number = 2;  

    // Verify if the numbers from 2 to N are prime, if it is, print the number
    while (current_number <= N) {
      if (isPrime(current_number)) {
        unsigned int checksum = calculateChecksum(current_number);
        
        Serial.print("Number: ");
        Serial.print(current_number);
        Serial.print(" checksum: ");
        Serial.println(checksum);
        // Delay between prime numbers
        delay(500);
      }
      current_number++; 
    }

    // Once all prime numbers up to N have been sent, set input to false
    user_input_received = false;
    // Send a confirmation message so the Python script knows all numbers have been sent
    Serial.println("Done!");
    delay(1000);
    exit(0);
  }
}