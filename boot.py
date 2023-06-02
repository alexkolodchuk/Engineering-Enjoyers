# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()
#cfrom machine import WDT
from time import sleep
#wdt = WDT(timeout=4000)
print("DRONE START IN 3, ", end='')
sleep(1)
print("2, " end='')
sleep(1)
print("1")
sleep(1)
#wdt.feed()