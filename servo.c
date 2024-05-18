#include <Servo.h>

Servo servo1;
Servo servo2;
int angle;

void setup() {
  Serial.begin(9600);
  servo1.attach(7); // 서보모터 핀
  servo2.attach(9);
}

void loop() {
  if (Serial.available() > 0) {
    angle = Serial.parseInt();
    servo1.write(angle);
    servo2.write(angle);
    delay(500);  // 0.5초 대기
  }
}
