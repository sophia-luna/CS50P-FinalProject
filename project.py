from random import randint
from pyfiglet import Figlet
import sys

def main():
    name=input("Your nickname: ")
    intro(name)
    while True:
        try:
            s=input().strip().lower()
            if s!="y" and s!="n":
                raise ValueError
        except:
            print("*press Y for Yes, or N for No.*")
        else:
            if s=='n':
                sys.exit("Grim Reaper: Goodbye.")
            break
    intro2()
    while True:
        try:
            level=int(input())
            if not acceptLevel(level):
                raise ValueError
        except:
            print("*Choose a level*")
            print("1 for Easy")
            print("2 for Standard")
            print("3 for Extreme")
        else:
            break

    guesses=set()
    ogWord=pickWord(level)
    lives=7
    word="_"*len(ogWord)
    while lives>0:
        display(word, lives)

        while True:
            try:
                guess=input("Guess: ").strip().lower()
                if not acceptGuess(guess):
                    raise ValueError
                if guess in guesses:
                    raise ValueError
            except:
                print("guess not accepted")
            else:
                guesses.add(guess)
                break

        if guess not in ogWord:
            lives-=1
        else:
            word=check(ogWord, word, guess)

        if word==ogWord:
            break

    if lives>0:
        display(word, lives)
        win(name)
    else:
        gameOver(name)

def gameOver(name):
    print("*You ran out of lives*\n")
    print(f"Grim Reaper: Well, {name}. I guess you're coming with me.")
    printAngel()
    figlet=Figlet()
    figlet.setFont(font="slant")
    print(figlet.renderText("GAME OVER"))

def win(name):
    print(f"Grim Reaper: Wow, {name}. You got me.")
    print("You can cross the bridge, good luck on your jorney.\n\n")
    printCat()
    figlet=Figlet()
    figlet.setFont(font="slant")
    print(figlet.renderText("    WIN"))

def check(og, word, guess):
    index=[]
    index.clear()
    for i in range(len(og)):
        if og[i]==guess:
            index.append(i)
    for i in index:
        word=word[:i]+guess+word[i+1:]
    return word

def acceptGuess(guess):
    letters=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    if guess in letters:
        return True
    return False

def acceptLevel(level):
    if 1<=level<=3:
        return True
    return False

def intro(name):
    print("\n")
    printCat()
    print(f"                  {name}")
    print("\n\n*You are a cat and every morning you leave the house and take a walk around the city.")
    print("    Today during your walk, you noticed a bridge and decided to explore it,")
    print("       but what you didn't expect was the appearance of the grim reaper.*\n\n\n")
    printGrimReaper()
    print(f"\nGrim Reaper: Hello, {name}. I have been waiting for you. Would you like to play a game?\n")
    print(f"*press Y for Yes, or N for No.*")


def intro2():
    print("\n\nGrim Reaper: You will have to guess the word I have in mind,")
    print("in order to cross the bridge. However, if you get it wrong")
    print(" you will have to follow another path with me hahaha\n")
    print("Grim Reaper: In Brazil, there is an old myth that cats are")
    print("believed to have 7 lives. Well, I can assure you it is true.")
    print(" You will have to guess the word I thought by guessing the ")
    print("  letters one by one and every time you guess a wrong ")
    print("      letter I will take one of yours lives.\n\n")
    print("*Choose a level*")
    print("1 for Easy")
    print("2 for Standard")
    print("3 for Extreme")

