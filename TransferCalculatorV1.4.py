# Program that allows for the calculation of player fees and reads/ writes from/ to a text file

import math

listOfPlayers = []
listHeadings = ['NAME', 'CLUB', 'AGE', 'HEIGHT', 'POSITION', 'WF ', 'SM', 'OVRL', 'PACE', 'SHOT', 'PASS', 'DRIB', 'DFND', 'PHYS']
columnOrder = [7, 8, 9, 10, 11, 12, 13, 5, 6]


playerFile = open('FIFA21PlayerFile.txt', 'r', encoding='utf-8')
lines = playerFile.readlines()
for l in lines:
    asList = l.rstrip('\n').split(',')
    listOfPlayers.append(asList)


def main():
    loop = True
    while loop == True:
        spacer()
        menuOption = input('Type \'Search\' if you wish to search for a player \n'
        'Type \'Add\' if you wish to add a player\n'
        'Type \'Quit\' to exit\n')
        spacer()
        if menuOption.upper().strip() == 'SEARCH':
            searchInput = input('Would you like to search by player, club or stats? Press enter to go back: ')
            if searchInput.upper() == 'PLAYER':
                searchPlayer()
            elif searchInput.upper() == 'CLUB':
                searchClub()
            elif searchInput.upper() == 'STATS':
                searchStats()
        elif menuOption.upper().strip() == 'ADD':
            print('Sorry, this menu option has yet to be added')
        elif menuOption.upper().strip() == 'QUIT':
            exit()
        else:
            print('Please enter a valid option')


def playersFormatted(playerIndex):
    headingsFormat =  ''
    playersFormat = ''
    print(listOfPlayers[playerIndex][0])
    print('_'*66)
    for i in range(1):
        for i in columnOrder:
            listLength = len(listHeadings[i]) 
            playerLength = len(str(listOfPlayers[playerIndex][i]))
            if listLength >= playerLength:
                difference = listLength - playerLength
                afterLongest = 8 - (listLength % 8)
                tabsNeeded = math.ceil((difference + afterLongest) / 8.0)
                headingsFormat += listHeadings[i] + '\t'
                playersFormat += listOfPlayers[playerIndex][i] + (tabsNeeded * '\t')
            elif playerLength > listLength:
                difference = playerLength - listLength
                afterLongest = 8 - (playerLength % 8)
                tabsNeeded = math.ceil((difference + afterLongest) / 8.0)
                headingsFormat += listHeadings[i] + (tabsNeeded * '\t')
                playersFormat += listOfPlayers[playerIndex][i] + '\t'
    print(headingsFormat)
    print(playersFormat)
    print('_'*66)


def spacer():
    print('_'*120)


def positionCheck(i):
    if listOfPlayers[i][4] == 'CM' or listOfPlayers[i][4] == 'RM' or listOfPlayers[i][4] == 'CAM' or listOfPlayers[i][4] == 'CDM' or listOfPlayers[i][4] == 'LM':
        midfielderCalculation(i)
    elif listOfPlayers[i][4] == 'LB' or listOfPlayers[i][4] == 'CB' or listOfPlayers[i][4] == 'RB' or listOfPlayers[i][4] == 'LWB' or listOfPlayers[i][4] == 'RWB':
        defenderCalculation(i)
    elif listOfPlayers[i][4] == 'ST' or listOfPlayers[i][4] == 'LW' or listOfPlayers[i][4] == 'RW' or listOfPlayers[i][4] == 'CF':
        attackerCalculation(i)
    elif listOfPlayers[i][4] == 'GK':
        goalkeeperCalculation(i)


def searchStats():
    loop = True
    while loop == True:
        playerFound = False
        overall = input('Overall or press enter to quit: ')
        if overall.upper() == '':
            loop = False
        else:
            pace = input('Pace: ')
            shooting = input('Shooting: ')
            passing = input('Passing: ')
            dribbling = input('Dribbling: ')
            defending = input('Defending: ')
            physical = input('Physical: ')
            weakFoot = input('Weak Foot: ')
            skillMoves = input('Skill Moves: ')
            spacer()
            for i in reversed(range(len(listOfPlayers))):
                if listOfPlayers[i][7] >= overall and listOfPlayers[i][8] >=pace and listOfPlayers[i][9] >=shooting and listOfPlayers[i][10] >= passing and listOfPlayers[i][11] >= dribbling and listOfPlayers[i][12] >= defending and listOfPlayers[i][13] >= physical and listOfPlayers[i][5] >= weakFoot and listOfPlayers[i][6] >= skillMoves:
                    playerFound = True
                    playersFormatted(i)
                    positionCheck(i)
            if playerFound  == False:
                spacer()
                print('No players found')
                spacer()


def searchPlayer():
    loop = True
    while loop == True:
        playerFound = False
        searchInput = input('Enter the full name of the player you would like to search for (capitals are important) or press enter to quit: ')
        spacer()
        if searchInput.upper() == '':
            loop = False
        else:
            for i in reversed(range(len(listOfPlayers))):
                if searchInput in listOfPlayers[i][0]:
                    playerFound = True
                    playersFormatted(i)
                    positionCheck(i)
            if playerFound  == False:
                spacer()
                print('Player not found')
                spacer()


