# 사용자 입력 기간(string)을 list로 반환
def get_date_lst(sd, ed):
    import datetime
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