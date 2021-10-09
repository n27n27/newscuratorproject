from tkinter import *
from tkcalendar import Calendar

# 메인
def newsCuratorRun():
    global root
    root = Tk()
    root.title("News Curator")
    root.geometry("1100x800")
    root.resizable(False, False)
    root.configure(bg="green")
    HeaderFrame(root)
    NewsFrame(root)
    SectionFrame(root)
    AdFrame(root)
    SearchFrame(root)
    ListFrame(root)
    FooterFrame(root)    
    root.mainloop()

# footer 프레임
class FooterFrame():

    def __init__(self, master):        
        self.footerFrame = Frame(master, bg="green")
        self.footerFrame.pack(fill="x", padx=5, pady=5)
        self.footerFrame.place(x=10, y=750)
        
        self.createLabel = Label(self.footerFrame, text="POWERD by Holistic Python", width=30, fg="white", bg="green", anchor=W, font="Helvetica 15 bold")
        self.createLabel.pack(side="left")
        
        self.sortButton = Button(self.footerFrame, text="  ↘  정렬  ↗  ", width=50, bg="green", fg="white")
        self.sortButton.pack(side="left", padx=20)
        
        self.emailButton = Button(self.footerFrame, text="이메일발송", width=18, bg="green", fg="white")
        self.emailButton.pack(side="left", padx=6)
        
        self.saveButton = Button(self.footerFrame, text="csv저장", width=18, bg="green", fg="white")
        self.saveButton.pack(side="left", padx=6)

# 리스트 프레임
class ListFrame():

    def __init__(self, master):        

        self.listFrame = Frame(master, bg="green")
        self.listFrame.pack(fill="both", padx=5, pady=5)
        self.listFrame.place(x=10, y=250)
        self.scrollbar = Scrollbar(self.listFrame)
        self.scrollbar.pack(side="right", fill="y")

        self.newsList = Listbox(self.listFrame, selectmode="extended", width=150, height=30, yscrollcommand=self.scrollbar.set, bg="green")
        self.newsList.pack(fill="both", expand=True)
        self.scrollbar.config(command=self.newsList.yview)

# 캘린더 생성
class CalMake():    

    def __init__(self, master):
        self.newsCal = Calendar(master)
        self.newsCal.pack(pady=10)    
        
# 검색 프레임
class SearchFrame():    

    # 달력
    startCount = 0
    endCount = 0        

    def __init__(self, master):
        self.searchFrame = Frame(master, bg="green")
        self.searchFrame.pack(pady=5, fill="x")
        self.searchFrame.place(x=10, y=210)        
        
        self.startDateButton = Button(self.searchFrame, text="시작날짜", width=20, bg="green", fg="white", command=self.startCalMake)
        self.startDateButton.pack(side="left", padx=20)
        
        self.endDateButton = Button(self.searchFrame, text="종료날짜", width=20, bg="green", fg="white", command=self.endCalMake)
        self.endDateButton.pack(side="left", padx=20)

        self.searchEntry = Entry(self.searchFrame, width=30)
        self.searchEntry.pack(side="left", padx=20)

        self.searchButton = Button(self.searchFrame, text="검색", width=20, bg="green", fg="white", command=self.removeCal)
        self.searchButton.pack(side="left", padx=20)

    def startCalMake(self):        
           
        if self.startCount == 0:
            self.startCal = CalMake(root)
            self.startCount = 1
            self.startCal.newsCal.place(x=5, y=240)
        else:
            self.startCal.newsCal.destroy()
            self.startCount = 0

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

# 광고 프레임
class AdFrame():

    def __init__(self, master):
        self.adFrame = Frame(master, bg="green", highlightthickness=2, highlightcolor="white")
        self.adLabel=Label(self.adFrame, width=7, text="광고삽입", font='Helvetica 35 bold', fg="white", bg="green", anchor=CENTER, pady=50, padx=5)
        self.adLabel.pack()
        self.adFrame.pack(pady=5)
        self.adFrame.place(x=860, y=70)            

