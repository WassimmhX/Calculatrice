from calculator import Ui_Dialog
from math import *
from PyQt5.QtWidgets import *
def parenthese(ch=""):
    j=0
    for i in range(len(ch)):
        if ch[i]=="(":
            j+=1
        if ch[i]==")":
            j-=1
        if j==0:
            return i
def parenthese_1(ch=""):
    j=0
    for i in range(len(ch)-1,-1,-1):
        if ch[i]==")":
            j+=1
        if ch[i]=="(":
            j-=1
        if j==0:
            return i
def result(t):
    def fct(t):
        k=d = ""
        i = t.find("!")
        while True:
            if ord(t[i - 1]) not in range(ord("0"), ord("9")+1) and t[i - 1] != ".":
                if t[i - 1] == ')':
                    d = t[parenthese_1(t[:i]):i]
                    k=d
                    if "√" in d or "!" in d or "^" in d:
                        d = result(d)
                if d == "" or d in "()":
                    return ""
                break
            d = t[i - 1] + d
            k = t[i - 1] + k
            i -= 1
            if i <= 0:
                break
        try:
            eval(d)
        except:
            return ""
        if eval(d) == int(eval(d)):
            t = t.replace(k + "!", str(factorial(int(eval(d)))))
            return t
        else:
            return ""

    def rcn(t):
        k = d = ""
        i = t.find("√")
        if i == len(t) - 1 or t[i + 1] in ["^", "!"]:
            return ""
        while i != len(t) - 1:
            if ord(t[i + 1]) not in range(ord("0"), ord("9")+1) and t[i + 1] != ".":
                if t[i + 1] == '(':
                    d = t[i + 1:i+2+parenthese(t[i+1:])]
                    k = d
                    if "√" in d or "!" in d or "^" in d:
                        d = result(d)
                if t[i + 1] == '√':
                    k = t[i + 1:]
                    d = rcn(t[i + 1:])
                if d == "" or d in "()":
                    return ""
                break
            k += t[i + 1]
            d += t[i + 1]
            i += 1
        try:
            eval(d)
        except:
            return ""
        x = eval(d)
        if -10**(-12)<x < 10 ** (-12):
            x = 0
        t = t.replace("√" + k, str(sqrt(x)))
        return t
    def exp(t):
        k = d = ""
        i = t.find("^")
        if i == len(t) - 1 or t[i + 1] !="(":
            return ""
        d=t[i+1:i+2+parenthese(t[i+1:])]
        k=d
        if "!" in d or "^" in d or "√" in d:
            d=result(d)
        try:
            eval(d)
        except:
            return ""
        p=j=""
        while True:
            if ord(t[i - 1]) not in range(ord("0"), ord("9")+1) and t[i - 1] != ".":
                if t[i - 1] == ')':
                    j = t[i - 2 - t[:i - 1][::-1].find("("):i]
                    p=j
                    if "√" in j or "!" in j or "^" in j:
                        j = result(j)
                if j == "" or j in "()":
                    return ""
                break
            j = t[i - 1] + j
            p = t[i - 1] + p
            i -= 1
            if i <= 0:
                break
        try:
            eval(j)
        except:
            return ""
        x=eval(d)
        if -10**(-12)<x<10**(-12):
            x=0
        y=eval(j)
        if -10**(-12)<y<10**(-12):
            y=0
        t = t.replace(p+"^" + k, str(y**x))
        return t
    if "^" not in t and "!" not in t and '√' not in t:
        try:
            eval(t)
        except:
            return "Erreur"
        x=eval(t)
        if -10**(-12)<x<10**(-12):
            return "0"
        return str(x)
    else:
        if len(t) == 1 or t[0] in ["^", "!"]:
            return ""
        while True:
            e = s = f = len(t)
            if "^" in t:
                e = t.find("^")
            if "!" in t:
                f = t.find("!")
            if "√" in t:
                s = t.find("√")
            if e < min(f, s):
                t=exp(t)
                if t == "":
                    return ""
                e = len(t) + 1
            elif f < min(e, s):
                t = fct(t)
                if t == "":
                    return ""
                f = len(t) + 1
            elif s < min(f, e):
                t = rcn(t)
                if t == "":
                    return ""
                s = len(t) + 1
            if e == s == f == len(t):
                break
        return t
