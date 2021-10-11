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

    root = Tk()
    root.title("News Curator")
    root.geometry("1100x800")
    root.resizable(False, False)
    root.configure(bg="#284922")    
    headerFrame = HeaderFrame(root)
    innerFrame = InnerFrame(headerFrame.header)
    NewsFrame(root)                     
    SectionFrame(root)
    AdFrame(root)
    searchFrame = SearchFrame(root)
    ListFrame(root)
    FooterFrame(root)    
    root.mainloop()

# footer 프레임
class FooterFrame():

    def __init__(self, master):        
        footerFrame = Frame(master, bg="#284922")
        footerFrame.pack(fill="x", padx=5, pady=5)
        footerFrame.place(x=10, y=750)
        
        createLabel = Label(footerFrame, text="POWERD by Holistic Python", width=30, fg="white", bg="#284922", anchor=W, font="Helvetica 15 bold")
        createLabel.pack(side="left")
        
        sortButton = Button(footerFrame, text="  ↘  정렬  ↗  ", width=50, bg="#284922", fg="white")
        sortButton.pack(side="left", padx=20)
        
        emailButton = Button(footerFrame, text="이메일발송", width=18, bg="#284922", fg="white")
        emailButton.pack(side="left", padx=6)
        
        saveButton = Button(footerFrame, text="csv저장", width=18, bg="#284922", fg="white")
        saveButton.pack(side="left", padx=6)

# 리스트 프레임
class ListFrame():

    def __init__(self, master):        

        listFrame = Frame(master, bg="#284922")
        listFrame.pack(fill="both", padx=5, pady=5)
        listFrame.place(x=10, y=250)
        scrollbar = Scrollbar(listFrame)
        scrollbar.pack(side="right", fill="y")

        newsList = Listbox(listFrame, selectmode="extended", width=150, height=30, yscrollcommand=scrollbar.set, bg="#284922")
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
        self.searchFrame = Frame(master, bg="#284922")
        self.searchFrame.pack(pady=5, fill="x")
        self.searchFrame.place(x=10, y=210)        
        
        startDateButton = Button(self.searchFrame, text="시작날짜", width=20, bg="#284922", fg="white", command=self.startCalMake)
        startDateButton.pack(side="left", padx=20)
        
        endDateButton = Button(self.searchFrame, text="종료날짜", width=20, bg="#284922", fg="white", command=self.endCalMake)
        endDateButton.pack(side="left", padx=20)

        searchEntry = Entry(self.searchFrame, width=30)
        searchEntry.pack(side="left", padx=20)

        searchButton = Button(self.searchFrame, text="검색", width=20, bg="#284922", fg="white", command=self.search)
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
        self.calModal = Toplevel(master, bg="#284922")
        self.x, self.y = pyautogui.position()
        self.calModal.geometry(f"{300}x{90}+{self.x-450}+{self.y+50}")
        self.calModal.transient(master)
        self.errorLabel = Label(self.calModal, text="날짜 정보를 올바르게 입력해주세요.", fg="white", font='Helvetica 12', pady=10, padx=10, bg="#284922")
        self.errorLabel.pack()
        self.errorLabel1 = Label(self.calModal, text="종료날짜가 시작날짜 이전입니다.", fg="white", font='Helvetica 12', pady=10, padx=10, bg="#284922")
        self.errorLabel1.pack()
        self.calModal.protocol("WM_DELETE_WINDOW", self.close)         

    def close(self):
        root.wm_attributes("-disabled", False)
        self.calModal.destroy()     
    
# 광고 프레임
class AdFrame():

    def __init__(self, master):
        adFrame = Frame(master, bg="#284922", highlightthickness=2, highlightcolor="white")
        adLabel=Label(adFrame, width=7, text="광고삽입", font='Helvetica 35 bold', fg="white", bg="#284922", anchor=CENTER, pady=50, padx=5)
        adLabel.pack()
        adFrame.pack(pady=5)
        adFrame.place(x=860, y=70)            

# 섹션 프레임
class SectionFrame():

    def __init__(self, master):

        self.sectionVar = StringVar()

        sectionFrame = Frame(master, bg="#284922", highlightthickness=2, highlightcolor="white")    
        sectionFrame.pack(pady=5)
        sectionFrame.place(x=10, y=140)    

        radioSociety = Radiobutton(sectionFrame, selectcolor="#284922", activebackground = "#284922", width=15, font=15, text="사회", value="사회", bg="#284922", fg="white", variable=self.sectionVar, pady=15).grid(row=0, column = 0)    
        radioPolitics = Radiobutton(sectionFrame, selectcolor="#284922", activebackground = "#284922", width=15, font=15, text="정치", value="정치", bg="#284922", fg="white", variable=self.sectionVar, pady=15).grid(row=0, column = 1)
        radioEconomy = Radiobutton(sectionFrame, selectcolor="#284922", activebackground = "#284922", width=15, font=15, text="경제", value="경제", bg="#284922", fg="white", variable=self.sectionVar, pady=15).grid(row=0, column = 2)
        radioIT = Radiobutton(sectionFrame, selectcolor="#284922", activebackground = "#284922", width=15, font=15, text="IT", value="IT", bg="#284922", fg="white", variable=self.sectionVar, pady=15).grid(row=0, column = 3)
        radioSports = Radiobutton(sectionFrame, selectcolor="#284922", activebackground = "#284922", width=15, font=15, text="스포츠", value="스포츠", bg="#284922", fg="white", variable=self.sectionVar, pady=15).grid(row=0, column = 4)   

