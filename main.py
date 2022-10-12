from tkinter import *



def main():

    gui = Tk()
    
    gui.title("Quick Definitions")
    gui.geometry("500x500")
    gui['bg']='brown'
    test_label = Label(gui, text = 'Enter Word List', font=('calibre',10, 'bold'))


    def submit():
        inputValue=text.get("1.0","end-1c")
        words = inputValue.split("\n")
        print(words)
        output.insert(INSERT,f"you typed {len(words)} words ")

    def outputdefinition(definition):
        output.insert(INSERT,definition)
        #new lines
        output.insert(INSERT, "\n")

    
    sub_btn= Button(gui,text = 'Submit', command = submit)
    text = Text(gui,height=8, width=40)
    outlabel = Label(gui, text = 'Definitions')
    output = Text(gui,height = 10, width = 50)

    scroll = Scrollbar(gui)
    text.configure(yscrollcommand=scroll.set)

  
    scroll.config(command=text.yview)
    test_label.grid(row=0,column=0)
    text.grid(row=4,column=0,pady=10, padx=10)
    sub_btn.grid(row=4,column=1)
    outlabel.grid(row = 5, column = 0)
    output.grid(row=6,column = 0,pady=10, padx=1)
    




    #make sure this is at the bottom of code
    gui.mainloop()

if __name__ == '__main__':
    main()