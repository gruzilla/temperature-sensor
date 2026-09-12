import time
import board
import digitalio
import adafruit_max31865

# Gemeinsamer SPI-Bus
spi = board.SPI()

# Drei getrennte Chip-Select-Leitungen
cs1 = digitalio.DigitalInOut(board.D5)    # GPIO5, physical Pin 29
cs2 = digitalio.DigitalInOut(board.D6)    # GPIO6, physical Pin 31
cs3 = digitalio.DigitalInOut(board.D13)   # GPIO13, physical Pin 33


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
        d1 = sensor1.read_rtd()
        t1 = sensor1.temperature
        r1 = sensor1.resistance
        f1 = sensor1.fault

        d2 = sensor2.read_rtd()
        t2 = sensor2.temperature
        r2 = sensor2.resistance
        f2 = sensor2.fault

        d3 = sensor3.read_rtd()
        t3 = sensor3.temperature
        r3 = sensor3.resistance
        f3 = sensor3.fault

        print(
            f"Sensor 1: {t1:7.2f} °C   {r1:8.3f} Ω   F:{f1}   R:{d1}   | "
            f"Sensor 2: {t2:7.2f} °C   {r2:8.3f} Ω   F:{f2}   R:{d2}   | "
            f"Sensor 3: {t3:7.2f} °C   {r3:8.3f} Ω   F:{f3}   R:{d3}"
        )

    except Exception as e:
        print(f"Fehler beim Auslesen: {e}")

    time.sleep(2)