from email.mime.nonmultipart import MIMENonMultipart
from case import test_case
from template import make_email_template
from email.mime.text import MIMEText
import smtplib

result = test_case()
print(result)

class Function():
    def save_csv(lst):
        import csv
        import datetime
        path = ""
        file_title = path + datetime.datetime.today().strftime("%Y-%m-%d") + ".csv"
        # file_title = ""
        f = open(file_title, 'w', encoding='utf-8-sig', newline='')
        wr = csv.writer(f)
        
        wr.writerow(["날짜", "섹션", "제목", "신문사", "링크"])
        
        for each in lst:
            wr.writerow(each.values())
        
        f.close()

    def sort_result(lst, terms):
        if terms == "date1":
            return sorted(lst, key=lambda article: (article['date']))
        elif terms == "date2":
            return sorted(lst, key=lambda article: (article['date']), reverse=True)
        elif terms == "category":
            return sorted(lst, key=lambda article: (article['category']))
        elif terms == "newspaper":
            return sorted(lst, key=lambda article: (article['newspaper']))

    def send_email(lst, dates, newspapers, cgs, word, to_email):
        try:
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.set_debuglevel(True)
            MY_GMAIL = ""
            MY_PASSWORD = ""
            s.ehlo()
            s.starttls()
            s.login(MY_GMAIL, MY_PASSWORD)

            msg = MIMENonMultipart("alternative")

            msg.set_charset('utf-8')
            msg['From'] = MY_GMAIL
            msg['To'] = to_email
            msg['subject'] = "TEST_EMAIL"

            template = make_email_template(lst, dates, newspapers, cgs, word)
            body = MIMEText(template, 'html', 'utf-8')

            msg.attach(body)

            s.sendmain(MY_GMAIL, to_email, msg.as_string())
        except Exception as e:
            print("메일 전송 실패")
            print(e)
        finally:
            s.quit()