"""
<문제>
서울의 오늘 날짜를 출력하는 프로그램을 작성하시오.

<입력>
입력은 없다.

<출력>
서울의 오늘 날짜를 "YYYY-MM-DD" 형식으로 출력한다.
"""

from datetime import datetime, timezone, timedelta

#import pytz | 아니 pytz 못쓰는거야 ㅅㅂ?

#print(datetime.datetime.now(pytz.timezone('Asia/Seoul')).strftime("%Y-%m-%d"))

print(datetime.now(timezone(timedelta(hours=9))).strftime("%Y-%m-%d"))