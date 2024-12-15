int ledpin = 13; 
void setup ()
{
  Serial.begin (9600); // com port speed
  Serial.println ("App setup "); 
  delay(100);
}

void loop ()
{
digitalWrite (ledpin, HIGH); 
delay (1000);
digitalWrite (ledpin, LOW);
Serial.println ("Hello World!"); 
}