from tkinter import *
from tkcalendar import Calendar
# 객체생성
root = Tk()
# 제목설정
root.title("News Curator")
# 화면크기 설정
root.geometry("1100x800")
# 화면크기 변경 안됨
root.resizable(False, False)
# 배경화면 녹색
root.configure(bg="green")

## header frame
headerFrame = Frame(root, bg="green")

# new curator label
newCuratorLabel = Label(headerFrame, text="뉴스 큐레이터", width=80, fg="white", bg="green", anchor=W, font='Helvetica 20 bold')
newCuratorLabel.pack(fill="x", side="left")

# login frame
logInFrame = Frame(headerFrame)
logInFrame.pack(fill="x")
# 아이디
idLabel = Label(logInFrame, text="아이디", width=10, fg="white", bg="green", font=15, padx=3)
idLabel.pack(side="left")
idEntry = Entry(logInFrame, width=15, font=15)
idEntry.pack(side="left")
# 비번
pwEntry = Entry(logInFrame, width=15, font=15)
pwLabel = Label(logInFrame, width=10, text="비밀번호", fg="white", bg="green", font=15, padx=3)
pwEntry.pack(side="right")
pwLabel.pack(side="right")
logInFrame.place(x=600, y=12)
headerFrame.pack(fill="x", padx=5, pady=5, ipadx=10, ipady=10)

# 신문사
newsFrame = Frame(root, bg="green", highlightcolor="white", highlightthickness=2)
news_var = StringVar()
# 조선
radioChosun = Radiobutton(newsFrame, width=15, font=15, text="조선일보", value="조선일보", bg="green", fg="white", variable=news_var, pady=15).grid(row=0, column=0)
# 중앙
radioJungang = Radiobutton(newsFrame, width=15, font=15, text="중앙일보", value="중앙일보", bg="green", fg="white", variable=news_var).grid(row=0, column=1)
# 동아
radioDonga = Radiobutton(newsFrame, width=15, font=15, text="동아일보", value="동아일보", bg="green", fg="white", variable=news_var).grid(row=0, column=2)
# 한겨레
radioHan = Radiobutton(newsFrame, width=15, font=15, text="한겨레", value="한겨레", bg="green", fg="white", variable=news_var).grid(row=0, column=3)
# 경향
radioKyung = Radiobutton(newsFrame, width=15, font=15, text="경향", value="경향", bg="green", fg="white", variable=news_var).grid(row=0, column=4)

newsFrame.pack(pady=5)
newsFrame.place(x=10, y=70)

# 섹션
sectionFrame = Frame(root, bg="green", highlightthickness=2, highlightcolor="white")
section_var = StringVar()
# 사회
radioSociety = Radiobutton(sectionFrame, width=15, font=15, text="사회", value="사회", bg="green", fg="white", variable=section_var, pady=15).grid(row=0, column = 0)
# 정치
radioPolitics = Radiobutton(sectionFrame, width=15, font=15, text="정치", value="정치", bg="green", fg="white", variable=section_var).grid(row=0, column = 1)
# 경제
radioEconomy = Radiobutton(sectionFrame, width=15, font=15, text="경제", value="경제", bg="green", fg="white", variable=section_var).grid(row=0, column = 2)
# IT/과학
radioIT = Radiobutton(sectionFrame, width=15, font=15, text="IT", value="IT", bg="green", fg="white", variable=section_var).grid(row=0, column = 3)
# sports
radioSports = Radiobutton(sectionFrame, width=15, font=15, text="스포츠", value="스포츠", bg="green", fg="white", variable=section_var).grid(row=0, column = 4)
sectionFrame.pack(pady=5)
sectionFrame.place(x=10, y=140)

# 광고 프레임
adFrame = Frame(root, bg="green", highlightthickness=2, highlightcolor="white")
adLabel=Label(adFrame, width=7, text="광고삽입", font='Helvetica 35 bold', fg="white", bg="green", anchor=CENTER, pady=50, padx=5)
adLabel.pack()
adFrame.pack(pady=5)
adFrame.place(x=860, y=70)

# 검색 프레임
searchFrame = Frame(root, bg="green")
startCount = 0
endCount = 0

def startCal():    
    global startCal
    global startCount    
    if startCount == 1:
        startCount = 0
        startCal.place_forget()
    else:       
        startCal = Calendar(root)
        startCount = startCount + 1
        startCal.pack(pady=10)
        startCal.place(x=5, y=240)

def endCal():    
    global endCal
    global endCount
    if endCount == 1:
        endCount = 0
        endCal.place_forget()
    else:
        endCal = Calendar(root)
        endCount = endCount + 1    
        endCal.pack(pady=10)
        endCal.place(x=230, y=240)

def removeCal():
    global startCount
    global endCount
    if startCount == 1:
        startCount = 0
        startCal.place_forget()
    if endCount == 1:
        endCount = 0
        endCal.place_forget()

# 시작날짜버튼
startDateButton = Button(searchFrame, text="시작날짜", width=20, bg="green", fg="white", command=startCal)
startDateButton.pack(side="left", padx=20)

# 종료날짜버튼
endDateButton = Button(searchFrame, text="종료날짜", width=20, bg="green", fg="white", command=endCal)
endDateButton.pack(side="left", padx=20)
# 검색어 입력창
searchEntry = Entry(searchFrame, width=30)
searchEntry.pack(side="left", padx=20)
# 검색버튼
searchButton = Button(searchFrame, text="검색", width=20, bg="green", fg="white", command=removeCal)
searchButton.pack(side="left", padx=20)

searchFrame.pack(pady=5, fill="x")
searchFrame.place(x=10, y=210)

# 리스트 프레임
listFrame = Frame(root, bg="green")
listFrame.pack(fill="both", padx=5, pady=5)
listFrame.place(x=10, y=250)
scrollbar = Scrollbar(listFrame)
scrollbar.pack(side="right", fill="y")

newsList= Listbox(listFrame, selectmode="extended", width=150, height=30, yscrollcommand=scrollbar.set, bg="green")
newsList.pack(fill="both", expand=True)
scrollbar.config(command=newsList.yview)

# footer 프레임
footerFrame = Frame(root, bg="green")
# 제작자 라벨
createLabel = Label(footerFrame, text="POWERD by Holistic Python", width=30, fg="white", bg="green", anchor=W, font="Helvetica 15 bold")
createLabel.pack(side="left")
# 정렬 버튼
sortButton = Button(footerFrame, text="  ↘  정렬  ↗  ", width=50, bg="green", fg="white")
sortButton.pack(side="left", padx=20)
# 이메일 버튼
emailButton = Button(footerFrame, text="이메일발송", width=18, bg="green", fg="white")
emailButton.pack(side="left", padx=6)
# CSV 저장 버튼
saveButton = Button(footerFrame, text="csv저장", width=18, bg="green", fg="white")
saveButton.pack(side="left", padx=6)

footerFrame.pack(fill="x", padx=5, pady=5)
footerFrame.place(x=10, y=750)

root.mainloop()