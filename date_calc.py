# 사용자 입력 기간(string)을 list로 반환

import datetime


def get_date_lst(sd, ed):
    global date_lst
    
    start_date_strp = datetime.datetime.strptime(sd, "%Y%m%d")
    end_date_strp = datetime.datetime.strptime(ed, "%Y%m%d")
    c = 0
    date_lst = []
    output = ""
    while True:
        date_format = start_date_strp + datetime.timedelta(c)
        date_lst.append(date_format.strftime("%Y%m%d"))
        c += 1
        if date_format == end_date_strp:
            return date_lst

def getDateList(sd, ed):

    dateDiff = int(ed) - int(sd)
    sd = datetime.datetime.strptime(sd, "%Y%m%d")    

    dateList = []

    for i in range(dateDiff + 1):
        date = (sd + datetime.timedelta(i)).strftime("%Y%m%d")
        dateList.append(date)
    
    return dateList
sd = "20211015"
ed = "20211019"
print(get_date_lst(sd, ed))
print(getDateList(sd, ed))
