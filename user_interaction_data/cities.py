
from customer_data import online_advertising


cities = []

for user_data in online_advertising:
 try:
        if user_data['moments_spent_on_internet'] >70:
         cities.append(user_data['city'])
 except TypeError:
   moments_spent_on_internet = str('moments_spent_on_internet')
  
 finally:
   if cities == 'None':
      cities.append(user_data['city'])

print(cities)