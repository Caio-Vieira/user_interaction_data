
from customer_data import online_advertising


countries =[]

try:
   for user_data in online_advertising:

     if (user_data['age']) >30:

       countries.append(user_data['country'])

except TypeError:
 age = str('age')

print(countries)