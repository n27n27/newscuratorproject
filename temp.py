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


imgObj = PhotoImage(file = "images/holy.png")

       
compLabel = Label(root, image=imgObj, text="이것은 글씨", compound=RIGHT)
# compLabel["image"] = imgObj
# compLabel["text"] = "이것은 글씨"
# compLabel["compound"] = "left"
compLabel.pack()

testCal = Calendar(root, date_pattern = "ymmdd")
print(testCal.get_date())

def ccc():    
    
    for i in range(len(ChkVar)):
        print(ChkVar[i].get())

testButton = Button(root, text="테스트", fg="black", command=ccc)
testButton.place(x=50, y=5)
testButton.pack()
ChkVar = []
abc = Frame(root)
abc.pack()
for i in range(0, 2):
    ChkVar.append(0)
    ChkVar[i] = IntVar()

checkbutton1 = Checkbutton(abc, text="체크1", bg="green", fg="white", selectcolor="green", variable=ChkVar[0]).grid(row=0, column=0)

checkbutton2 = Checkbutton(abc, text="체크1", bg="green", fg="white", selectcolor="green", variable=ChkVar[1]).grid(row=0, column=1)

listFrame = Frame(root)
listFrame.pack()

lists = Listbox(listFrame)
lists.pack(side=LEFT, fill=Y)
scrollbar = Scrollbar(listFrame, command=lists.yview)
scrollbar.pack(side=RIGHT, fill=Y)
lists.config(yscrollcommand=scrollbar.set)
# for x in range(100):
#     text1 = "text" + str(x)
#     label1 = Label(lists, text=text1)
#     lists.insert(END, "")
#     label1.pack()
    
#     # lists.insert(END, str(x))
lists.insert(END, "끝")







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