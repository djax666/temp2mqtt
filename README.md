# temp2mqtt
Send cpu temperature of a raspberry pi over mqtt for home assistant

Edit the **config.py** file and correct your mqtt server.

Run the **temp2mqtt_declaration.py** once.
Edit crontab with **crontab -e** and add this line:
````
*/1 *  *   *   *     /home/pi/temp2mqtt/temp2mqtt.py
````
It will update the temperature every minute.
