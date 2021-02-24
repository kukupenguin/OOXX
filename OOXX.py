def game_function():
    game=[[0]*3 for i in range(3)]
    print(game)
    rowstr=''
    list=[]
    times=0
    column=0
    row=0
    flag=True
    import os
    os.system("cls")
    for i in range(3):
        for j in range(3):
            game[i][j]="*"
    for i in range(3):
        for j in range(3):
            rowstr+=game[i][j]+' '
        print(rowstr)
        rowstr=''
    while(1):
        if times%2==0:
            print("\t\t輪到 O")
        else:
            print("\t\t輪到 X")
        print("輸入位置\n")
        while(1):
            row=input("第幾列")
            column=input("第幾行")
            if row.isdigit()==True and column.isdigit()==True:
                row=int(row)-1
                column=int(column)-1
                if row<=2 and row>=0 and column<=2 and column>=0:
                        if game[row][column]=="*":
                            break

                        else: 
                            print("\t重複!重新輸入!")
                else:
                    print("\t超出範圍!重新輸入!")
            else:
                print("\t錯誤!請輸入數字!")
        if times%2==0:
            game[row][column]="O"
        else:
            game[row][column]="X"
        times=times+1
        os.system("cls")
        for i in range(3):
            for j in range(3):
                rowstr+=game[i][j]+' '
            print(rowstr)
            rowstr=''
        list=[]
        for i in range(3):
            for j in range(3):
                list.append(game[i][j]) 
        #print(list)
        def check_function(n1,n2,n3):
            cstr=""
            cstr=list[n1]+list[n2]+list[n3]
            if cstr=="OOO" or cstr=="XXX":
                return True
        if check_function(0,1,2):
            break
        if check_function(0,3,6):
            break
        if check_function(0,4,8):
            break
        if check_function(1,4,7):
            break
        if check_function(2,4,6):
            break
        if check_function(2,5,8):
            break
        if check_function(3,4,5):
            break
        if check_function(6,7,8):
            break
        if times==9:
            print("\n\t平手\n")
            flag=False
            break
    if flag:
        if times%2==0:
            print("\n\t X 勝利!\n")
        else:
            print("\n\t O 勝利!\n")
    while(1):
        again=input("\t是否再玩一次 Y/N :")
        if again=='N' or again=='Y':
                return again
while (1):
    if game_function()!='Y':
        print("\n\t遊戲結束!\n")
        break