from datetime import datetime

data_str = "2023-07-08 22:16:38"
data_str_fmt = "%Y-%m-%d %H:%M:%S"
data = datetime(2023, 4, 20)
time = datetime(2023, 4, 20, 7, 23, 2)
datastr = datetime.strptime(data_str, data_str_fmt)
print(datetime.now())
print(data)
print(time)
print(datastr)
data = datetime.now()
print(data.timestamp())
print(datetime.fromtimestamp(1688926343.44536))
fmt = '%d/%m/%Y'
print(datastr.strftime(fmt))
