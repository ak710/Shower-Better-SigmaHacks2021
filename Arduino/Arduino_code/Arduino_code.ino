#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>

ESP8266WebServer server(80);
server.on("/Python", handlePath);  
int speedPin = 5; 
int dir1 = 3;
int dir2 = 2;
int time = 5; //time in seconds


void setup() {

Serial.begin(115200);
pinMode(speedPin, OUTPUT);
pinMode(dir1, OUTPUT);
pinMode(dir2, OUTPUT);
WiFi.begin("Akshat's Room", "Password");  //Connect to the WiFi network

while (WiFi.status() != WL_CONNECTED) {  //Wait for connection

delay(500);
Serial.println("Waiting to connect…");

}

Serial.print("IP address: ");
Serial.println(WiFi.localIP());                         //Print the local IP of the webserver

server.on("/Python", handlePath);              //Associate the handler function to the path
server.begin();                                                   //Start the server
Serial.println("Server listening");

}

void loop() {

server.handleClient(); //Handling of incoming requests

}

void handlePath() { //Handler for the path

time = time*100;
delay (time);
digitalWrite(dir1, LOW);
digitalWrite(dir2, HIGH);
for (int i=0;i<=255;i++) 
  {
    analogWrite(speedPin,i);
    delay(40);
  }
analogWrite(speedPin, 0);

}
