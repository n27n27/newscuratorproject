from tkinter import *
from tkcalendar import Calendar


# 메인
def mainWindow():
    global root
    root = Tk()
    root.title("News Curator")
    root.geometry("1100x800")
    root.resizable(False, False)
    root.configure(bg="green")
    headerFrameMake()
    logInFrameMake()
    newsFrameMake()
    sectionFrameMake()
    addFrameMake()
    searchFrameMake()
    listFrameMake()
    footerFrameMake()
    root.mainloop()

# footer 프레임
def footerFrameMake():
    footerFrame = Frame(root, bg="green")
    footerFrame.pack(fill="x", padx=5, pady=5)
    footerFrame.place(x=10, y=750)
    
    createLabel = Label(footerFrame, text="POWERD by Holistic Python", width=30, fg="white", bg="green", anchor=W, font="Helvetica 15 bold")
    createLabel.pack(side="left")
    
    sortButton = Button(footerFrame, text="  ↘  정렬  ↗  ", width=50, bg="green", fg="white")
    sortButton.pack(side="left", padx=20)
    
    emailButton = Button(footerFrame, text="이메일발송", width=18, bg="green", fg="white")
    emailButton.pack(side="left", padx=6)
    
    saveButton = Button(footerFrame, text="csv저장", width=18, bg="green", fg="white")
    saveButton.pack(side="left", padx=6)

# 리스트 프레임
def listFrameMake():
    listFrame = Frame(root, bg="green")
    listFrame.pack(fill="both", padx=5, pady=5)
    listFrame.place(x=10, y=250)
    scrollbar = Scrollbar(listFrame)
    scrollbar.pack(side="right", fill="y")

    newsList= Listbox(listFrame, selectmode="extended", width=150, height=30, yscrollcommand=scrollbar.set, bg="green")
    newsList.pack(fill="both", expand=True)
    scrollbar.config(command=newsList.yview)

# 검색 프레임
def searchFrameMake():
    global searchEntry
    searchFrame = Frame(root, bg="green")
    searchFrame.pack(pady=5, fill="x")
    searchFrame.place(x=10, y=210)
    
    startDateButton = Button(searchFrame, text="시작날짜", width=20, bg="green", fg="white", command=startCal)
    startDateButton.pack(side="left", padx=20)


    endDateButton = Button(searchFrame, text="종료날짜", width=20, bg="green", fg="white", command=endCal)
    endDateButton.pack(side="left", padx=20)

    searchEntry = Entry(searchFrame, width=30)
    searchEntry.pack(side="left", padx=20)

    searchButton = Button(searchFrame, text="검색", width=20, bg="green", fg="white", command=searchNews)
    searchButton.pack(side="left", padx=20)        

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

def searchNews():
    global startCount    
    print("검색뉴스 : " + newsVar.get())
    print("검색섹션 : " + sectionVar.get())    
    if startCount != 0:
        print("시작날짜 : " + startCal.get_date())
    if endCount != 0:
        print("종료날짜 : " + endCal.get_date())
    print("검색어: " + searchEntry.get())
    removeCal()

# 광고 프레임
def addFrameMake():
    adFrame = Frame(root, bg="green", highlightthickness=2, highlightcolor="white")
    adLabel=Label(adFrame, width=7, text="광고삽입", font='Helvetica 35 bold', fg="white", bg="green", anchor=CENTER, pady=50, padx=5)
    adLabel.pack()
    adFrame.pack(pady=5)
    adFrame.place(x=860, y=70)        

# 섹션 프레임
def selectedSection():
    global sectionVar
    sectionVar.get()

def sectionFrameMake():
    global sectionVar
    sectionVar = StringVar()
    sectionFrame = Frame(root, bg="green", highlightthickness=2, highlightcolor="white")    
    sectionFrame.pack(pady=5)
    sectionFrame.place(x=10, y=140)    

    radioSociety = Radiobutton(sectionFrame, selectcolor="green", activebackground = "green", width=15, font=15, text="사회", value="사회", bg="green", fg="white", variable=sectionVar, pady=15, command=selectedSection).grid(row=0, column = 0)    
    radioPolitics = Radiobutton(sectionFrame, selectcolor="green", activebackground = "green", width=15, font=15, text="정치", value="정치", bg="green", fg="white", variable=sectionVar, pady=15, command=selectedSection).grid(row=0, column = 1)
    radioEconomy = Radiobutton(sectionFrame, selectcolor="green", activebackground = "green", width=15, font=15, text="경제", value="경제", bg="green", fg="white", variable=sectionVar, pady=15, command=selectedSection).grid(row=0, column = 2)
    radioIT = Radiobutton(sectionFrame, selectcolor="green", activebackground = "green", width=15, font=15, text="IT", value="IT", bg="green", fg="white", variable=sectionVar, pady=15, command=selectedSection).grid(row=0, column = 3)
    radioSports = Radiobutton(sectionFrame, selectcolor="green", activebackground = "green", width=15, font=15, text="스포츠", value="스포츠", bg="green", fg="white", variable=sectionVar, pady=15, command=selectedSection).grid(row=0, column = 4)

# 신문사 프레임
def selectedNews():
    global newsVar
    newsVar.get()

def newsFrameMake():
    global newsVar
    newsVar = StringVar()
    newsFrame = Frame(root, bg="green", highlightcolor="white", highlightthickness=2)
    newsFrame.pack(pady=5)
    newsFrame.place(x=10, y=70)    
    
    radioChosun = Radiobutton(newsFrame, selectcolor="green", activebackground = "green", width=15, font=15, text="조선일보", value="조선일보", bg="green", fg="white", variable=newsVar, pady=15, command=selectedNews).grid(row=0, column=0)
    radioJungang = Radiobutton(newsFrame, selectcolor="green", activebackground = "green", width=15, font=15, text="중앙일보", value="중앙일보", bg="green", fg="white", variable=newsVar, pady=15, command=selectedNews).grid(row=0, column=1)
    radioDonga = Radiobutton(newsFrame, selectcolor="green", activebackground = "green", width=15, font=15, text="동아일보", value="동아일보", bg="green", fg="white", variable=newsVar, pady=15, command=selectedNews).grid(row=0, column=2)
    radioHan = Radiobutton(newsFrame, selectcolor="green", activebackground = "green", width=15, font=15, text="한겨레", value="한겨레", bg="green", fg="white", variable=newsVar, pady=15, command=selectedNews).grid(row=0, column=3)
    radioKyung = Radiobutton(newsFrame, selectcolor="green", activebackground = "green", width=15, font=15, text="경향", value="경향", bg="green", fg="white", variable=newsVar, pady=15, command=selectedNews).grid(row=0, column=4)   

# header frame
def headerFrameMake():
    global headerFrame
    headerFrame = Frame(root, bg="green")
    headerFrame.pack(fill="x", padx=5, pady=5, ipadx=10, ipady=10)
    newsCuratorLabel = Label(headerFrame, text="뉴스 큐레이터", width=80, fg="white", bg="green", anchor=W, font='Helvetica 20 bold')
    newsCuratorLabel.pack(fill="x", side="left")

# login frame
def logInFrameMake():
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
    
