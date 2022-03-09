#include <Arduino.h>
#include <Adafruit_NeoPixel.h>

#define LED_COUNT 30
#define LED_PIN 22
#define LED_LEFT 14
#define LED_RIGHT 15

Adafruit_NeoPixel strip(LED_COUNT, LED_PIN, NEO_GRB + NEO_KHZ800);

void setup() {
  strip.begin();
  strip.show();
  strip.setBrightness(10);
  pinMode(LED_LEFT, OUTPUT);
  pinMode(LED_RIGHT, OUTPUT);
}

void rainbow(int wait) {
  for(long firstPixelHue = 0; firstPixelHue < 5*65536; firstPixelHue += 256) {
    for(int i=0; i<strip.numPixels(); i++) { 
      int pixelHue = firstPixelHue + (i * 65536L / strip.numPixels());
      strip.setPixelColor(i, strip.gamma32(strip.ColorHSV(pixelHue)));
    }
    strip.show();
    delay(wait);
  }
}

void loop() {
  analogWrite(LED_RIGHT, 20);
  delay(1000);
  analogWrite(LED_LEFT, 20);
  rainbow(20);
}