bool isPrime(int num) {
  if (num == 1) return false;
  for (int i = 2; i < num; i++) {
    if (num % i == 0) return false;
  }
  return true;
}

unsigned int calculateChecksum(const unsigned int* data, int length) {
  unsigned long sum = 0;
  for (int i = 0; i < length; i++) {
    sum += data[i];
    while (sum >> 16) {
      sum = (sum & 0xFFFF) + (sum >> 16);
    }
  }
  return ~sum & 0xFFFF;
}

void setup() {
  Serial.begin(9600);
  while (!Serial) {
    ;
  }
  Serial.println("Arduino is ready");
}

void loop() {
  static bool user_input_received = false;
  static int N;
  const int max_primes = 100;
  static unsigned int primes[max_primes];
  static int prime_count = 0;

  if (!user_input_received) {
    if (Serial.available() > 0) {
      N = Serial.parseInt();
      Serial.print("Received N: ");
      Serial.println(N);
      user_input_received = true;
    }
  } else {
    static int current_number = 2;

    while (current_number <= N) {
      if (isPrime(current_number)) {
        if (prime_count < max_primes) {
          primes[prime_count++] = current_number;
        }
      }
      current_number++;
    }

    if (current_number > N) {
      unsigned int checksum = calculateChecksum(primes, prime_count);

      for (int i = 0; i < prime_count; i++) {
        Serial.println(primes[i]);
        delay(100);
      }

      Serial.print("Checksum: ");
      Serial.println(checksum);

      Serial.println("Done!");
      user_input_received = false;
      prime_count = 0;
      current_number = 2;
    }
  }
}
