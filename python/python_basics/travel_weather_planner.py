distance_mi = 5
is_raining = False
has_bike = True
has_car = True
has_ride_share_app = True

# Falsy value (0 or None)
if not distance_mi:
    print('False')

# Distance up to 1 mile
elif distance_mi <= 1 and not is_raining:
    print('True')

# Distance between 1 and 6 miles
elif 1 < distance_mi <= 6 and has_bike and not is_raining:
    print('True')

# Distance over 6 miles
elif distance_mi > 6 and (has_car or has_ride_share_app):
    print('True')

# None of above conditions
else:
    print('False')

