from tkinter import *
from PIL import ImageTk,Image
# root = Tk()

# # root.geometry("500x350")
# root.resizable(width=False,height=False)
# root.title("Album")
# root.iconbitmap("albumIcon1.ico")

# gridspace = Label(root,text ="                  ").grid(row = 0,column = 0)
# heading = Label(root,text="Album",font = "arial 20 bold").grid(row = 1,column = 1)

# frame = Frame(root,width=300,height=300)
# frame.grid(row = 2,column = 1)
# frame.propagate(0)

# img_1 = ImageTk.PhotoImage(Image.open("contact.jpg"))
# img_2 = ImageTk.PhotoImage(Image.open("GoogleImage.jpg"))
# img_3 = ImageTk.PhotoImage(Image.open("google-reuters-2.jpg"))
# img_4 = ImageTk.PhotoImage(Image.open("newspaper.png"))

# albumlist = [img_1,img_2,img_3,img_4]

# my_lab = Label(frame,image=img_1)
# my_lab.grid(row=0,column=0)

# def showNext(num):
#     global my_lab
#     global btn_1 
#     global btn_2
#     if num == 3:
#         btn_1 = Button(root,text = "Next",state = "disable")
#     my_lab.grid_forget()
#     lab = Label(frame,image = albumlist[num],width = 300,height=300)
#     btn_2 = Button(root,text ="Next",command= lambda:showNext(num+1)).grid(row = 3,column= 2)
#     btn_1 = Button(root,text ="Previous",command= lambda:showPrev(num-1)).grid(row = 3,column= 0)

#     lab.grid(row=0,column=0)

# def showPrev(num):
#     global my_lab
#     global btn_1 
#     global btn_2
#     my_lab.grid_forget()
#     if num == 1:
#         btn_1 = Button(root,text = "Previous",state = "disable")
#     lab = Label(frame,image = albumlist[num-1],width = 300,height=300)
#     btn_1 = Button(root,text ="Previous",command= lambda:showPrev(num-1)).grid(row = 3,column= 0)
#     btn_2 = Button(root,text ="Next",command= lambda:showNext(num+1)).grid(row = 3,column= 2)
    
#     lab.grid(row=0,column=0)

# gridspace = Label(root,text ="                  ").grid(row = 0,column = 0)
# heading = Label(root,text="Album",font = "arial 20 bold").grid(row = 1,column = 1)



# # albumlocation = ["contact.jpg","GoogleImage.jpg","newspaper.png","google-reuters-2.jpg"]


# btn_1 = Button(root,text="Previous",command =showPrev).grid(row = 3,column= 0)
# btn_2 = Button(root,text="Next",command =lambda: showNext(0)).grid(row = 3,column = 2)


# root.mainloop()



root = Tk()
# root.geometry("600x600")

img_1 = ImageTk.PhotoImage(Image.open("contact.jpg"))
img_2 = ImageTk.PhotoImage(Image.open("GoogleImage.jpg"))
img_3 = ImageTk.PhotoImage(Image.open("google-reuters-2.jpg"))
img_4 = ImageTk.PhotoImage(Image.open("newspaper.png"))

albumlist = [img_1,img_2,img_3,img_4]

my_label = Label(image = img_1)
my_label.grid(row=0,column=0,columnspan=3)
def showNext(number):
    global my_label
    global btn_1
    global btn_2
    my_label.grid_forget()

    print(number)
    if number == 3:
        btn_2 = Button(root,text="Next",state=DISABLED)

    my_label = Label(image=albumlist[number],width = 500,height=500)
    btn_1 = Button(text ='Previous',command = lambda:showPrev(number-1))
    btn_2 = Button(text = "Next",command= lambda:showNext(number+1))
    
    my_label.grid(row=0,column=0,columnspan=3)
    btn_1.grid(row=1,column=0)
    btn_2.grid(row=1,column=2)
    
def showPrev(number):
    global my_label
    global btn_1
    global btn_2
    my_label.grid_forget()
    
    print(number)
    if number == 1:
        btn_1 = Button(root,text="Previous",state = DISABLED)
    
    my_label = Label(image=albumlist[number],width = 500,height=500)
    btn_1 = Button(text ='Previous',command = lambda:showPrev(number-1))
    btn_2 = Button(text = "Next",command= lambda:showNext(number+1))
    
    my_label.grid(row=0,column=0,columnspan=3)
    btn_1.grid(row=1,column=0)
    btn_2.grid(row=1,column=2)



btn_1 = Button(root,text="Previous",command =showPrev).grid(row = 1,column= 0)
btn_2 = Button(root,text="Next",command =lambda: showNext(1)).grid(row = 1,column = 2)

root.mainloop()