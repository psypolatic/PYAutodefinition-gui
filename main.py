from tkinter import *



def main():

    gui = Tk()
    
    gui.title("Quick Definitions")
    gui.geometry("500x500")
    gui['bg']='brown'
    gui.iconbitmap("appicon.ico")
    test_label = Label(gui, text = 'Test input', font=('calibre',10, 'bold'))


    def submit():
        inputValue=text.get("1.0","end-1c")
        print(inputValue.split("\n"))

    
    sub_btn= Button(gui,text = 'Submit', command = submit)
    text = Text(gui,height=8, width=40)

    scroll = Scrollbar(gui)
    text.configure(yscrollcommand=scroll.set)

  
    scroll.config(command=text.yview)
    test_label.grid(row=0,column=0)
    text.grid(row=4,column=0,pady=10, padx=10)
    sub_btn.grid(row=4,column=1)
    




    #make sure this is at the bottom of code
    gui.mainloop()

if __name__ == '__main__':
    main()

