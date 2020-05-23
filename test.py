import ephem
import datetime

tokyo = ephem.city('Tokyo')
tokyo.date = datetime.datetime.utcnow()

sun = ephem.Sun()

print("次の東京の日の出時刻: ",ephem.localtime(tokyo.next_rising(sun)))
print("次の東京の日の入り時刻: ",ephem.localtime(tokyo.next_setting(sun)))