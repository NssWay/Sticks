sticks = 15
print(sticks)
count = 1
def sum_sticks():
    global sticks
    global count
    if count % 2 == 1:   #подправить условие
        print('Player 1 you need')
    else:
        print('Player 2 you need')
    subtract = int(input('Enter the number from 1 to 3: '))
    print(sticks - subtract)
    sticks = sticks - subtract
    count += 1


game = True
while game:
    if sticks > 1:
        sum_sticks()
    else:
        game = False
        print('Game is over')
        print(count)
        if count // 2 == 0:
            print('!!!Player 1 win, player 2 lose!!!')
        else:
            print('!!!Player 2 win, player 1 lose!!!')