from tkinter import *
from tkcalendar import Calendar
import pyautogui
#  객체생성
root = Tk()
# 제목설정
root.title("News Curator")
# 화면크기 설정
root.geometry("1100x800")
# 화면크기 변경 안됨
root.resizable(False, False)
# 배경화면 녹색
# root.configure(bg="green")

# 조선
radioChosun = Radiobutton(width=15, font=15, text="조선일보", value="조선일보", fg="black", pady=15)
radioChosun.pack()
radioChosun1 = Radiobutton(width=15, font=15, text="조선일보", value="조선일보", fg="black", pady=15)
radioChosun1.pack()
testButton = Button(root, text="버튼", fg="black")
testButton.pack()
print(testButton.cget("text"))
root.mainloop()
x, y = pyautogui.position()
print(x)

