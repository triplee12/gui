"""Scientific calculator"""
from tkinter import *
import Pmw


class SLable(Frame):
    """
    SLable defines a 2-sided label within a Frame. 
    The left hand label has blue letters; the right hand label 
    has white letters.
    """
    def __init__(self, master, left1, right1):
        Frame.__init__(self, master, bg="gray40")
        self.pack(side=LEFT, expand=YES, fill=BOTH)
        Label(self, text=left1, fg="steelblue1", font=(
            "Arial", 6, "bold"), width=5, bg="gray40"
        ).pack(side=LEFT, expand=YES, fill=BOTH)
        Label(self, text=right1, fg="#fff", font=(
            "Arial", 6, "bold"), width=1, bg="gray40"
        ).pack(side=RIGHT, expand=YES, fill=BOTH)


class Key(Button):
    """Key defines the button"""
    def __init__(self, master, font=("Arial", 8, "bold"), 
            fg="#fff", width=5, borderwidth=5, **kw):
        kw["font"] = font
        kw["fg"] = fg
        kw["width"] = width
        kw["borderwidth"] = borderwidth
        Button.__init__(self, master, kw)
        self.pack(side=LEFT, expand=NO, fill=NONE)


class Calculator(Frame):
    """Calculator"""
    def __init__(self, parent=None):
        Frame.__init__(self, bg="gray40")
        self.pack(expand=YES, fill=BOTH)
        self.master.title("Scientific Calculator")
        self.master.iconname("Sci-calc")
        self.calc = Evaluator()
        self.buildCalculator()

        # This is an incomplete dictionary - a good exercise!
        self.actionDict = {
            "second": self.doThis,
            "mode": self.doThis,
            "delete": self.doThis, "alpha": self.doThis,
            "stat": self.doThis, "math": self.doThis,
            "matrix": self.doThis, "program": self.doThis,
            "vars": self.doThis, "clear": self.clearall,
            "sin": self.doThis, "cos": self.doThis,
            "tan": self.doThis, "up": self.doThis,
            "X1": self.doThis, "X2": self.doThis,
            "log": self.doThis, "ln": self.doThis,
            "store": self.doThis, "off": self.turnoff,
            "neg": self.doThis, "enter": self.doEnter,
        }
        self.current = ""
    
    def doThis(self, action):
        print('"%s" has not been implemented' % action)
    
    def turnoff(self, action):
        """Turn off the calculator"""
        self.quit()
    
    def clearall(self, *args):
        """Clear the screen"""
        self.current = ""
        self.display.component('text').delete(1.0, END)
    
    def doEnter(self, *args):
        """Run command on 'Enter' button press"""
        self.display.insert(END, '\n')
        result = self.calc.runpython(self.current)
        if result:
            self.display.insert(END, "%s\n" % result, "ans")
        self.current = ""
    
    def doKeypress(self, event):
        """Keypress event handler"""
        key = event.char
        if key != '\b':
            self.current = self.current + key
        else:
            self.current = self.current[:-1]
    
    def keyAction(self, key):
        """Key action handler"""
        self.display.insert(END, key)
        self.current = self.current + key
    
    def evalAction(self, action):
        """Evaluate action handler"""
        try:
            self.actionDict[action](action)
        except KeyError:
            pass
    
    def buildCalculator(self):
        """Build calculator object"""
        FUN = 1
        KEY = 0
        KC1 = "gray30"
        KC2 = "gray50"
        KC3 = "steelblue1"
        KC4 = "steelblue"
        keys = [
            [('2nd', '', '', KC3, FUN, 'second'), # Row 1
            ('Mode', 'Quit', '', KC1, FUN, 'mode'),
            ('Del', 'Ins', '', KC1, FUN, 'delete'),
            ('Alpha','Lock', '', KC2, FUN, 'alpha'),
            ('Stat', 'List', '', KC1, FUN, 'stat')],
            [('Math', 'Test', 'A', KC1, FUN, 'math'), # Row 2
            ('Mtrx', 'Angle','B', KC1, FUN, 'matrix'),
            ('Prgm', 'Draw', 'C', KC1, FUN, 'program'),
            ('Vars', 'YVars','', KC1, FUN, 'vars'),
            ('Clr', '', '', KC1, FUN, 'clear')],
            [('X-1', 'Abs', 'D', KC1, FUN, 'X1'), # Row 3
            ('Sin', 'Sin-1','E', KC1, FUN, 'sin'),
            ('Cos', 'Cos-1','F', KC1, FUN, 'cos'),
            ('Tan', 'Tan-1','G', KC1, FUN, 'tan'),
            ('^', 'PI', 'H', KC1, FUN, 'up')],
            [('X2', 'Root', 'I', KC1, FUN, 'X2'), # Row 4
            (',', 'EE', 'J', KC1, KEY, ','),
            ('(', '{', 'K', KC1, KEY, '('),
            (')', '}', 'L', KC1, KEY, ')'),
            ('/', '', 'M', KC4, KEY, '/')],
            [('Log', '10x', 'N', KC1, FUN, 'log'), # Row 5
            ('7', 'Un-1', 'O', KC2, KEY, '7'),
            ('8', 'Vn-1', 'P', KC2, KEY, '8'),
            ('9', 'n', 'Q', KC2, KEY, '9'),
            ('X', '[', 'R', KC4, KEY, '*')],
            [('Ln', 'ex', 'S', KC1, FUN, 'ln'), # Row 6
            ('4', 'L4', 'T', KC2, KEY, '4'),
            ('5', 'L5', 'U', KC2, KEY, '5'),
            ('6', 'L6', 'V', KC2, KEY, '6'),
            ('-', ']', 'W', KC4, KEY, '-')],
            [('STO', 'RCL', 'X', KC1, FUN, 'store'), # Row 7
            ('1', 'L1', 'Y', KC2, KEY, '1'),
            ('2', 'L2', 'Z', KC2, KEY, '2'),
            ('3', 'L3', '', KC2, KEY, '3'),
            ('+', 'MEM', '"', KC4, KEY, '+')],
            [('Off', '', '', KC1, FUN, 'off'), # Row 8
            ('0', '', '', KC2, KEY, '0'),
            ('.', ':', '', KC2, KEY, '.'),
            ('(-)', 'ANS', '?', KC2, FUN, 'neg'),
            ('Enter','Entry','', KC4, FUN, 'enter')]
        ]
        self.display = Pmw.ScrolledText(self, hscrollmode="dynamic",
                            vscrollmode="dynamic", hull_relief="sunken",
                            hull_background="gray40", hull_borderwidth=10,
                            text_background="honeydew4", text_width=16,
                            text_foreground="black", text_height=6,
                            text_padx=10, text_pady=10, text_relief="groove",
                            text_font=("Arial", 12, "bold")
                        )
        self.display.pack(side=TOP, expand=YES, fill=BOTH)
        self.display.tag_config("ans", foreground="white")
        self.display.component("text").bind("<Key>", self.doKeypress)
        self.display.component("text").bind("<Return>", self.doEnter)

        for row in keys:
            rowa = Frame(self, bg="gray40")
            rowb = Frame(self, bg="gray40")
            for p1, p2, p3, color, ktype, func in row:
                if ktype == FUN:
                    a = lambda s=self, a=func: s.evalAction(a)
                else:
                    a = lambda s=self, k=func: s.keyAction(k)
                SLable(rowa, p2, p3)
                Key(rowb, text=p1, bg=color, command=a)
            rowa.pack(side=TOP, expand=YES, fill=BOTH)
            rowb.pack(side=TOP, expand=YES, fill=BOTH)


class Evaluator:
    """Evaluator class. This evaluate maths functions
    and execute system functions
    """
    def __init__(self):
        self.myNameSpace = {}
        self.runpython("from math import *")
    
    def runpython(self, code):
        try:
            return repr(eval(code, self.myNameSpace, self.myNameSpace))
        except SyntaxError:
            try:
                exec(code, self.myNameSpace, self.myNameSpace)
            except:
                return "Error"


Calculator().mainloop()