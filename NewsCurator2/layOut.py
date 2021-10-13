from tkinter import *
from tkcalendar import Calendar
import pyautogui
from datetime import *

# 메인
def newsCuratorRun():
    global root
    global headerFrame
    global searchFrame
    global innerFrame
    global backGroundColor
    global sectionFrame
    global newsFrame    

    backGroundColor = "#284922"
    root = Tk()
    root.title("News Curator")
    root.geometry("1100x800")
    root.resizable(False, False)
    root.configure(bg=backGroundColor)    
    headerFrame = HeaderFrame(root)
    innerFrame = InnerFrame(headerFrame.header)
    newsFrame = NewsFrame(root)                     
    sectionFrame = SectionFrame(root)
    AdFrame(root)
    searchFrame = SearchFrame(root)
    ListFrame(root)
    FooterFrame(root)    
    root.mainloop()

# footer 프레임
class FooterFrame():

    def __init__(self, master):        
        footerFrame = Frame(master, bg=backGroundColor)
        footerFrame.pack(fill="x", padx=5, pady=5)
        footerFrame.place(x=10, y=750)
        
        createLabel = Label(footerFrame, text="POWERD by Holistic Python", width=30, fg="white", bg=backGroundColor, anchor=W, font="Helvetica 15 bold")
        createLabel.pack(side="left")
        
        sortButton = Button(footerFrame, text="  ↘  정렬  ↗  ", width=50, bg=backGroundColor, fg="white")
        sortButton.pack(side="left", padx=20)
        
        emailButton = Button(footerFrame, text="이메일발송", width=18, bg=backGroundColor, fg="white")
        emailButton.pack(side="left", padx=6)
        
        saveButton = Button(footerFrame, text="csv저장", width=18, bg=backGroundColor, fg="white")
        saveButton.pack(side="left", padx=6)

# 리스트 프레임
class ListFrame():

    def __init__(self, master):        

        listFrame = Frame(master, bg=backGroundColor)
        listFrame.pack(fill="both", padx=5, pady=5)
        listFrame.place(x=10, y=250)
        scrollbar = Scrollbar(listFrame)
        scrollbar.pack(side="right", fill="y")

        newsList = Listbox(listFrame, selectmode="extended", width=150, height=30, yscrollcommand=scrollbar.set, bg=backGroundColor)
        newsList.pack(fill="both", expand=True)
        scrollbar.config(command=newsList.yview)

# 캘린더 생성
class CalMake():    

    def __init__(self, master):
        self.newsCal = Calendar(master, date_pattern = "ymmdd")
        self.newsCal.pack(pady=10)    
        
# 검색 프레임
class SearchFrame():    

    # 달력
    startCount = 0
    endCount = 0        

    def __init__(self, master):
        self.searchFrame = Frame(master, bg=backGroundColor)
        self.searchFrame.pack(pady=5, fill="x")
        self.searchFrame.place(x=10, y=210)        
        
        startDateButton = Button(self.searchFrame, text="시작날짜", width=20, bg=backGroundColor, fg="white", command=self.startCalMake)
        startDateButton.pack(side="left", padx=20)
        
        endDateButton = Button(self.searchFrame, text="종료날짜", width=20, bg=backGroundColor, fg="white", command=self.endCalMake)
        endDateButton.pack(side="left", padx=20)

        searchEntry = Entry(self.searchFrame, width=30)
        searchEntry.pack(side="left", padx=20)

        searchButton = Button(self.searchFrame, text="검색", width=20, bg=backGroundColor, fg="white", command=self.search)
        searchButton.pack(side="left", padx=20)

    # 검색날짜 세팅
    def dateSet(self):

        now = datetime.now().strftime("%Y%m%d")

        # 시작날짜(없으면 오늘)
        if self.startCount != 0:
           startDate = self.startCal.newsCal.get_date()       
        else:
            startDate = now

        # 종료날짜(없으면 오늘)
        if self.endCount != 0:
            endDate = self.endCal.newsCal.get_date()
        else:
            endDate = now
        
        if int(endDate) > int(now):
            endDate = now       
        
        if int(startDate) > int(endDate):
            root.wm_attributes("-disabled", True)
            CalError(root)  

    # 검색    
    def search(self):
        searchSection = []
        searchNews = []
        for i in range(len(sectionFrame.sectionVar)):
            if sectionFrame.sectionVar[i].get() != "":
                searchSection.append(sectionFrame.sectionVar[i].get())

            if newsFrame.newsVar[i].get() != "":
                searchNews.append(newsFrame.newsVar[i].get())

        print(searchSection, searchNews)
        
        self.dateSet()
        self.removeCal()

    # 시작달력
    def startCalMake(self):        
           
        if self.startCount == 0:
            self.startCal = CalMake(root)
            self.startCount = 1
            self.startCal.newsCal.place(x=5, y=240)                     
        else:
            self.startCal.newsCal.destroy()
            self.startCount = 0

    # 종료 달력
    def endCalMake(self):

        if self.endCount == 0:
            self.endCal = CalMake(root)
            self.endCount = 1
            self.endCal.newsCal.place(x=230, y=240)            
        else:
            self.endCal.newsCal.destroy()
            self.endCount = 0

    def removeCal(self):
        
        if self.startCount == 1:

            self.startCount = 0
            self.startCal.newsCal.destroy()                   
        
        if self.endCount == 1:

            self.endCount = 0
            self.endCal.newsCal.destroy()            

