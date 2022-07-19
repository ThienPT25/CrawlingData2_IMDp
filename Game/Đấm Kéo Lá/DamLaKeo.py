from random import randint

#Giả lập trò chơi đấm, kéo, lá 
#Khai báo cho computer
computer = randint(0,2)
if computer == 0:
    computer = "Dam"
elif computer == 1:
    computer = "Keo"
elif computer == 2:
    computer = "La"

#Khai báo cho player
player = input("Player choose: ")
while player != "Dam" and player != "Keo" and player != "La" :
    print("Nhập sai!")
    print("Mời bạn chọn lại!")
    player = input("Player choose: ")

#Đặt điều kiện so sanh player và computer
if player == computer:
    print("Computer choose: " + computer)
    print("Draw")
else:
    if player == "Dam":
        print("Computer choose: " + computer)
        if computer == "Keo":
            print("Win")
        else:
            print("Lose")
    elif player == "Keo":
        print("Computer choose: " + computer)
        if computer =="Dam":
            print("Lose")
        else:
            print("Win")
    elif player == "La":
        print("Computer choose: " + computer)
        if computer =="Dam":
            print("Win")
        else:
            print("Lose")