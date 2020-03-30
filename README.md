# Realtime Serial Plot
Thing to make this work
* upload Realtime-Serial-Plot.ino on Arduino via Arduino IDE
* In `Realtime-Serial-Plot.py`:
  * change port `'COM8'`. You can check port in Arduino IDE (Tools->Port)
  * `dt` should be equal to delay(..) in .ino
  * time_range define time rande for plot
  * NB: reading time form port could be bigger that delay which was set. So verifie this for your computer before trust time-axe
* Run `Realtime-Serial-Plot.py`
