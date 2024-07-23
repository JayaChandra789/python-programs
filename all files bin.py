import pickle
def write():
    f=open("rkavanthi.bin",'wb')
    record=[]
    while True:
        rno=int(input("Enter roll number"))
        name=input("Enter Name")
        marks=int(input("Enter Marks"))
        data=[rno,name,marks]
        record.append(data)
        ch=input("You want to enter more records(Y/N)")
        if ch in 'Nn':
            break
    pickle.dump(record,f)
    print("Records added")
    f.close()
def read():
    print("Contents in a file is....")
    f=open("rkavanthi.bin",'rb')
    try:
        while True:
            s=pickle.load(f)
            for i in s:
                print(i)
    except Exception:
        f.close
def append():
    print("Appending file is...")
    f=open("rkavanthi.bin",'rb+')
    rec=pickle.load(f)
    while True:
        rno=int(input("Enter roll number"))
        name=input("Enter Name")
        marks=int(input("Enter Marks"))
        data=[rno,name,marks]
        rec.append(data)
        ch=input("You want to enter more records(Y/N)")
        if ch in 'Nn':
            break
    f.seek(0)
    pickle.dump(rec,f)
    print("Record appended Sucessfully....")
    f.close()
def search():
    f=open("rkavanthi.bin",'rb')
    r=int(input("Enter roll number to search..."))
    found=0
    try:
        while True:
            s=pickle.load(f)
            for i in s:
                print("Record is found....")
                print(i)
                found=1
                break
    except EOFError:
        f.close()
    if found==0:
        print("Sorry no records found")
def update():
    f=open("rkavanthi.bin",'rb+')
    r=int(input("Enter roll number whose details to be updated:"))
    f.seek(0)
    try:
        while True:
            rpos=f.tell()
            s=pickle.load(f)
            print(s)
            for i in s:
                if i[0]==r:
                    i[1]=input("Enter updated name")
                    i[2]=int(input("enter updated marks"))
                    f.seek(rpos)
                    pickle.dump(s,f)
                    break
    except Exception:
        f.close()
def delete():
    f=open("rkavanthi.bin",'rb')
    s=pickle.load(f)
    f.close()
    r=int(input("Enter roll number to be delete"))
    f=open("rkavanthi.bin",'wb')
    print(s)
    reclst=[]
    for i in s:
        if i[0]==r:
            continue
        reclst.append(i)
    pickle.dump(reclst,f)
    f.close()
def MainMenu():
    print("-"*50)
    print("1. Write data in a binary file")
    print("2. Read data from a binary file")
    print("3. Append data in a binary file")
    print("4. Search data in a binary file")
    print("5. Update data in a binary file")
    print("6. Delete data from a binary file")
    print("7. Exit")
    print("-"*50)
while True:
    MainMenu()
    ch=int(input("Enter Your choice"))
    if ch==1:
        write()
    elif ch==2:
        read()
    elif ch==3:
        append()
    elif ch==4:
        search()
    elif ch==5:
        update()
    elif ch==6:
        delete()
    elif ch==7:
        break
