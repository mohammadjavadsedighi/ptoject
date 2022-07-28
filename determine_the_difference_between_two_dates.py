from datetime import datetime,timedelta
from traceback import print_list

start = datetime.now()

end = start + timedelta(days=30)

between = end - start

print(start)

print(end)

print(between)

print(f'hello you have {int(between.total_seconds())} seconds')

print(int(between.total_seconds() / 86400))