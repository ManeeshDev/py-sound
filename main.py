from datetime import date
from sound import Sound

print("")
print("Windows Sound Manager (Python 3)")
print("Copyright (c) 2014 - %d | Paradoxis" % date.today().year)
print("")

try:
    print("trying....")
    print("Sound muted    | %s" % str(Sound.is_muted()))
    print("----------------------")

    if ((not Sound.is_muted())):
        Sound.mute()
        Sound.volume_set(50)

    print("Current volume | %s" % str(Sound.current_volume()))

except:
    print("An exception occurred")
