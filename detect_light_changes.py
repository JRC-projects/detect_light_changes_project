import time
import logging
import os, sys
try:
    # Transitional fix for breaking change in LTR559
    from ltr559 import LTR559
    ltr559 = LTR559()
except ImportError:
    import ltr559


logging.basicConfig(
    format='%(asctime)s.%(msecs)03d %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

logging.info("""light.py - Monitoring Light sensor.
Press Ctrl+C to exit!
""")


def light_list_compare(light_level, light_list):
    """ Returns bool, true if light is out of range, false if not"""
    if len(light_list) <= 5:
        return False # not yet enough values
    
    fixing_factor = 2 

    min_light = min(light_list)
    max_light = max(light_list)*fixing_factor

    if light_level > max_light:
        output_bool = True
    else:
        output_bool = False

    return output_bool


def do_something_print():
    print("oi who's that, turn that light off!!!")
    return None


def do_something_play_sound():

    sound_file = "./shreck_annoying.mp3"
    # os.system(f"omxplayer -o hdmi {sound_file}")
    os.system("omxplayer -o local shreck_annoying.mp3")




def main_fun():
        
    lux_list = []

    try:
        while True:
            lux = ltr559.get_lux()
            
            logging.info("""Light: {:05.02f} Lux""".format(lux))
            time.sleep(1.0)
            
            # Compare current value to historic list
            if light_list_compare(lux,lux_list):
                do_something_print()
                do_something_play_sound()

            lux_list.append(lux)

            if len(lux_list) >= 10:
                lux_list = lux_list[1:10] # removes first value if list is 10 long (or longer)


    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main_fun()




