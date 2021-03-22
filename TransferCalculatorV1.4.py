# Program that allows for the calculation of player fees and reads/ writes from/ to a text file

import math


listOfPlayers = []
listHeadings = ['NAME', 'CLUB', 'AGE', 'HEIGHT', 'POSITION', 'WF ', 'SM', 'OVRL', 'PACE', 'SHOT', 'PASS', 'DRIB', 'DFND', 'PHYS']
columnOrder = [7, 8, 9, 10, 11, 12, 13, 5, 6]


# Open and read the player file line by line into a list and append the list to the listOfPlayers array
playerFile = open('FIFA21PlayerFile.txt', 'r', encoding='utf-8')
lines = playerFile.readlines()
for l in lines:
    asList = l.rstrip('\n').split(',')
    listOfPlayers.append(asList)


# While loop menu to take user input for what they would like to do
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
            addPlayer()
        elif menuOption.upper().strip() == 'QUIT':
            exit()
        else:
            print('Please enter a valid option')


# Takes the player information and prints it to the console in a properly formatted fashion
def playersFormatted(playerIndex):
    headingsFormat =  ''
    playersFormat = ''
    # Print the players name
    print(listOfPlayers[playerIndex][0])
    print('_'*66)
    for i in range(1):
        # Print in order of pre-determined column order
        for i in columnOrder:
            listLength = len(listHeadings[i]) 
            playerLength = len(str(listOfPlayers[playerIndex][i]))
            # Determines how many spaces it is to the nearest tab for top and bottom row and makes sure that columns are lined up
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


# Provides some formatting to differentiate between players
def spacer():
    print('_'*120)


# Checks the position in the array that holds the player position and runs the correct function per the player
def positionCheck(i):
    if listOfPlayers[i][4] == 'CM' or listOfPlayers[i][4] == 'RM' or listOfPlayers[i][4] == 'CAM' or listOfPlayers[i][4] == 'CDM' or listOfPlayers[i][4] == 'LM':
        midfielderCalculation(i)
    elif listOfPlayers[i][4] == 'LB' or listOfPlayers[i][4] == 'CB' or listOfPlayers[i][4] == 'RB' or listOfPlayers[i][4] == 'LWB' or listOfPlayers[i][4] == 'RWB':
        defenderCalculation(i)
    elif listOfPlayers[i][4] == 'ST' or listOfPlayers[i][4] == 'LW' or listOfPlayers[i][4] == 'RW' or listOfPlayers[i][4] == 'CF':
        attackerCalculation(i)
    elif listOfPlayers[i][4] == 'GK':
        goalkeeperCalculation(i)


# Allows the user to search for a player per specific stats
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
            # Checks each user input to see if there is a player(s) that matches and then runs the correct functions to format the player(s) if there are
            # Reversed range so that it prints the highest overall player last as this is probably the most relevant
            for i in reversed(range(len(listOfPlayers))):
                if listOfPlayers[i][7] >= overall and listOfPlayers[i][8] >=pace and listOfPlayers[i][9] >=shooting and listOfPlayers[i][10] >= passing and listOfPlayers[i][11] >= dribbling and listOfPlayers[i][12] >= defending and listOfPlayers[i][13] >= physical and listOfPlayers[i][5] >= weakFoot and listOfPlayers[i][6] >= skillMoves:
                    playerFound = True
                    playersFormatted(i)
                    positionCheck(i)
            if playerFound  == False:
                spacer()
                print('No players found')
                spacer()


# Allows the user to search for a player by name
def searchPlayer():
    loop = True
    while loop == True:
        playerFound = False
        searchInput = input('Enter the full name of the player you would like to search for (capitals are important) or press enter to quit: ')
        spacer()
        if searchInput.upper() == '':
            loop = False
        else:
            # Reversed range so that it prints the highest overall player last as this is probably the most relevant
            for i in reversed(range(len(listOfPlayers))):
                if searchInput in listOfPlayers[i][0]:
                    playerFound = True
                    playersFormatted(i)
                    positionCheck(i)
            if playerFound  == False:
                spacer()
                print('Player not found')
                spacer()