# 달력 에러 알림창 modal 적용
class CalError():   

    def __init__(self, master):
        self.calModal = Toplevel(master, bg=backGroundColor)
        self.x, self.y = pyautogui.position()
        self.calModal.geometry(f"{300}x{90}+{self.x-450}+{self.y+50}")
        self.calModal.transient(master)
        self.errorLabel = Label(self.calModal, text="날짜 정보를 올바르게 입력해주세요.", fg="white", font='Helvetica 12', pady=10, padx=10, bg=backGroundColor)
        self.errorLabel.pack()
        self.errorLabel1 = Label(self.calModal, text="종료날짜가 시작날짜 이전입니다.", fg="white", font='Helvetica 12', pady=10, padx=10, bg=backGroundColor)
        self.errorLabel1.pack()
        self.calModal.protocol("WM_DELETE_WINDOW", self.close)         

    def close(self):
        root.wm_attributes("-disabled", False)
        self.calModal.destroy()     
    
# 광고 프레임
class AdFrame():

    def __init__(self, master):
        adFrame = Frame(master, bg=backGroundColor, highlightthickness=2, highlightcolor="white")
        adLabel=Label(adFrame, width=7, text="광고삽입", font='Helvetica 35 bold', fg="white", bg=backGroundColor, anchor=CENTER, pady=50, padx=5)
        adLabel.pack()
        adFrame.pack(pady=5)
        adFrame.place(x=860, y=70)            

# 섹션 프레임
class SectionFrame():

    def __init__(self, master):        

        sectionFrame = Frame(master, bg=backGroundColor, highlightthickness=2, highlightcolor="white")    
        sectionFrame.pack(pady=5)
        sectionFrame.place(x=10, y=140)

        self.sectionVar = []

        for i in range(5):
            self.sectionVar.append(0)
            self.sectionVar[i] = StringVar()
        
        checkSociety = Checkbutton(sectionFrame, selectcolor=backGroundColor, activebackground = backGroundColor, width=15, font=15, text="사회", bg=backGroundColor, fg="white", pady=15, variable=self.sectionVar[0], onvalue="사회", offvalue="").grid(row=0, column = 0)    
        checkPolitics = Checkbutton(sectionFrame, selectcolor=backGroundColor, activebackground = backGroundColor, width=15, font=15, text="정치", bg=backGroundColor, fg="white", pady=15, variable=self.sectionVar[1], onvalue="정치", offvalue="").grid(row=0, column = 1)
        checkEconomy = Checkbutton(sectionFrame, selectcolor=backGroundColor, activebackground = backGroundColor, width=15, font=15, text="경제", bg=backGroundColor, fg="white",  pady=15, variable=self.sectionVar[2], onvalue="경제", offvalue="").grid(row=0, column = 2)
        checkIT = Checkbutton(sectionFrame, selectcolor=backGroundColor, activebackground = backGroundColor, width=15, font=15, text="IT", bg=backGroundColor, fg="white", pady=15, variable=self.sectionVar[3], onvalue="IT", offvalue="").grid(row=0, column = 3)
        checkSports = Checkbutton(sectionFrame, selectcolor=backGroundColor, activebackground = backGroundColor, width=15, font=15, text="스포츠", bg=backGroundColor, fg="white", pady=15, variable=self.sectionVar[4], onvalue="스포츠", offvalue="").grid(row=0, column = 4)      
        
# 뉴스 프레임
class NewsFrame():    
    
    def __init__(self, master) -> None:
        
        newsFrame = Frame(master, bg=backGroundColor, highlightcolor="white", highlightthickness=2)
        newsFrame.pack(pady=5)
        newsFrame.place(x=10, y=70)        
        
        self.newsVar = []

        for i in range(5):
            self.newsVar.append(0)
            self.newsVar[i] = StringVar()
        checkChosun = Checkbutton(newsFrame, text="조선일보", font=15, fg="white", activebackground = backGroundColor, bg=backGroundColor, width=15, selectcolor=backGroundColor, pady=15, variable=self.newsVar[0], onvalue="조선일보", offvalue="").grid(row=0, column=0)
        checkJungang = Checkbutton(newsFrame, text="중앙일보", font=15, fg="white", activebackground = backGroundColor, bg=backGroundColor, width=15, selectcolor=backGroundColor, pady=15, variable=self.newsVar[1], onvalue="중앙일보", offvalue="").grid(row=0, column=1)
        checkDonga = Checkbutton(newsFrame, text="동아일보", font=15, fg="white", activebackground = backGroundColor, bg=backGroundColor, width=15, selectcolor=backGroundColor, pady=15, variable=self.newsVar[2], onvalue="동아일보", offvalue="").grid(row=0, column=2)
        checkHan = Checkbutton(newsFrame, text="한겨레", font=15, fg="white", activebackground = backGroundColor, bg=backGroundColor, width=15, selectcolor=backGroundColor, pady=15, variable=self.newsVar[3], onvalue="한겨레", offvalue="").grid(row=0, column=3)
        checkKyung = Checkbutton(newsFrame, text="경향", font=15, fg="white", activebackground = backGroundColor, bg=backGroundColor, width=15, selectcolor=backGroundColor, pady=15, variable=self.newsVar[4], onvalue="경향", offvalue="").grid(row=0, column=4)        
    
