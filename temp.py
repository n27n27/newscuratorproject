from tkinter import *
from babel.dates import DateTimePattern
from tkcalendar import Calendar
import pyautogui
from datetime import *
#  객체생성
root = Tk()
# 제목설정
root.title("News Curator")
# 화면크기 설정
root.geometry("300x200")
# 화면크기 변경 안됨
root.resizable(False, False)
# 배경화면 녹색
root.configure(bg="green")

testCal = Calendar(root, date_pattern = "ymmdd")
print(testCal.get_date())

testButton = Button(root, text="테스트", fg="black")
testButton.place(x=50, y=5)
testButton.pack()


def modalTest():
    root.wm_attributes("-disabled", True)    
    modalWindow = Toplevel(root)
    
    modalWindow.geometry("300x200")
    
    modalWindow.transient(root)
    modalLabel = Label(modalWindow, text="종료날짜가 시작날짜 이전입니다. 다시 선택해주세요")
    modalLabel.pack(side="top")
    modalButton = Button(root, text="모달테스트", fg="black", command=modalTest)
    modalButton.pack()
    
root.mainloop()