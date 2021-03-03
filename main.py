import logging
import traceback
from datetime import datetime
from timesheet import clocker
from playsound import playsound
from config import clock_in_id,clock_out_id,meal_start_id,meal_end_id

logging.basicConfig(filename='.\\auto_clocker.log', filemode='a', 
format='%(name)s - %(ascitime)s - %(message)s')

logger = logging.getLogger()

""" Script that clocks me into work based on what time it is. """
now = datetime.now()

current_time = now.strftime("%H:%M")

if current_time == '08:00':
    try:
        clocker(clock_in_id)
    else:
        playsound('Apple Pay Success Sound Effect.mp3')
    except:
        playsound('XP Critical Error Sound Effect.mp3')
        logger.error(traceback.format_exc())
    
elif current_time =='12:00':
    try:
        clocker(meal_start_id)
    else:
        playsound('Apple Pay Success Sound Effect.mp3')
    except:
        playsound('XP Critical Error Sound Effect.mp3')
        logger.error(traceback.format_exc())

elif current_time == '13:00':
    try:
        clocker(meal_end_id)
    else:
        playsound('Apple Pay Success Sound Effect.mp3')
    except:
        playsound('XP Critical Error Sound Effect.mp3')
        logger.error(traceback.format_exc())
        
elif current_time == '17:00':
    try:
        clocker(clock_out_id)
    else:
        playsound('Apple Pay Success Sound Effect.mp3')
    except:
        playsound('XP Critical Error Sound Effect.mp3')
        logger.error(traceback.format_exc())
    