# logIn Frame
class LogInFrame():

    def __init__(self, master):        
        self.logIn = Frame(master, bg=backGroundColor)
        self.logIn.pack(fill="x", ipady=5)

        idLabel = Label(self.logIn, text="아이디", width=6, fg="white", bg=backGroundColor, font=10, padx=10)
        idLabel.pack(side="left")
        idEntry = Entry(self.logIn, width=11, font=10)
        idEntry.pack(side="left", padx=5)

        backButton = Button(self.logIn, text="←", width=2, fg="white", bg=backGroundColor, font=6, command=self.back)
        backButton.pack(side="right", padx=7)
        goButton = Button(self.logIn, text="Go", width=2, fg="white", bg=backGroundColor, font=6)
        goButton.pack(side="right", padx=7)

        pwEntry = Entry(self.logIn, width=12, font=10)
        pwLabel = Label(self.logIn, width=7, text="비밀번호", fg="white", bg=backGroundColor, font=10, padx=10)
        pwEntry.pack(side="right", padx=5)
        pwLabel.pack(side="right")
        self.logIn.place(x=630, y=12)

    def back(self):
        self.logIn.destroy()
        InnerFrame(headerFrame.header) 


# 회원 가입창
class JoinUs():
    
    def __init__(self, master, x, y):
        self.joinWindow = Toplevel(root, bg=backGroundColor)
        self.joinWindow.title("회원가입")
        self.joinWindow.geometry(f"{250}x{150}+{x-130}+{y+40}")
        self.joinWindow.protocol("WM_DELETE_WINDOW", self.quitWindow)

        labelFrame = Frame(self.joinWindow, padx=5, pady=5, bg=backGroundColor)    
        labelFrame.grid(row=0, column=0)

        name = Label(labelFrame, text="Name", padx=5, pady=5, bg=backGroundColor, fg="white").pack()
        email = Label(labelFrame, text="e-mail", padx=5, pady=5, bg=backGroundColor, fg="white").pack()
        password = Label(labelFrame, text="Password", padx=5, pady=5, bg=backGroundColor, fg="white").pack()
        entryFrame = Frame(self.joinWindow, padx=5, pady=5, bg=backGroundColor)
        entryFrame.grid(row=0, column=1)

        nameEntry = Entry(entryFrame).pack(padx=5, pady=5)
        emailEntry = Entry(entryFrame).pack(padx=5, pady=5)
        passwordEntry = Entry(entryFrame).pack(padx=5, pady=5)

        joinButton = Button(self.joinWindow, text="회원가입", padx=10, bg=backGroundColor, fg="white").grid(row=1, columnspan=5, pady=5)
        
        
    def quitWindow(self):
        innerFrame.joinCount = 0 
        self.joinWindow.destroy()        

# inner frame
class InnerFrame():

    joinCount = 0       

    def __init__(self, master):
        self.innerFrame = Frame(master, bg=backGroundColor)
        self.innerFrame.place(x=800, y=12)

        self.joinUsButton = Button(self.innerFrame, text="회원가입", width=10, fg="white", bg=backGroundColor, padx=3, command=self.joinUs)        
        self.joinUsButton.pack(side="right", padx=20)        

        logInButton = Button(self.innerFrame, text="로그인", width=10, fg="white", bg=backGroundColor, padx=3, command=self.logIn)
        logInButton.pack(side="right", padx=20)

    def logIn(self):
        self.innerFrame.destroy()
        logInFrame = LogInFrame(headerFrame.header) 
    
    def joinUs(self):
        
        global x
        global y
        
        if self.joinCount == 0:
            self.joinCount = 1
            x, y = pyautogui.position()
            self.joinUsWindow = JoinUs(root, x, y)
        else:
            self.joinUsWindow.quitWindow()
        
# header frame
class HeaderFrame():           

    def __init__(self, master):
        self.header = Frame(master, bg=backGroundColor)
        self.header.pack(fill="x", padx=5, pady=5, ipadx=10, ipady=10)
        self.newsCuratorLabel = Label(self.header, text="뉴스 큐레이터", width=80, fg="white", bg=backGroundColor, anchor=W, font='Helvetica 20 bold')
        self.newsCuratorLabel.pack(fill="x", side="left")