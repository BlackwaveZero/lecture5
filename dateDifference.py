import datetime
def dateDiff(date1,date2):
    date1=datetime.datetime.strptime(date1,"%Y-%m-%d %H:%M:%S")
    date2=datetime.datetime.strptime(date2,"%Y-%m-%d %H:%M:%S")
    return date1-date2
print(dateDiff(input(),input()))
