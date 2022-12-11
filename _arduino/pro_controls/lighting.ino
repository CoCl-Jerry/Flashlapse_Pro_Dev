void stripUpdate() {
  for (uint16_t i = 0; i < strip.numPixels(); i++) {
    if (i >= commands[2] && i < commands[3]) {
      strip.setPixelColor(i, int(commands[4]), int(commands[5]), int(commands[6]));
    }
  }
  strip.setBrightness(int(commands[7]));
  strip.show();
}

void brightnessUpdate() {
  strip.setBrightness(int(commands[2]));
  strip.show();
}

void stripClear() {
  strip.clear();
  strip.show();
}

void stripShow() {
  strip.show();
}

void infraOn() {
  digitalWrite(IR_PIN, HIGH);
}

void infraOff() {
  digitalWrite(IR_PIN, LOW);
}

void colorWipe(uint32_t color, int wait) {
  for (int i = 0; i < strip.numPixels(); i++) {  // For each pixel in strip...
    strip.setPixelColor(i, color);               //  Set pixel's color (in RAM)
    strip.show();                                //  Update strip to match
    delay(wait);                                 //  Pause for a moment
  }
}

void rainbow() {
  for (long firstPixelHue = 0; firstPixelHue < 65536; firstPixelHue += 256) {
    strip.rainbow(firstPixelHue);
    strip.show();
  }
}