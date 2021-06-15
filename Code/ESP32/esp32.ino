#include "BluetoothSerial.h"
#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth is not enabled! Please run `make menuconfig` to and enable it
#endif
int i;
int servomotor = 26;
int PirPin = 25;
float waarde;
BluetoothSerial SerialBT;
// Handle received and sent messages
String message = "";
char incomingChar;
String ledon = "led_on";
String ledoff = "led_off";

bool statusPir;

void setup() {
  pinMode(servomotor, OUTPUT);

  pinMode(PirPin, INPUT_PULLUP);
  Serial.begin(115200);
  // Bluetooth device name
  SerialBT.begin("esp"); // ------------------------------------------------------------------------------------------------------
  Serial.println("The device started, now you can pair it with bluetooth!");
}
void loop() {
  // Read received messages (LED control command)
  statusPir = digitalRead(PirPin);
  if (SerialBT.available()) {

    char incomingChar = SerialBT.read();
    if (incomingChar != '\n') {
      message += String(incomingChar);
    }
    else {
      message = "";
    }
    Serial.write(incomingChar);
    // Check received message and control output accordingly
    if (message == "gesloten") {
      graden(omrekenen(180));
      message = "";
    }
    if (message == "open") {
      graden(omrekenen(90));
      message = "";
    }
    if (message == "opgeslo") {
      graden(omrekenen(1));
      message = "";
    }
    if (message == "pir") {
      delay(500);
      if (statusPir == 0) {
        SerialBT.write('D');
      }
      if (statusPir == 1) {
        SerialBT.write('T');
      }
      message = "";
    }
  }
  delay(100);
}

int graden(int cijfer) {
  for (i = 0; i < 200; i++ )  {
    digitalWrite(servomotor, HIGH);
    delayMicroseconds(cijfer);
    digitalWrite(servomotor, LOW);
    delayMicroseconds(20000 - cijfer);
  }
}
float omrekenen(int graden) {
  return (((graden / 56.84) + 1) * 600);

}