def searchClub():
    loop = True
    while loop == True:
        playerFound = False
        searchInput = input('Enter the full name of the club you would like to search for (capital are important) or press enter to quit: ')
        spacer()
        if searchInput.upper() == '':
            loop = False
        else:
            for i in reversed(range(len(listOfPlayers))):
                if searchInput in listOfPlayers[i][1]:
                    playerFound = True
                    playersFormatted(i)
                    positionCheck(i)
            if playerFound  == False:
                spacer()
                print('Player not found')
                spacer()


def midfielderCalculation(playerIndex):
    pace = float(listOfPlayers[playerIndex][8]) * 2
    shooting = float(listOfPlayers[playerIndex][9]) * 1.5
    passing = float(listOfPlayers[playerIndex][10]) * 1.5
    dribbling = float(listOfPlayers[playerIndex][11]) * 1.5
    defence = float(listOfPlayers[playerIndex][12]) * 1.5
    physical = float(listOfPlayers[playerIndex][13]) * 1.5
    height = float(listOfPlayers[playerIndex][3]) * 0.5
    skillMoves = float(listOfPlayers[playerIndex][6]) * 20
    weakFoot = float(listOfPlayers[playerIndex][5]) * 20
    multiplier = ratingMultiplier(playerIndex)
    total = ((pace + shooting + passing + dribbling + defence + physical + height + skillMoves + weakFoot) / 40) * multiplier
    print('Transfer fee:', round(total, 2))
    spacer()


def attackerCalculation(playerIndex):
    pace = float(listOfPlayers[playerIndex][8]) * 2
    shooting = float(listOfPlayers[playerIndex][9]) * 2
    passing = float(listOfPlayers[playerIndex][10]) * 1.5
    dribbling = float(listOfPlayers[playerIndex][11]) * 1.5
    defence = float(listOfPlayers[playerIndex][12]) * 0.5
    physical = float(listOfPlayers[playerIndex][13]) * 1
    height = float(listOfPlayers[playerIndex][3]) * 0.5
    skillMoves = float(listOfPlayers[playerIndex][6]) * 20
    weakFoot = float(listOfPlayers[playerIndex][5]) * 20
    multiplier = ratingMultiplier(playerIndex)
    total = ((pace + shooting + passing + dribbling + defence + physical + height + skillMoves + weakFoot) / 40) * multiplier
    print('Transfer fee:', round(total, 2))
    spacer()


def defenderCalculation(playerIndex):
    pace = float(listOfPlayers[playerIndex][8]) * 2
    shooting = float(listOfPlayers[playerIndex][9]) * 0.5
    passing = float(listOfPlayers[playerIndex][10]) * 1.5
    dribbling = float(listOfPlayers[playerIndex][11]) * 1
    defence = float(listOfPlayers[playerIndex][12]) * 2
    physical = float(listOfPlayers[playerIndex][13]) * 1.5
    height = float(listOfPlayers[playerIndex][3]) * 0.5
    skillMoves = float(listOfPlayers[playerIndex][6]) * 10
    weakFoot = float(listOfPlayers[playerIndex][5]) * 20
    multiplier = ratingMultiplier(playerIndex)
    total = ((pace + shooting + passing + dribbling + defence + physical + height + skillMoves + weakFoot) / 40) * multiplier
    print('Transfer fee:', round(total, 2))
    spacer()


def goalkeeperCalculation(playerIndex):
    print('Sorry forgot the values lol')
    spacer()


def ratingMultiplier(playerIndex):   
    if int(listOfPlayers[playerIndex][7]) < 71:
        return float(1)
    elif int(listOfPlayers[playerIndex][7]) == 71:
        return float(1.2)
    elif int(listOfPlayers[playerIndex][7]) == 72:
        return float(1.4)
    elif int(listOfPlayers[playerIndex][7]) == 73:
        return float(1.6)
    elif int(listOfPlayers[playerIndex][7]) == 74:
        return float(1.8)
    elif int(listOfPlayers[playerIndex][7]) == 75:
        return float(2)
    elif int(listOfPlayers[playerIndex][7]) == 76:
        return float(2.2)
    elif int(listOfPlayers[playerIndex][7]) == 77:
        return float(2.4)
    elif int(listOfPlayers[playerIndex][7]) == 78:
        return float(2.6)
    elif int(listOfPlayers[playerIndex][7]) == 79:
        return float(2.8)
    elif int(listOfPlayers[playerIndex][7]) == 80:
        return float(3)
    elif int(listOfPlayers[playerIndex][7]) == 81:
        return float(3.2)
    elif int(listOfPlayers[playerIndex][7]) == 82:
        return float(3.4)
    elif int(listOfPlayers[playerIndex][7]) == 83:
        return float(3.6)
    elif int(listOfPlayers[playerIndex][7]) == 84:
        return float(3.8)
    elif int(listOfPlayers[playerIndex][7]) == 85:
        return float(4)
    elif int(listOfPlayers[playerIndex][7]) == 86:
        return float(4.2)
    elif int(listOfPlayers[playerIndex][7]) == 87:
        return float(4.4)
    elif int(listOfPlayers[playerIndex][7]) == 88:
        return float(4.6)
    elif int(listOfPlayers[playerIndex][7]) == 89:
        return float(4.8)
    elif int(listOfPlayers[playerIndex][7]) == 90:
        return float(5)
    elif int(listOfPlayers[playerIndex][7]) == 91:
        return float(5.2)
    elif int(listOfPlayers[playerIndex][7]) == 92:
        return float(5.4)
    elif int(listOfPlayers[playerIndex][7]) == 93:
        return float(5.6)
    elif int(listOfPlayers[playerIndex][7]) == 94:
        return float(5.8)


main()