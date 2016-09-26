from __future__ import print_function

from attackoftheorcs_v1_1 import Knight
from gameuniterror import HealthMeterException

if __name__ == '__main__':
    print("Creating a Knight..")
    knight = Knight("Sir Bar")
    # Assume the knight has sustained injuries in the combat
    knight.health_meter = 10
    knight.show_health()
    try:
        knight.heal(heal_by=100, full_healing=False)
    except HealthMeterException as e:
        print(e)
        print(e.error_message)

    knight.show_health()
