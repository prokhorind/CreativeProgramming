#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_RESET -1
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

#define MQ3_PIN A0

unsigned long lastUpdate = 0;
const unsigned long updateInterval = 1000;  // Update every 1 second
int lastSensorValue = -1;  // Store previous sensor reading

// Function to draw progress bar
void drawProgressBar(int x, int y, int w, int h, int progress) {
  display.drawRect(x, y, w, h, SSD1306_WHITE);
  int fillWidth = map(progress, 0, 1023, 0, w);
  display.fillRect(x + 1, y + 1, fillWidth - 2, h - 2, SSD1306_WHITE);
}

// **Setup Function: Initializes Display & Sensor**
void setup() {
  Serial.begin(9600);
  Wire.begin();
  Wire.setClock(400000);  // Boost I2C speed for stability

  if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    Serial.println(F("Display failed, retrying..."));

    Wire.end();  // Reset I2C
    delay(500);
    Wire.begin();  // Restart I2C

    if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
      Serial.println(F("OLED failed, stopping"));
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

  if (millis() - lastUpdate > updateInterval) {
    lastUpdate = millis();

    int sensorValue = analogRead(MQ3_PIN);

    Serial.print("Sensor Value: ");
    Serial.println(sensorValue);

    // Prevent unnecessary updates if sensor value barely changes
    if (abs(sensorValue - lastSensorValue) < 5) {
      return;
    }
    lastSensorValue = sensorValue;

    // **Instead of clearing the entire screen, overwrite sections**
    display.fillRect(0, 0, SCREEN_WIDTH, 12, SSD1306_BLACK); // Clear sensor text smoothly
    display.setCursor(0, 0);
    display.setTextSize(1);
    display.print("Sensor: ");
    display.setTextSize(2);
    display.println(sensorValue);

    drawProgressBar(0, 16, SCREEN_WIDTH, 10, sensorValue);

    display.fillRect(0, 32, SCREEN_WIDTH, 32, SSD1306_BLACK); // Clear status text smoothly
    display.setTextSize(1);
    display.setCursor(0, 32);
    display.println("Status:");
    display.setTextSize(2);
    if (sensorValue < 500) {
      display.println("Sober");
    } else if (sensorValue < 650) {
      display.println("Tipsy :)");
    } else if (sensorValue < 750) {
      display.println("Drunk :P");
    } else if (sensorValue < 850) {
      display.println("Wasted :O");
    } else {
      display.println("Blackout X");
    }

    display.display();
  }
}

