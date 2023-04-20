
from customer_data import online_advertising

income =  []

try:

 for user_data in online_advertising:

  if(user_data['clicked_on_ad']) ==1:

    income.append(user_data['rent_area'])

except KeyError:

    clicked_on_ad = str('clicked_on_ad')

print(income)


