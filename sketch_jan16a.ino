#include <LiquidCrystal.h>
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

const int switchPin = 6;
int switchState = 0;
int prevSwitchState = 0;
int reply;

void setup() {
  lcd.begin(16, 2);
  lcd.print("Booting");
  pinMode(switchPin, INPUT);

  Serial.begin(9600);
  Serial.println("done");
  lcd.setCursor(0, 1);
  lcd.print("booted");
}

void loop() {
  while (Serial.available()) {
    String in = Serial.readString();
    int pos = in.indexOf(";");
    String loc = in.substring(pos + 1);
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print(in);
    lcd.setCursor(0, 1);
    lcd.print(loc);
    Serial.println("recieved" + in);
  }
}
