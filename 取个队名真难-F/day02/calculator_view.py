# @time 2018/10/16-12:16
# @Author lhf

from tkinter import Entry, Button, messagebox, Frame
from tkinter.ttk import Label


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.hintLabel = Label(self, text='请输入需要计算的运算符：')
        self.hintLabel.pack()
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='计算', command=self.reduce)
        self.alertButton.pack()
        self.resultLabel = Label(self, text='')
        self.resultLabel.pack()
    def reduce(self):
        name = self.nameInput.get() or ''
        if name=='':
            messagebox.showinfo('提示', '请输入运算')
            return
        try:
            self.resultLabel["text"] = "输出结果:"+str(eval(name))
        except:
            messagebox.showinfo('警告',"肥仔别闹")

if __name__=="__main__":
    app = Application()
    # 设置窗口标题:
    app.master.title('计算器')
    # 主消息循环:
    app.mainloop()
