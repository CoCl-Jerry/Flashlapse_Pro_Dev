void motorStatus() {
  digitalWrite(EN_PIN, commands[2]);
}

void dirUpdate() {
  digitalWrite(DIR_PIN, commands[2]);
}

void setDir(bool mot) {
  if (mot)
    digitalWrite(DIR_PIN, commands[2]);

}

void setMotor() {
  microstep = commands[2];
  interval = commands[3];
  
  ms_change = true;
}
