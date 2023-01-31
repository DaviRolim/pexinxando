import math
offer_price = 152
current_price = 319.50
difference = abs(offer_price - current_price)
print(difference)
ratio2 = (offer_price + current_price) / 2
print(ratio2)
percentage_difference = (difference / ratio2) * 100
discount = math.floor(percentage_difference)
print(discount)