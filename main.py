from symbol import parameters
from tkinter import *
from definitionfunc import *
import itertools



def main():

    gui = Tk()
    
    gui.title("Quick Definitions")
    gui.geometry("500x500")
    gui['bg']='brown'
    test_label = Label(gui, text = 'Enter Word List', font=('calibre',10, 'bold'))


    def submit():
        output.delete("1.0","end")
        inputValue=text.get("1.0","end-1c")
        words = inputValue.split("\n")
        word_num = 0
        for word in words:
            word_num += 1
            if togglestate():
                outputdefinition(word_num,define.word(word,int(definitionlimit.get("1.0","end-1c"))))
            else:
                outputdefinition(word_num,define.word(word))


    def outputdefinition(word_num, definition):
        lets = ["A", "B","C"]

        if definition[0]:
            definition.pop(0)
            for (defin,letter) in zip(definition,lets):
                output.insert(INSERT,f"\n{word_num}{letter} ~ {defin}")
        else:
            output.insert(INSERT,"\n"+definition[1])

    def togglelimit():
        #toggles switch on and off
        definitionlimittoggle.config(text = {True:"True", False:"False"}[not eval(definitionlimittoggle.cget("text"))])
        if togglestate():
            limitlabel.grid(row=9,column=0)
            definitionlimit.grid(row=10,column=0)
        else:
            definitionlimit.grid_forget()
            limitlabel.grid_forget()

    def togglestate():
        return eval(definitionlimittoggle.cget("text"))



    togglelabel = Label(gui,text = "Definition limit toggle",font=('calibre',10, 'bold'))
    definitionlimittoggle = Button(gui,text = "False",command = togglelimit)
    limitlabel = Label(gui,text = "Enter max ammount of definitions",font=('calibre',10, 'bold'))
    definitionlimit = Text(gui,height = 1,width = 4)
    sub_btn= Button(gui,text = 'Submit', command = submit)
    text = Text(gui,height=8, width=40)
    outlabel = Label(gui, text = 'Definitions',font=('calibre',10, 'bold'))
    output = Text(gui,height = 10, width = 50)

    scroll = Scrollbar(gui)
    text.configure(yscrollcommand=scroll.set)

  
    scroll.config(command=text.yview)
    test_label.grid(row=0,column=0)
    text.grid(row=4,column=0,pady=10, padx=10)
    sub_btn.grid(row=4,column=1)
    outlabel.grid(row = 5, column = 0)
    output.grid(row=6,column = 0,pady=10, padx=1)
    togglelabel.grid(row=7,column=0)
    definitionlimittoggle.grid(row=8,column=0)





    #make sure this is at the bottom of code
    gui.mainloop()

if __name__ == '__main__':
    main()