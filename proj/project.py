import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from promptpay import qrcode
from PIL import Image,ImageTk


addmenu = []
addface = []
addtopping = []
addcount = []
addprice = []

Pizzadough_list = ["Soft Crust Pizza","Crust Pizza"]   
Topping_list = ["Seafood","Tom Yum Kung","Hawaiian","Double Cheese","Spicy Seafood","Cheese & Bacon","Classic Mushroom"]
Addtopping_list = ["Mozzarella Cheese","Bacon Bits","Mushrooms","Prawn","Seafood","Red & Green Chilli","Tomato"]
Drink_list = ["Mineral Water","Beer","Cola","Soda","Orange juice","Watermelon"]
total_detail={'Soft Crust Pizza':150,'Crust Pizza':150,'Mozzarella Cheese':25,'Bacon Bits':40,'Mushrooms':15,'Prawn':20,'Seafood':40,'Tomato':10
              ,'Mineral Water':15,'Beer':50,'Cola':25,'Soda':15,'Orange juice':30,'Watermelon':30,'':0}

totalprice = 0


def pay():

    payy = tk.Toplevel()
    payy.resizable(False, False)
    payy.geometry('200x240')

    ttk.Label(payy,text=f'Payment : {totalprice} Baht').pack(pady=10)

    id_or_phone_number = '1209301141511'
    payload_with_amount = qrcode.generate_payload(id_or_phone_number, totalprice)

    # export to PIL image
    img23 = qrcode.to_image(payload_with_amount)
    img23.save('qr.png')

    image = Image.open('qr.png')
    re_im = image.resize((150, 150))
    tkim = ImageTk.PhotoImage(re_im,payy)
    label = ttk.Label(payy, image=tkim)
    label.pack()
    ttk.Label(payy,text='วุฒินันท์ ภูมิประหมัน').pack(pady=10)
    payy.mainloop()

def click(action,table):
    global totalprice,wcount,watervar,facevar,topvar,radiovar,dcount
    if action == "Add":
        waterh = water.get()
        watercount = wc.get()
        pizza = radiovar.get()
        facepizza = face.get()
        toppizza = topping.get()
        pizzad = dc.get()
        if pizza != '0':
            if facepizza == "":
                messagebox.showinfo(title='Error',message='กรุณาเลือกหน้าพิซซ่า')
            
            elif pizzad == "":
                messagebox.showinfo(title='Error',message='กรุณาใส่จำนวน')

            else:
                price = (total_detail[pizza] + total_detail[toppizza]) * int(pizzad)
                totalprice += price
                total.configure(text=totalprice)
                content = [pizza,facepizza,toppizza,pizzad,price]
                table.insert('',tk.END,values=content)
                addmenu.append(pizza)
                addface.append(facepizza)
                addtopping.append(toppizza)
                addcount.append(pizzad)
                addprice.append(price)
                radiovar.set(0)
                facevar.set('')
                topvar.set('')
                dcount.set('')


        if waterh:
            if watercount == "":
                messagebox.showinfo(title='Error',message='กรุณาใส่จำนวน')
                
            else:
                price = total_detail[waterh] * int(watercount)
                totalprice += price
                total.configure(text=totalprice)
                content = [waterh,"","",watercount,price]
                table.insert('',tk.END,values=content)
                wcount.set('')
                watervar.set('')
                addmenu.append(waterh)
                addface.append("")
                addtopping.append("")
                addcount.append(watercount)
                addprice.append(price)
                

    elif action == "Delete":
        for select_item in table.selection():

            item = table.item(select_item)
            # *** ตัดต่อ Strint เพื่อใส่ 0 หน้า id
            record = item['values']
            id = str(record[0])
            idx = addmenu.index(id)
            if idx >= 0:
                answer = messagebox.askyesno(title='ยืนยันการลบ',
                                  message='คุณต้องการลบรายการนี้หรือไม่?')
                if answer:
                    totalprice -= addprice[idx]
                    total.configure(text=totalprice)

                    addmenu.pop(idx)
                    addface.pop(idx)
                    addtopping.pop(idx)
                    addprice.pop(idx)
                    addcount.pop(idx)

                    # ***  ค่า idx ออกจาก Tree
                    table.delete(select_item)

    elif action == "Close":
        root.destroy()
        print('Program is closed')

    elif action == 'Pay':
        pay()

