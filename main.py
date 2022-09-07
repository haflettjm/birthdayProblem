'''The Birthday Paradox, also called the Birthday Problem, is the surprisingly high
probability that two people will have the same birthday even in a small group of people. In a group of 70 people, there’s a 99.9 percent chance
of two people having a matching birthday. But even in a group as small as 23 people, there’s a 50 percent chance of a matching birthday. This program per-
forms several probability experiments to determine the percentages for groups of different sizes. We call these types of experi-
ments, in which we conduct multiple random trials to understand the likely outcomes, Monte Carlo experiments.
'''

from random import randint


#generate random birthdays
def getNumberToMake():
    amount = int(input("How many birthdays shall I generate?\n"))
    return amount

#generate the random birthdays

def ranBirthday():
    # generate the month
    months = ['Jan','Feb','March','April','May','June','July','Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    monthRand = months[randint(0,11)]
    day30Month = ['April', 'June', 'Sep','Nov']
    if monthRand == 'Feburary':
        day = str(randint(1,28))
    elif monthRand in day30Month:
        day = str(randint(1,30))
    else:
        day = str(randint(1,31))

    birthday = monthRand + ' ' + day
    return birthday


#generate the amount of birthdays for the given group
def amountBirthdays(amount):
    birthdays = []
    for num in range(amount):
        birthdays.append(ranBirthday())

    return birthdays

def comparison(birthdays):
    #get empty list of matching birthdays
    matchingBirthdays = []

    #for the current grab the birth in the enumerated birthday list
    for index, birth in enumerate(birthdays):
        #for the second value iterate through the list except for the last value
        for value in birthdays[index+1:]:
            if birth == value:
                if birth not in matchingBirthdays:
                    matchingBirthdays.append(birth)



    return matchingBirthdays
#main logic
def main():
    #get the number of birthdays to generate
    amount = getNumberToMake()
    #generate those birthdays
    birthdays = amountBirthdays(amount)

    #print out the birthdays
    print('Here are the birthdays generated:\n')
    print(*birthdays, sep=", ")
    print('\n')

    #do comparison
    matchingBirths = comparison(birthdays)
    if len(matchingBirths) != 0:
        print("There were multiple births on these days:", *matchingBirths, sep=" ")
    else:
        print("There were no matching births this time!")

    #Determine Probability for group sizes

    #Multiple random trials

    #figure out how many different pairs there are

    #(groupSize * groupSize -1) / 2individuals = Set of comparisons


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
