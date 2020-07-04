import datetime
now = datetime.datetime.now()
month = now.month

if month in [3, 4, 5]:
    season = "봄"
elif month in [6, 7, 8]:
    season = "여름"
elif month in [9, 10, 11]:
    season = "가을"
else:
    season="겨울"

print("현재는 {0}입니다.".format(season))
