"""
Handling date and time is often notorious in data analysis and handling
arrow module can simplify it

"""

import arrow
import pytz
utc = arrow.utcnow()
local = utc.to('US/Pacific')
chennai = utc.to('Asia/Kolkata')

print(local.format('YYYY-MM-DD HH:mm:ss'))
print(chennai.format('YYYY-MM-DD HH:mm:ss'))

# Get a list of all time zones
all_timezones = pytz.all_timezones

# Print the list of time zones
for timezone in all_timezones:
    print(timezone)