class Exec:
    def __init__(self):
        self.window=QDialog()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self.window)
        self.ui.pushButton_4.clicked.connect(lambda:self.write("-"))
        self.ui.pushButton_5.clicked.connect(lambda:self.write("1"))
        self.ui.pushButton_6.clicked.connect(lambda:self.write("4"))
        self.ui.pushButton_7.clicked.connect(lambda:self.write("7"))
        self.ui.pushButton_9.clicked.connect(lambda:self.write("0"))
        self.ui.pushButton_10.clicked.connect(lambda:self.write("2"))
        self.ui.pushButton_11.clicked.connect(lambda:self.write("5"))
        self.ui.pushButton_12.clicked.connect(lambda:self.write("8"))
        self.ui.pushButton_15.clicked.connect(lambda:self.write("."))
        self.ui.pushButton_16.clicked.connect(lambda:self.write("3"))
        self.ui.pushButton_17.clicked.connect(lambda:self.write("6"))
        self.ui.pushButton_18.clicked.connect(lambda:self.write("9"))
        self.ui.pushButton_22.clicked.connect(lambda:self.write("+"))
        self.ui.pushButton_23.clicked.connect(lambda:self.write("-"))
        self.ui.pushButton_24.clicked.connect(lambda:self.write("*"))
        self.ui.pushButton_25.clicked.connect(lambda:self.write("/"))
        self.ui.pushButton_13.clicked.connect(lambda:self.write(self.ui.pushButton_13.text()))
        self.ui.pushButton.clicked.connect(lambda:self.write("("))
        self.ui.pushButton_2.clicked.connect(lambda:self.write(")"))
        self.ui.pushButton_27.clicked.connect(lambda:self.write("!"))
        self.ui.pushButton_28.clicked.connect(lambda:self.write("π"))
        self.ui.pushButton_19.clicked.connect(lambda:self.write(self.ui.pushButton_19.text()))
        self.ui.pushButton_8.clicked.connect(lambda:self.write(self.ui.pushButton_8.text()))
        self.ui.pushButton_26.clicked.connect(self.delete)
        self.ui.pushButton_20.clicked.connect(self.clear)
        self.ui.pushButton_21.clicked.connect(self.calcul)
        self.ui.pushButton_3.clicked.connect(self.trg)
        self.window.show()
        self.p = self.ui.label.text()
    def write(self,ch):
        if ch=="x²":
            ch="^("
        if ch=="1/x":
            ch="^(-1)"
        t=self.ui.label.text()
        if t==self.p or t=="Erreur":
            self.ui.label.setText(ch)
        else:
            self.ui.label.setText(t+ch)
    def delete(self):
        t = self.ui.label.text()
        if t!=self.p:
            t=t[:len(t)-1]
            if t=="":
                self.ui.label.setText(self.p)
            else:
                self.ui.label.setText(t)
    def clear(self):
        self.ui.label.setText(self.p)
    def calcul(self):
        t=self.ui.label.text()
        test=False
        while(t.find("π")!=-1):
            t=t.replace("π",str(pi))
        for i in range(0,10):
            if str(i)in t:
                test=True
        if t=="" or test==False:
            self.ui.label.setText("Erreur")
            return
        t=result(t)
        if t=="":
            self.ui.label.setText("Erreur")
            return
        if float(t)==int(float(t)):
            t=str(int(float(t)))
        self.ui.label.setText(t)
    def trg(self):
        if self.ui.pushButton_8.text()=="sin":
            self.ui.pushButton_8.setText("1/x")
            self.ui.pushButton_19.setText("√")
            self.ui.pushButton_13.setText("x²")
        else:
            self.ui.pushButton_8.setText("sin")
            self.ui.pushButton_19.setText("cos")
            self.ui.pushButton_13.setText("tan")