# 뉴스 프레임
class NewsFrame():    
    
    def __init__(self, master) -> None:

        self.newsVar = StringVar()
        newsFrame = Frame(master, bg="#284922", highlightcolor="white", highlightthickness=2)
        newsFrame.pack(pady=5)
        newsFrame.place(x=10, y=70)        

        radioChosun = Radiobutton(newsFrame, selectcolor="#284922", activebackground = "#284922", width=15, font=15, text="조선일보", value="조선일보", bg="#284922", fg="white", variable=self.newsVar, pady=15).grid(row=0, column=0)
        radioJungang = Radiobutton(newsFrame, selectcolor="#284922", activebackground = "#284922", width=15, font=15, text="중앙일보", value="중앙일보", bg="#284922", fg="white", variable=self.newsVar, pady=15).grid(row=0, column=1)
        radioDonga = Radiobutton(newsFrame, selectcolor="#284922", activebackground = "#284922", width=15, font=15, text="동아일보", value="동아일보", bg="#284922", fg="white", variable=self.newsVar, pady=15).grid(row=0, column=2)
        radioHan = Radiobutton(newsFrame, selectcolor="#284922", activebackground = "#284922", width=15, font=15, text="한겨레", value="한겨레", bg="#284922", fg="white", variable=self.newsVar, pady=15).grid(row=0, column=3)
        radioKyung = Radiobutton(newsFrame, selectcolor="#284922", activebackground = "#284922", width=15, font=15, text="경향", value="경향", bg="#284922", fg="white", variable=self.newsVar, pady=15).grid(row=0, column=4) 

    def selectedNews(self):
        print(self.newsVar.get())

# logIn Frame
class LogInFrame():

    def __init__(self, master):        
        self.logIn = Frame(master, bg="#284922")
        self.logIn.pack(fill="x", ipady=5)

        idLabel = Label(self.logIn, text="아이디", width=6, fg="white", bg="#284922", font=10, padx=10)
        idLabel.pack(side="left")
        idEntry = Entry(self.logIn, width=11, font=10)
        idEntry.pack(side="left", padx=5)

        backButton = Button(self.logIn, text="←", width=2, fg="white", bg="#284922", font=6, command=self.back)
        backButton.pack(side="right", padx=7)
        goButton = Button(self.logIn, text="Go", width=2, fg="white", bg="#284922", font=6)
        goButton.pack(side="right", padx=7)

        pwEntry = Entry(self.logIn, width=12, font=10)
        pwLabel = Label(self.logIn, width=7, text="비밀번호", fg="white", bg="#284922", font=10, padx=10)
        pwEntry.pack(side="right", padx=5)
        pwLabel.pack(side="right")
        self.logIn.place(x=630, y=12)

    def back(self):
        self.logIn.destroy()
        InnerFrame(headerFrame.header) 


# 회원 가입창
class JoinUs():
    
    def __init__(self, master, x, y):
        self.joinWindow = Toplevel(root, bg="#284922")
        self.joinWindow.title("회원가입")
        self.joinWindow.geometry(f"{250}x{150}+{x-130}+{y+40}")
        self.joinWindow.protocol("WM_DELETE_WINDOW", self.quitWindow)

        labelFrame = Frame(self.joinWindow, padx=5, pady=5, bg="#284922")    
        labelFrame.grid(row=0, column=0)

        name = Label(labelFrame, text="Name", padx=5, pady=5, bg="#284922", fg="white").pack()
        email = Label(labelFrame, text="e-mail", padx=5, pady=5, bg="#284922", fg="white").pack()
        password = Label(labelFrame, text="Password", padx=5, pady=5, bg="#284922", fg="white").pack()
        entryFrame = Frame(self.joinWindow, padx=5, pady=5, bg="#284922")
        entryFrame.grid(row=0, column=1)

        nameEntry = Entry(entryFrame).pack(padx=5, pady=5)
        emailEntry = Entry(entryFrame).pack(padx=5, pady=5)
        passwordEntry = Entry(entryFrame).pack(padx=5, pady=5)

        joinButton = Button(self.joinWindow, text="회원가입", padx=10, bg="#284922", fg="white").grid(row=1, columnspan=5, pady=5)
        
        
    def quitWindow(self):
        innerFrame.joinCount = 0 
        self.joinWindow.destroy()        

# inner frame
class InnerFrame():

    joinCount = 0       

    def __init__(self, master):
        self.innerFrame = Frame(master, bg="#284922")
        self.innerFrame.place(x=800, y=12)

        self.joinUsButton = Button(self.innerFrame, text="회원가입", width=10, fg="white", bg="#284922", padx=3, command=self.joinUs)        
        self.joinUsButton.pack(side="right", padx=20)        

        logInButton = Button(self.innerFrame, text="로그인", width=10, fg="white", bg="#284922", padx=3, command=self.logIn)
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
        self.header = Frame(master, bg="#284922")
        self.header.pack(fill="x", padx=5, pady=5, ipadx=10, ipady=10)
        self.newsCuratorLabel = Label(self.header, text="뉴스 큐레이터", width=80, fg="white", bg="#284922", anchor=W, font='Helvetica 20 bold')
        self.newsCuratorLabel.pack(fill="x", side="left")