def create_grade_table(container):
    # กำหนดคอลัมน์ของตาราง
    columns = ('menulist','face', 'topping', 'count', 'total')
    tree = ttk.Treeview(container, columns=columns, show='headings')

    # สร้างหัวข้อคอลัมน์ของตาราง
    tree.heading('menulist', text='รายการ')
    tree.heading('face', text='หน้าพิซซ่า')
    tree.heading('topping', text='ท็อปปิ้ง')
    tree.heading('count', text='จำนวน')
    tree.heading('total', text='ราคา')

    # กำหนดความกว้างของคอลัมน์
    tree.column("menulist", minwidth=0, width=90, stretch=NO)
    tree.column("face", minwidth=0, width=90, stretch=NO)
    tree.column("topping", minwidth=0, width=90, stretch=NO)
    tree.column("count", minwidth=0, width=40, stretch=NO)
    tree.column("total", minwidth=0, width=50, stretch=NO)
    return tree

root = tk.Tk()
root.title('Pizza')
root.resizable(False,False)
root.geometry('400x400')

#button
addbutton = ttk.Button(root,text='Add',command=lambda: click('Add',menu_table))
addbutton.place(x=320,y=5)
deletebtn = ttk.Button(root,text='Delete',command=lambda: click('Delete',menu_table))
deletebtn.place(x=320,y=40)
closebtn = ttk.Button(root,text='Close',command=lambda: click('Close',menu_table))
closebtn.place(x=320,y=75)
billbtn = ttk.Button(root,text='Pay',command=lambda:click('Pay',menu_table))
billbtn.place(x=320,y=360)
memberbtn = ttk.Button(root,text='Member')
memberbtn.place(x=10,y=360)

#label
ttk.Label(root,text='เลือกแป้ง:').place(x=10,y=5)
ttk.Label(root,text='เลือกหน้า:').place(x=10,y=30)
ttk.Label(root,text='เลือกท็อปปิ้ง:').place(x=10,y=55)
ttk.Label(root,text='เลือกเครื่องดื่ม:').place(x=10,y=80)
ttk.Label(root,text='จำนวน').place(x=250,y=30)
ttk.Label(root,text='Total : ').place(x=200,y=365)
total = ttk.Label(root,text='0',foreground='green',font=5)
total.place(x=235,y=360)

#entry count
countvalues = [1,2,3,4,5]
dcount = tk.StringVar()
dc = ttk.Combobox(root,width=4,textvariable=dcount,values=countvalues)
dc.place(x=245,y=55)
wcount = tk.StringVar()
wc = ttk.Combobox(root,width=4,textvariable=wcount,values=countvalues)
wc.place(x=245,y=80)

#choose
radiovar = tk.StringVar()
radiovar.set(0)
facevar = tk.StringVar()
topvar = tk.StringVar()
watervar = tk.StringVar()

dough = ttk.Radiobutton(root,text=Pizzadough_list[0],value=Pizzadough_list[0],variable=radiovar)
dough.place(x=90,y=5)
dough1 = ttk.Radiobutton(root,text=Pizzadough_list[1],value=Pizzadough_list[1],variable=radiovar)
dough1.place(x=200,y=5)
face = ttk.Combobox(root,width=20,values=Topping_list,textvariable=facevar)
face.place(x=90,y=30)
topping = ttk.Combobox(root,width=20,values=Addtopping_list,textvariable=topvar)
topping.place(x=90,y=55)
water = ttk.Combobox(root,width=20,values=Drink_list,textvariable=watervar)
water.place(x=90,y=80)

#scrollbar
menu_table = create_grade_table(root)
menu_table.place(x=10,y=120)
# สร้าง scrollbar สำหรับตาราง grade_table
scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=menu_table.yview)
menu_table.configure(yscroll=scrollbar.set)
scrollbar.place(x=375,y=120)

root.mainloop()