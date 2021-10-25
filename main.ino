const int button = 2;

int state = 0;

void setup() {
  Serial.begin(9600);
  pinMode(button, INPUT);
}

void loop() {
  delay(2000);
  state = digitalRead(button);
  if (state == HIGH) {
    Serial.write("toggle");
   }
  
}
