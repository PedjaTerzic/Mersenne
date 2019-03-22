'''
    This script was written in python 3.x.
    In order to run this script, please make sure your python version is 3.x or above.
    How to run:
        python mersenne.py
    or if it doesn't work use this one:
        python3 mersenne.py
    Author: Pedja <pedja.terzic@hotmail.com>
'''
from mpmath import *
from sympy import *
from tkinter import *
import tkinter.messagebox
from tkinter.ttk import Frame, Label, Entry, Radiobutton, Button, Style

mp.dps = 500000; mp.pretty = True

class Mersenne(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("MERSENNE")
        self.pack(fill=BOTH, expand=True)
        global value
        value = 0
        global v
        v = IntVar()
        v.set(1)
        
        global base
        base = StringVar()
        global exp
        exp = StringVar()
        
        global res
        res = StringVar()

        frame1 = Frame(self,style='My.TFrame')
        frame1.pack(fill=X)
		
        
        rb1 = Radiobutton(frame1, text = "(b^p-1)/(b-1)", variable = v, value = 1,style='My.TRadiobutton')
        rb1.pack( anchor = W )
		
        rb2 = Radiobutton(frame1, text = "(b^p+1)/(b+1)", variable = v, value = 2,style='My.TRadiobutton')
        rb2.pack( anchor = W )
		
        
      
		
        frame2 = Frame(self,style='My.TFrame')
        frame2.pack(fill=X)

        lbl2 = Label(frame2, text="Enter the base :", width=18,background='orange')
        lbl2.pack(side=LEFT, padx=5, pady=5)

        entry2 = Entry(frame2,textvariable=base,style='My.TEntry')
        entry2.pack(fill=X, padx=5, expand=True)
		
        frame3 = Frame(self,style='My.TFrame')
        frame3.pack(fill=X)

        lbl3 = Label(frame3, text="Enter the exponent :", width=18,background='orange')
        lbl3.pack(side=LEFT, padx=5, pady=5)

        entry3 = Entry(frame3,textvariable=exp,style='My.TEntry')
        entry3.pack(fill=X, padx=5, expand=True)
		
       

        
        frame4 = Frame(self,style='My.TFrame')
        frame4.pack(fill=X)

        result = Label(frame4, textvariable=res, width=32,background='orange')
        result.pack(side=LEFT, padx=103, pady=5)

		
        frame5 = Frame(self,style='My.TFrame')
        frame5.pack(fill=X)

        btntest = Button(frame5, text="Test", width=10, command=self.test,style='My.TButton')
        btntest.pack(side=LEFT, anchor=N, padx=5, pady=5)
		
        btnclear = Button(frame5, text="Clear", width=10, command=self.clear,style='My.TButton')
        btnclear.pack(side=LEFT, anchor=N, padx=5, pady=5)
		
        btnclose = Button(frame5, text="Close", width=10, command=self.quit,style='My.TButton')
        btnclose.pack(side=LEFT, anchor=N, padx=5, pady=5)

    def errorMsg(self,msg):
        if msg == 'error':
            tkinter.messagebox.showerror('Error!', 'Something went wrong! Maybe invalid entries')
        elif msg == 'errc':
            tkinter.messagebox.showerror('Error!', 'Exponent must be a prime number')
        elif msg == 'errb':
            tkinter.messagebox.showerror('Error!', 'Base must be greater than one')
        elif msg == 'erre':
            tkinter.messagebox.showerror('Error!', 'Exponent must be greater than base')
			
    
        
    

    def test(self):
        try:
            
            b = int(base.get())
            n = int(exp.get())
            
			
            if not(isprime(n)):
                self.errorMsg('errc')
            elif b<2:
                self.errorMsg('errb')
            elif n<=b:
                self.errorMsg('erre')
            else:
				
                def polynomial(m,x):
                    if m==0:
                        return 2
                    elif m==1:
                        return x
                    else:
                        p0=2
                        p1=x
                        l=2
                        while l<=m:
                            p=x*p1-p0
                            p0=p1
                            p1=p
                            l=l+1
                        return p
                def jacobi(a,q):
                    j=1
                    while a != 0:
                        while a%2==0:
                            a=a/2
                            if q%8==3 or q%8==5:
                                j=-j
                        #interchange(a,q)
                        c=a
                        a=q
                        q=c
                        if a%4==3 and q%4==3:
                            j=-j
                        a=fmod(a,q)
                    if q==1:
                        return j
                    else:
                        return 0
               
            
                if v.get()==1:
                    M=(b**n-1)//(b-1)
                    d=3
                    while not(jacobi(d-2,M)==-1 and jacobi(d+2,M)==1):
                        d=d+1
                    s=polynomial(b,d)
                    
                    ctr=1
                    while ctr<=n-1:
                        s=polynomial(b,s)%M
                        ctr=ctr+1
                    if int(s)==polynomial(b-2,d):
                        value="probably prime"
                        res.set(self.makeAsItIs(value))
                    else:
                        value="composite"
                        res.set(self.makeAsItIs(value))
					
                else:
                    N=(b**n+1)//(b+1)
                    d=3
                    while not(jacobi(d-2,N)==-1 and jacobi(d+2,N)==1):
                        d=d+1
                    s=polynomial(b,d)
                    ctr=1
                    while ctr<=n-1:
                        s=polynomial(b,s)%N
                        ctr=ctr+1
                    if int(s)==polynomial(b+2,d):
                        value="probably prime"
                        res.set(self.makeAsItIs(value))
                    else:
                        value="composite"
                        res.set(self.makeAsItIs(value))

          
        except:
            self.errorMsg('error')
			
    def clear(self):
        try:
            res.set('')
            base.set('')
            exp.set('')
            
        except:
            self.errorMsg('error')
			
    
    def makeAsItIs(self, value):
        return value

def main():
    root = Tk()
    root.resizable(0,0)
    s = Style()
    s.configure('My.TFrame', background='orange')
    s.configure('My.TButton', background='light gray')
    s.configure('My.TEntry', fieldbackground='light gray')
    s.configure('My.TRadiobutton', background='orange')
    s.map('My.TRadiobutton', background=[('active', '#FFC133')])
    root.geometry("300x150")
    mersenne = Mersenne(root)
    root.mainloop()

if __name__ == '__main__':
    main()