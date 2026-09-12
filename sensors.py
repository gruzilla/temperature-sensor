import time
import board
import digitalio
import adafruit_max31865

# Gemeinsamer SPI-Bus
spi = board.SPI()

# Drei getrennte Chip-Select-Leitungen
cs1 = digitalio.DigitalInOut(board.D8)   # GPIO8, physical Pin 24
cs2 = digitalio.DigitalInOut(board.D7)   # GPIO7, physical Pin 26
cs3 = digitalio.DigitalInOut(board.D5)   # GPIO5, physical Pin 29


# ------------------------------------------------------------
# Board 1 (Noname PT100)
# PT100
# MAX31865 mit RREF = 430 Ohm
# ------------------------------------------------------------
sensor1 = adafruit_max31865.MAX31865(
    spi,
    cs1,
    wires=3,
    rtd_nominal=100.0,
    ref_resistor=430.0
)


# ------------------------------------------------------------
# Board 2 (Noname PT100)
# PT100
# MAX31865 mit RREF = 430 Ohm
# ------------------------------------------------------------
sensor2 = adafruit_max31865.MAX31865(
    spi,
    cs2,
    wires=3,
    rtd_nominal=100.0,
    ref_resistor=430.0
)


# ------------------------------------------------------------
# Board 3 (Adafruit PT1000/PT100)
# PT100
# MAX31865 mit RREF = 4300 Ohm
#
# Wichtig:
# Der Sensor selbst ist weiterhin PT100 -> rtd_nominal = 100
# Nur der Referenzwiderstand dieses Boards ist 4300 Ohm.
# ------------------------------------------------------------
sensor3 = adafruit_max31865.MAX31865(
    spi,
    cs3,
    wires=3,
    rtd_nominal=100.0,
    ref_resistor=4300.0
)


while True:
    try:
        t1 = sensor1.temperature
        r1 = sensor1.resistance

        t2 = sensor2.temperature
        r2 = sensor2.resistance

        t3 = sensor3.temperature
        r3 = sensor3.resistance

        print(
            f"Sensor 1: {t1:7.2f} °C   {r1:8.3f} Ω | "
            f"Sensor 2: {t2:7.2f} °C   {r2:8.3f} Ω | "
            f"Sensor 3: {t3:7.2f} °C   {r3:8.3f} Ω"
        )

    except Exception as e:
        print(f"Fehler beim Auslesen: {e}")

    time.sleep(2)