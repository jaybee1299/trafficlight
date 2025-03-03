#define LED_PIN_1 11  // Pin for LED 1 (Friday)
#define LED_PIN_2 10  // Pin for LED 2 (Saturday)
#define LED_PIN_3 9   // Pin for LED 3 (Sunday)

void setup() {
  pinMode(LED_PIN_1, OUTPUT);
  pinMode(LED_PIN_2, OUTPUT);
  pinMode(LED_PIN_3, OUTPUT);
  Serial.begin(9600);  // Initialize serial communication
}

void loop() {
  if (Serial.available() > 0) {  // Check if a command has been received
    char command = Serial.read();  // Read the serial command

    if (command == '1') {
      digitalWrite(LED_PIN_1, HIGH);
      digitalWrite(LED_PIN_2, LOW);
      digitalWrite(LED_PIN_3, LOW);
      Serial.println("LED 1 (Friday) turned ON");
    } 
    else if (command == '2') {
      digitalWrite(LED_PIN_1, LOW);
      digitalWrite(LED_PIN_2, HIGH);
      digitalWrite(LED_PIN_3, LOW);
      Serial.println("LED 2 (Saturday) turned ON");
    }
    else if (command == '3') {
      digitalWrite(LED_PIN_1, LOW);
      digitalWrite(LED_PIN_2, LOW);
      digitalWrite(LED_PIN_3, HIGH);
      Serial.println("LED 3 (Sunday) turned ON");
    }
    else if (command == '0') {
      digitalWrite(LED_PIN_1, LOW);
      digitalWrite(LED_PIN_2, LOW);
      digitalWrite(LED_PIN_3, LOW);
      Serial.println("All LEDs turned OFF");
    }
  }
}
