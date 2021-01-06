from datetime import datetime
from timesheet import clocker
from config import clock_in_id,clock_out_id,meal_start_id,meal_end_id

# Add SMTP logging in the future.
""" Script that clocks me into work based on what time it is. """
now = datetime.now()

current_time = now.strftime("%H:%M")

if current_time == '08:00':
    clocker(clock_in_id)
    pass

elif current_time =='12:00':
    clocker(meal_start_id)
    pass

elif current_time == '13:00':
    clocker(meal_end_id)
    pass

elif current_time == '17:00':
    clocker(clock_out_id)
    pass
    
