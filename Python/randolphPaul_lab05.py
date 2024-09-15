# Randolph Paul 3/26/2024 randolphPaul_lab05
"""The purpose of this program is to rewrite the number of
seconds a user gives it into days, hours, minutes, and seconds."""

# declare constants
day_conversion = 86400
hour_conversion = 3600
minute_conversion = 60
zero = 0

# Get the number of seconds from the user
print('''\nThis program rewrites the number of seconds 
a user gives it into days, hours, minutes, and seconds.''')
seconds = int(input("\nPlease enter the number of seconds: "))

# Calculate days, hours, minutes, and remaining seconds
days = seconds // day_conversion
seconds %= day_conversion
hours = seconds // hour_conversion
seconds %= hour_conversion
minutes = seconds // minute_conversion
seconds %= minute_conversion

# Display the result
if days > zero:
    print(f"{days:,} day/s, {hours} hour/s, {minutes} minute/s, {seconds} second/s")
elif hours > zero:
    print(f"{hours} hour/s, {minutes} minute/s, {seconds} second/s")
elif minutes > zero:
    print(f"{minutes} minute/s, {seconds} second/s")
else:
    print(f"{seconds} second/s")
