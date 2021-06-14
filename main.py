import random
import string
from colorama import Fore

def generator():
    result = []
    max_link = random.randint(2, 9)
    for i in range(1,max_link):
        r = random.randint(1, 2)
        if r == 1:
            result.append(random.choice(string.ascii_letters))
        elif r == 2:
            result.append(random.randint(0, 9))
    print("> https://prnt.sc/",*result, sep = '')

print(Fore.MAGENTA)
print('')
print('    __    _       __    __  _____ __          __     ______                           __            ')
print('   / /   (_)___ _/ /_  / /_/ ___// /_  ____  / /_   / ____/__  ____  ___  _________ _/ /_____  _____')
print('  / /   / / __ `/ __ \/ __/\__ \/ __ \/ __ \/ __/  / / __/ _ \/ __ \/ _ \/ ___/ __ `/ __/ __ \/ ___/')
print(' / /___/ / /_/ / / / / /_ ___/ / / / / /_/ / /_   / /_/ /  __/ / / /  __/ /  / /_/ / /_/ /_/ / /    ')
print('/_____/_/\__, /_/ /_/\__//____/_/ /_/\____/\__/   \____/\___/_/ /_/\___/_/   \__,_/\__/\____/_/     ')
print('        /____/                                                                                      ')
print('                                                                                     by MRK')
print('')
print(Fore.RESET)
print('Thanks for using LightShot Generator')
print('')
print(Fore.RED)
print('⛔', ' Please remember that a lot of the links are dead, use a checker or test them yourself.')
print(Fore.RESET)

linksWanted = int(input('How many links do you want ?       '))

def makeRandom():
    finishedLinks = 0
    while (finishedLinks < linksWanted):
        randomShit = generator()
        finishedLinks = finishedLinks + 1
        
print('')
makeRandom()

print(Fore.LIGHTGREEN_EX)
print('')
print("Done!")
print(Fore.MAGENTA,"-> donate: https://www.paypal.me/markaatioo")
print(Fore.RESET)