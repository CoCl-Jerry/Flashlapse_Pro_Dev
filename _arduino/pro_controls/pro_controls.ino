#include <TMC2208Stepper.h>
#include <Adafruit_NeoPixel.h>
#include <Wire.h>
#include <avr/wdt.h>

#define DIR_PIN   10
#define STEP_PIN  11
#define EN_PIN    12

#define LED_PIN 6
#define NUM_LEDS 108

#define BUZZER_PIN A8
#define IR_PIN A0
#define FAN_PIN 8

#define SLAVE_ADDRESS 0x08
#define COMMANDSIZE 6

TMC2208Stepper Motor = TMC2208Stepper(&Serial1);
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUM_LEDS, LED_PIN, NEO_GRB + NEO_KHZ800);

char data[50];
int commands[COMMANDSIZE];

int interval = 1;
int currentLimit = 300;
int microstep = 64;
boolean dir = false;

// boolean ms_change = false;

unsigned long NextTime = 0;

void setup() {
  Serial.begin(9600);

  Serial1.begin(115200);
  Motor.push();

  pinMode(IR_PIN, OUTPUT);
  pinMode(FAN_PIN, OUTPUT);
  pinMode(BUZZER_PIN, OUTPUT);

  pinMode(DIR_PIN, OUTPUT);
  pinMode(STEP_PIN, OUTPUT);
  pinMode(EN_PIN, OUTPUT);

  strip.setBrightness(255);
  strip.begin();
  strip.show();

  digitalWrite(EN_PIN, HIGH);   // Disable driver in hardware

  Motor.pdn_disable(true);     // Use PDN/UART pin for communication
  Motor.I_scale_analog(false); // Use internal voltage reference
  Motor.rms_current(currentLimit);      // Set driver current 500mA
  Motor.toff(2);               // Enable driver in software
  Motor.mstep_reg_select(true);
  Motor.microsteps(microstep);
  Motor.dedge(true);

  // digitalWrite(EN_PIN, LOW);   // Disable driver in hardware

  uint32_t data = 0;

  Motor.DRV_STATUS(&data);
  digitalWrite(DIR_PIN, 1);

  Wire.begin(SLAVE_ADDRESS);
  Wire.onReceive(receiveData);

  startup();
  digitalWrite(FAN_PIN, HIGH);
  digitalWrite(IR_PIN, LOW);
}

void loop() {
  // if (ms_change)
  // {
  //   Motor.microsteps(microstep);
  //   ms_change = false;
  // }

  if (micros() < NextTime)
    NextTime = micros();

  if (micros() - NextTime > interval) {
    digitalWrite(STEP_PIN, !digitalRead(STEP_PIN));
    NextTime = micros();         // reset for next pulse
  }
}
