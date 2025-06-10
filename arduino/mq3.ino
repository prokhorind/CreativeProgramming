#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_RESET -1
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

#define MQ3_PIN A0

unsigned long lastUpdate = 0;
const unsigned long updateInterval = 3000; // Update every 1 sec
int lastSensorValue = -1;  // Store previous sensor reading

void drawProgressBar(int x, int y, int w, int h, int progress) {
  display.drawRect(x, y, w, h, SSD1306_WHITE);
  int fillWidth = map(progress, 0, 1023, 0, w);
  display.fillRect(x + 1, y + 1, fillWidth - 2, h - 2, SSD1306_WHITE);
}

void setup() {
  Serial.begin(9600);
  Wire.begin();
  Wire.setClock(400000);

  if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    Serial.println(F("SSD1306 allocation failed, retrying..."));

    Wire.end();
    delay(500);
    Wire.begin();
    if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
      Serial.println(F("OLED failed, halting"));
      while (true);
    }
  }

  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(0, 0);
  display.println("Alcohol Tester");
  display.display();
  delay(2000);
}

void loop() {
  // **Auto-Recover Display If Disconnected**
  if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    Serial.println(F("OLED disconnected, reinitializing..."));
    Wire.end();
    delay(500);
    Wire.begin();
    display.begin(SSD1306_SWITCHCAPVCC, 0x3C);
    display.clearDisplay();
    display.display();
  }

  // **Only update when needed**
  if (millis() - lastUpdate > updateInterval) {
    lastUpdate = millis();

    int sensorValue = analogRead(MQ3_PIN);

    // **Prevent Unnecessary Screen Updates**
    if (abs(sensorValue - lastSensorValue) < 5) {
      return; // Skip update if value is nearly the same
    }

    lastSensorValue = sensorValue;

    display.clearDisplay();
    display.setCursor(0, 0);
    display.setTextSize(2);
    display.print("Sensor: ");
    display.setTextSize(1);
    display.println(sensorValue);

    drawProgressBar(0, 16, SCREEN_WIDTH, 10, sensorValue);

    display.setTextSize(1);
    display.setCursor(0, 32);
    if (sensorValue < 100) {
      display.println("Status: Sober");
    } else if (sensorValue < 200) {
      display.println("Status: Tipsy :)");
    } else if (sensorValue < 350) {
      display.println("Status: Drunk :P");
    } else if (sensorValue < 500) {
      display.println("Status: Wasted :O");
    } else {
      display.println("Status: Blackout X");
    }

    display.display();
    Serial.print("Sensor Value: ");
    Serial.println(sensorValue);
  }
}