def pickWord(level):
    easy=["job", "hug", "cake", "ball", "list", "sad", "win", "flat", "size", "have", "give", "spot", "jam", "rest", "cute", "pile", "wipe", "dig", "one", "love", "rose", "tape", "help", "plum", "mud", "lose", "mine", "bell", "play", "sing", "bird", "tree", "rice", "dark", "moon", "cool", "ring", "bear", "pear", "dice"]
    normal=["abroad", "budget", "burden", "couple", "detail", "device", "casual", "artist", "strong", "chance", "danger", "church", "circle", "coffee", "beauty", "before", "amount", "animal", "corner", "deputy", "bottle", "bottom", "branch", "cactus", "castle", "bridge", "camera", "driver", "eleven", "dollar", "career", "bright", "closed", "change", "choice", "author", "course", "action", "august", "debate"]
    hard=["abruptly", "awkward", "jazz", "rhythm", "sphinx", "unknown", "whiskey", "pneumonia", "oxygen", "pajama", "nowadays", "lymph", "fuchsia", "exodus", "espionage", "embezzle", "blizzard", "psyche", "avenue", "quartz", "ovary", "scratch", "opponent", "simulation", "joker", "gecko", "enhance" "element", "ability", "anxiety", "chronic", "article", "eastern", "economy", "january", "factory", "fashion", "federal", "bachelor", "advanced", "business" ]
    num=randint(0,39)
    if level==1:
        return easy[num]
    if level==2:
        return normal[num]
    return hard[num]

def display(word, lives):
    figlet=Figlet()
    figlet.setFont(font="slant")
    print(figlet.renderText(word))
    hearts=""
    for _ in range(lives):
        hearts+="<3 "
    figlet=Figlet()
    figlet.setFont(font="slant")
    print(figlet.renderText(hearts))

def printCat():
    print("                ,_     _ ")
    print("                |\\\_,-~/")
    print("               / _  _ |    ,--.")
    print("              (  @  @ )   / ,-'")
    print("               \  _T_/-._( (")
    print("              /         `. \ ")
    print("             |         _  \ |")
    print("              \ \ ,  /     _|")
    print("               || |-_\__   /")
    print("              ((_/`(____,-'")

def printAngel():
    print("                           ___")
    print("                          (___)")
    print("                   ____")
    print("                 _\___ \  |\_/|")
    print("                \     \ \/ X X \ ___")
    print("                 \__   \ \ =T= //|||\ ")
    print("                 |===  \/____)_)|||||")
    print("                  \______|    | |||||")
    print("                      _/_|  | | =====")
    print("                     (_/  \_)_) ")
    print("                  __________________")
    print("                 (                 _)")
    print("                  (__   '         _)")
    print("                    (___    _____)")
    print("                        '--'")

def printGrimReaper():
    print('                                            .""--..__')
    print('                    _                      []       ``-.._')
    print("                  .'` `'.                  ||__           `-._")
    print('                 /    ,-.\                 ||_ ```---..__     `-.')
    print('                /    /:::\\               /|//}          ``--._  `.')
    print('                |    |:::||              |////}                `-. \ ')
    print("                |    |:::||             //'///                    `.\ ")
    print("                |    |:::||            //  ||'                      `| ")
    print("                /    |:::|/        _,-//\  ||")
    print("               /`    |:::|`-,__,-'`  |/  \ ||")
    print("             /`  |   |'' ||           \   |||")
    print('           /`    \   |   ||            |  /||')
    print('         |`       |  |   |)            \ | ||')
    print('        |          \ |   /      ,.__    \| ||')
    print('        /           `         /`    `\   | ||')
    print('       |                     /        \  / ||')
    print('       |                     |        | /  ||')
    print('       /         /           |        `(   ||')
    print('      /          .           /          )  ||')
    print('     |            \          |     ________||')
    print('   /             |          /     `-------.|')
    print('   |\            /          |              ||')
    print('   \/`-._       |           /              ||')
    print('    //   `.    /`           |              ||')
    print('   //`.    `. |             \              ||')
    print('  ///\ `-._  )/             |              ||')
    print(' //// )   .(/               |              ||')
    print(" ||||   ,'` )               /              //")
    print(' ||||  /                    /             || ')
    print(' `\\` /`                    |             // ')
    print('     |`                     \            ||  ')
    print('    /                        |           //  ')
    print('  /`                          \         //   ')
    print('/`                            |        ||    ')
    print("`-.___,-.      .-.        ___,'        (/    ")
    print("         `---'`   `'----'`")

if __name__ == "__main__":
    main()