# 섹션 프레임
class SectionFrame():

    def __init__(self, master):

        self.sectionVar = StringVar()

        self.sectionFrame = Frame(master, bg="green", highlightthickness=2, highlightcolor="white")    
        self.sectionFrame.pack(pady=5)
        self.sectionFrame.place(x=10, y=140)    

        self.radioSociety = Radiobutton(self.sectionFrame, selectcolor="green", activebackground = "green", width=15, font=15, text="사회", value="사회", bg="green", fg="white", variable=self.sectionVar, pady=15).grid(row=0, column = 0)    
        self.radioPolitics = Radiobutton(self.sectionFrame, selectcolor="green", activebackground = "green", width=15, font=15, text="정치", value="정치", bg="green", fg="white", variable=self.sectionVar, pady=15).grid(row=0, column = 1)
        self.radioEconomy = Radiobutton(self.sectionFrame, selectcolor="green", activebackground = "green", width=15, font=15, text="경제", value="경제", bg="green", fg="white", variable=self.sectionVar, pady=15).grid(row=0, column = 2)
        self.radioIT = Radiobutton(self.sectionFrame, selectcolor="green", activebackground = "green", width=15, font=15, text="IT", value="IT", bg="green", fg="white", variable=self.sectionVar, pady=15).grid(row=0, column = 3)
        self.radioSports = Radiobutton(self.sectionFrame, selectcolor="green", activebackground = "green", width=15, font=15, text="스포츠", value="스포츠", bg="green", fg="white", variable=self.sectionVar, pady=15).grid(row=0, column = 4)   

# 뉴스 프레임
class NewsFrame():    
    
    def __init__(self, master) -> None:

        self.newsVar = StringVar()
        self.newsFrame = Frame(master, bg="green", highlightcolor="white", highlightthickness=2)
        self.newsFrame.pack(pady=5)
        self.newsFrame.place(x=10, y=70)        

        self.radioChosun = Radiobutton(self.newsFrame, selectcolor="green", activebackground = "green", width=15, font=15, text="조선일보", value="조선일보", bg="green", fg="white", variable=self.newsVar, pady=15).grid(row=0, column=0)
        self.radioJungang = Radiobutton(self.newsFrame, selectcolor="green", activebackground = "green", width=15, font=15, text="중앙일보", value="중앙일보", bg="green", fg="white", variable=self.newsVar, pady=15).grid(row=0, column=1)
        self.radioDonga = Radiobutton(self.newsFrame, selectcolor="green", activebackground = "green", width=15, font=15, text="동아일보", value="동아일보", bg="green", fg="white", variable=self.newsVar, pady=15).grid(row=0, column=2)
        self.radioHan = Radiobutton(self.newsFrame, selectcolor="green", activebackground = "green", width=15, font=15, text="한겨레", value="한겨레", bg="green", fg="white", variable=self.newsVar, pady=15).grid(row=0, column=3)
        self.radioKyung = Radiobutton(self.newsFrame, selectcolor="green", activebackground = "green", width=15, font=15, text="경향", value="경향", bg="green", fg="white", variable=self.newsVar, pady=15).grid(row=0, column=4) 

    def selectedNews(self):
        print(self.newsVar.get())

# header frame
class HeaderFrame():

    def __init__(self, master):
        header = Frame(master, bg="green")
        header.pack(fill="x", padx=5, pady=5, ipadx=10, ipady=10)
        header.newsCuratorLabel = Label(header, text="뉴스 큐레이터", width=80, fg="white", bg="green", anchor=W, font='Helvetica 20 bold')
        header.newsCuratorLabel.pack(fill="x", side="left")

        header.logIn = Frame(header)
        header.logIn.pack(fill="x")

        header.idLabel = Label(header.logIn, text="아이디", width=10, fg="white", bg="green", font=15, padx=3)
        header.idLabel.pack(side="left")
        header.idEntry = Entry(header.logIn, width=15, font=15)
        header.idEntry.pack(side="left")

        header.pwEntry = Entry(header.logIn, width=15, font=15)
        header.pwLabel = Label(header.logIn, width=10, text="비밀번호", fg="white", bg="green", font=15, padx=3)
        header.pwEntry.pack(side="right")
        header.pwLabel.pack(side="right")
        header.logIn.place(x=600, y=12)    