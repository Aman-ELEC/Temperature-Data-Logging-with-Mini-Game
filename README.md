# Temperature-Data-Logging-with-Mini-Game
Graphed temperature in real-time on a stripchart. Option to play a mini-game if one touched the sensor.

- Coded a project in C that read analog inputs of an external analog to digital converter (ADC) using a serial peripheral interface (SPI)
- Utilized an MCP3008 as the ADC with an LM335 temperature sensor interfaced with a PIC32-microcontroller
- Applied a python script to open the serial port in the host computer and constantly read the received temperature value
- Affixed code that displayed a stripchart that plotted temperature in real-time
- Created a mini-game that if one were to raise the temperature over 25 degrees Celsius, they would trigger a game where they would have to stay between 25 to 26 degrees to continue playing
- Encompassed a feature that if the temperature were to go out of bounds during the mini-game, flashing disco lines would appear on the stripchart at each reading to provide an aesthetic attribute
- Wired blue, red, and yellow LEDs to indicate whether the climate was cold, hot, or at room temperature respectively
