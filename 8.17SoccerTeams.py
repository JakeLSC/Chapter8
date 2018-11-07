soccerTeam = {}
menuOption = 'a'

for i in range(5):
    playerNum = int(input('Enter player {}\'s jersey number:\n'.format(i + 1)))
    playerRate = int(input('Enter player {}\'s rating:\n'.format(i + 1)))
    print()
    soccerTeam[playerNum] = playerRate
        
print('ROSTER')
for key in sorted(soccerTeam.keys()):
    print('Jersey number: {},'.format(key), 'Rating:', soccerTeam[key])

while menuOption != 'q':    
    print('\nMENU')
    print('a - Add player')
    print('d - Remove player')
    print('u - Update player rating')
    print('r - Output players above a rating')
    print('o - Output roster')
    print('q - Quit\n')

    menuOption = input('Choose an option:\n')

    if menuOption == 'a':
        playerNum = int(input('Enter player {}\'s jersey number:\n'.format(i + 2)))
        playerRate = int(input('Enter player {}\'s rating:\n'.format(i + 2)))
        soccerTeam[playerNum] = playerRate
        i += 1

    elif menuOption == 'd':
        playerNum = int(input('Enter a jersey number:'))
        if playerNum in soccerTeam.keys():
            del soccerTeam[playerNum]

    elif menuOption == 'u':
        playerNum = int(input('Enter a jersey number: '))
        if playerNum in soccerTeam.keys():
            playerRate = int(input('Enter a new rating for player: '))
            soccerTeam[playerNum] = playerRate
        
    elif menuOption == 'r':
        playerRate = int(input('Enter a rating:\n'))
        print('ABOVE {}'.format(playerRate))
        for key in sorted(soccerTeam.keys()):
            if soccerTeam[key] > playerRate:
                print('Jersey number:',key, 'Rating:', soccerTeam[key])
        print()

    elif menuOption == 'o':
        print('ROSTER')
        for key in sorted(soccerTeam.keys()):
            print('Jersey number:',key,'Rating:',soccerTeam[key])
