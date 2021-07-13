## First Exercise ##

temps = [222, 225, 124, 125]

new_temps = [temp/10 for temp in temps]

print(new_temps)

## Second Exercise - if in list comprehension ##
temps = [222, 225, 124, 125, -9999]

new_temps = [temp/10 for temp in temps if temp != -9999]

print(new_temps)

## Third Exercise - if else in list comprehension ## 

temps = [222, 225, 124, 125, -9999]

new_temps = [temp/10 if temp != -9999 else 0 for temp in temps]

print(new_temps)