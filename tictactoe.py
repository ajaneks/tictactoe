from tkinter import *​
from tkinter import messagebox #paziņojumi, ieteikumi​
mansLogs=Tk() # loga objekts​
mansLogs.title("TicTacToe")

speletajsX=True #kuram spēlētājam kārta spēlēt, liks krustiņus​
count=0 #aizpildīto rūtiņu skaits

galvenaIzvelne=Menu(mansLogs)#izveido galveno izvēlni​
mansLogs.config(meu=galvenaIzvelne)#pievieno galvenajam logam
#Mazā izvēlne​

opcijas=Menu(galvenaIzvelne,tearoff=False)#mazā izvēlne​

galvenaIzvelne.add_cascade(label="Opcijas",menu=opcijas)​

#lejupkrītošais saraksts




def btnClick(button): #padod visu pogu​
   global speletajsX,count #kādi mainīgie tiks izmantoti visā programmā​
   if button["text"]==" "and speletajsX==True:#spēlē X spēlētājs​
        button["text"]="X"#maina uz X​

        speletajsX=False​

        count+=1 # palielina rūtiņu skaitu


def checkWinner():​

    global winner​

     winner=False #noteiks, ja būs neizšķirts​

if (btn1["text"]=="X"and btn2["text"]=="X" and btn3["text"]=="X" or​

btn4...):​


def reset():​
    btn1.config(state=NORMAL)​
…..​

btn1["text"]=" "

  global winner, count, speletajsX​

    winner=False​

    count=0​

    speletajsX=False​




winner=True​
messagebox.showinfo("TicTacToe","SpeletajsX ir uzvarētājs")​
elif (btn1["text"]=="O"and btn2["text"]=="O" and btn3["text"]=="O" or...):​
winner=True​
messagebox.showinfo("TicTacToe","SpeletajsO ir uzvarētājs")
elif count==9 and winner==False:​
messagebox.showinfo("TicTacToe", "Neizšķirts")
 winner=True
 ​
   disableButtons()

def disableButtons(): #spēle beidzas, pogas izslēgtas​

   btn1.config(state=DISABLED) #pogas stāvoklis izslēgts



elif button["text"]==" " and speletajsX==False: # mainās spēlētāji​

        button["text"]="0"​

        speletajsX=True​

        count+=1​

else:​

        messagebox.showerror("TicTacToe","Šeit kāds ir ieklikšķinājis!")


btn1=Button(mansLogs,text=" ",width=6,height=3,font=('Helvica',24),command=lambda:btnClick(btn1))

…....btn9 #nepieciešamas 9 pogas​

​

btn1.grid(row=0,column=0) #pievieno pogas ​
btn2.grid(row=0,column=1)​
btn3.grid(row=0,column=2)​

…..​




mansLogs.mainloop()