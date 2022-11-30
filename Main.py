import phonenumbers
from phonenumbers import geocoder,carrier,timezone

number = phonenumbers.parse("+628524314394")

region = geocoder.description_for_number(number, 'en')
service_provider = carrier.name_for_number(number, 'en')
valid = phonenumbers.is_valid_number(number)
possibel = phonenumbers.is_possible_number(number)
timezone = timezone.time_zones_for_number(number)

print(number)
print(service_provider)
print(region)
print(valid)
print(possibel)
print(timezone)