# Allows the user to search by club
def searchClub():
    loop = True
    while loop == True:
        playerFound = False
        searchInput = input('Enter the full name of the club you would like to search for (capital are important) or press enter to quit: ')
        spacer()
        if searchInput.upper() == '':
            loop = False
        else:
            # Reversed range so that it prints the highest overall player last as this is probably the most relevant
            for i in reversed(range(len(listOfPlayers))):
                if searchInput in listOfPlayers[i][1]:
                    playerFound = True
                    playersFormatted(i)
                    positionCheck(i)
            if playerFound  == False:
                spacer()
                print('Player not found')
                spacer()


# Allows the user to add a new player
def addPlayer():
    with open('FIFA21PlayerFile.txt', 'a') as writeFile:
        loop = True
        while loop == True:
            playerFound = False
            name = input('Input the name of the new player press enter to quit: ')
            if name.upper() == '':
                loop = False
            else:
                club = input('Club: ')
                age = input('Age: ')
                height = input('Height: ')
                position = input('Position: ')
                weakFoot = input('Weak Foot: ')
                skillMoves = input('Skill Moves: ')
                overall = input('Overall: ')
                pace = input('Pace: ')
                shooting = input('Shooting: ')
                passing = input('Passing: ')
                dribbling = input('Dribbling: ')
                defending = input('Defending: ')
                physical = input('Physical: ')
                writeFile.write(name + ',' + club + ',' + age + ',' + height + ',' + position + ',' + weakFoot + ',' + skillMoves + ',' + overall + ',' + pace + ',' + shooting + ',' + passing + ',' + dribbling + ',' + defending + ',' + physical) 
                print('Player has been added!')


# Calculates the player value if they are a midfielder
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


# Calculates the player value if they are an attacker
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


# Calculates the player value if they are a defender
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


# Calculates the player value if they are a goalkeeper
def goalkeeperCalculation(playerIndex):
    if int(listOfPlayers[playerIndex][7]) < 71:
        print('Transfer fee: 5')
    elif int(listOfPlayers[playerIndex][7]) == 71:
        print('Transfer fee: 7.5')
    elif int(listOfPlayers[playerIndex][7]) == 72:
        print('Transfer fee: 10')
    elif int(listOfPlayers[playerIndex][7]) == 73:
        print('Transfer fee: 12.5')
    elif int(listOfPlayers[playerIndex][7]) == 74:
        print('Transfer fee: 15')
    elif int(listOfPlayers[playerIndex][7]) == 75:
        print('Transfer fee: 17.5')
    elif int(listOfPlayers[playerIndex][7]) == 76:
        print('Transfer fee: 20')
    elif int(listOfPlayers[playerIndex][7]) == 77:
        print('Transfer fee: 22.5')
    elif int(listOfPlayers[playerIndex][7]) == 78:
        print('Transfer fee: 25')
    elif int(listOfPlayers[playerIndex][7]) == 79:
        print('Transfer fee: 27.5')
    elif int(listOfPlayers[playerIndex][7]) == 80:
        print('Transfer fee: 30')
    elif int(listOfPlayers[playerIndex][7]) == 81:
        print('Transfer fee: 32.5')
    elif int(listOfPlayers[playerIndex][7]) == 82:
        print('Transfer fee: 35')
    elif int(listOfPlayers[playerIndex][7]) == 83:
        print('Transfer fee: 37.5')
    elif int(listOfPlayers[playerIndex][7]) == 84:
        print('Transfer fee: 40')
    elif int(listOfPlayers[playerIndex][7]) == 85:
        print('Transfer fee: 42.5')
    elif int(listOfPlayers[playerIndex][7]) == 86:
        print('Transfer fee: 45')
    elif int(listOfPlayers[playerIndex][7]) == 87:
        print('Transfer fee: 47.5')
    elif int(listOfPlayers[playerIndex][7]) == 88:
        print('Transfer fee: 50')
    elif int(listOfPlayers[playerIndex][7]) == 89:
        print('Transfer fee: 52.5')
    elif int(listOfPlayers[playerIndex][7]) == 90:
        print('Transfer fee: 55')
    elif int(listOfPlayers[playerIndex][7]) == 91:
        print('Transfer fee: 57.5')
    elif int(listOfPlayers[playerIndex][7]) == 92:
        print('Transfer fee: 60')
    elif int(listOfPlayers[playerIndex][7]) == 94:
        print('Transfer fee: 62.5')
    spacer()


# Checks the overall rating of the player and applies a multiplier based on the overall rating that each player has
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
