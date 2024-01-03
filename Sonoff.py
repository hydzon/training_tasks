import sonoff

email = 'hydzon@yandex.ru'
password = '37xv07bik'
region = 'eu'

s = sonoff.Sonoff(email, password, region)
devices = s.get_devices()

print(devices[0]["params"]["currentTemperature"])




# s.update_devices()
#
# print(devices[0]["params"]["currentTemperature"])