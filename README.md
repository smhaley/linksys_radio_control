## Linksys Router Radio Toggle

Simple Linksys router radio toggle script.

Configurable to control 2.4mgz and 5mgz radio signals.


## To Run
Currently this is set up to run on the ChromeDriver (chromium or google chrome)

Script has been tested with Google Chrome and the `chromedriver` as well as chromium-browser `chromium-browser-v7` driver on a raspberypi.

- runtime python python `3.7`
- install `requirments.txt`
- set up `config.json` (see `demo_config.json`)
- run `wifi_actions.py` to disable radio
- run `wifi_actions.py --enable` to enable radio

## Note
Running on a raspbery pi is easiest with chromium

Set up the driver and browser with: `sudo apt-get install chromium-chromedriver`




