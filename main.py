from bs4 import BeautifulSoup
import requests

from CrawlData import Craw
import tkinter as tk
import tkinter.messagebox as box



def Exit():
    var = box.askyesno( 'Message Box', 'Are you sure!!')
    if(var == 1):
        window.destroy()

def About():
    box.showinfo("", "This project was made by Phuc Hoang Pham ")

def Describe():
    box.showinfo("", "This project was made for tracking Covid-19")



def Set_up_for_menu(i):

    if i == 0:
        State_name.config(text='' + Country[i][:-5])
    else:
        State_name.config(text=''+Country[i])
    Total_Case.config(text='' + Data.get(Country[i])[0])
    Death.config(text='' + Data.get(Country[i])[2])
    Total_Recover.config(text='' + Data.get(Country[i])[4])
    New_Case.config(text='' + Data.get(Country[i])[1])
    New_Death.config(text='' + Data.get(Country[i])[3])
    Total_Test.config(text='' + Data.get(Country[i])[5])
    #print(Country[i])



window = tk.Tk()

craw = Craw()

Data = craw.Craw_data_from_web()

app_width = 500
app_height = 600

x = (window.winfo_screenwidth()/2) - (app_width/2)
y = (window.winfo_screenheight()/2) - (app_height/2)

Country = list(Data.keys())




#print(len(Country))

#print(Country[0][:-5])

#print((Data.get(Country[0]))[0])


# For the name state
State_name = tk.Label(window,text=""+Country[0][:-5], font = 'Helvetica 30 bold')
State_name.pack(pady = 10)

State_Case = tk.Label(window,text="Total Case", font = 'Helvetica 20 ')
State_Case.pack(pady = 0)

Total_Case = tk.Label(window,text=""+Data.get(Country[0])[0], font = 'Helvetica 20 bold', fg = 'grey')
Total_Case.pack(pady = 0)

State_Death = tk.Label(window, text="Total Death", font ='Helvetica 20 ')
State_Death.pack(pady = 0)

Death = tk.Label(window,text=""+Data.get(Country[0])[2], font = 'Helvetica 20 bold', fg = 'grey21')
Death.pack(pady = 0)

State_Recover = tk.Label(window, text="Total Recovered", font ='Helvetica 20')
State_Recover.pack(pady = 0)

Total_Recover = tk.Label(window,text=""+Data.get(Country[0])[4], font = 'Helvetica 20 bold', fg = 'green')
Total_Recover.pack(pady = 0)

State_new = tk.Label(window, text="New Case", font ='Helvetica 20')
State_new.pack(pady = 0)

New_Case = tk.Label(window,text=""+Data.get(Country[0])[1], font = 'Helvetica 20 bold', fg = 'orange')
New_Case.pack(pady = 0)


State_New_Death = tk.Label(window, text="New Death", font ='Helvetica 20')
State_New_Death.pack(pady = 0)

New_Death = tk.Label(window,text=""+Data.get(Country[0])[3], font = 'Helvetica 20 bold', fg = 'red')
New_Death.pack(pady = 0)

State_Test = tk.Label(window, text="Total Test", font ='Helvetica 20')
State_Test.pack(pady = 0)

Total_Test = tk.Label(window,text=""+Data.get(Country[0])[5], font = 'Helvetica 20 bold', fg = 'Blue')
Total_Test.pack(pady = 0)


menubar =tk.Menu(window)
window.config(menu=menubar)

filemenu = tk.Menu(menubar,tearoff = 0)

menubar.add_cascade(label='Option', menu=filemenu)

#filemenu.add_command(label='To Hexadecimal',command = ToHexadecimal)
for i in range(0,len(Country)):
    if i ==0:
        filemenu.add_command(label='' + Country[i][:-5], command=lambda i=i: Set_up_for_menu(i))
    else:
        filemenu.add_command(label='' + Country[i],command =lambda i=i: Set_up_for_menu(i))




filemenu.add_separator()
filemenu.add_command(label='Exit',command = Exit)


helpmenu = tk.Menu(menubar,tearoff = 0)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label='About...', command=About)
helpmenu.add_command(label='Describe',command = Describe)





window.geometry('%dx%d+%d+%d' % (app_width, app_height, x, y))

window.title('COVID19 in US- Tracking')



if __name__ == '__main__':
    window.mainloop()
