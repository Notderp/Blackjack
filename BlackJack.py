from logging import exception
import random

#==================================== klasa gracz, atrybuty i metody
class Player:
    PlayerTurn=0
    @staticmethod
    def comparePlayers(listOfPlayers):
        totalScores= []
        values=[]

        for player in listOfPlayers:
            if player.total>21:
                totalScores.append((player.name, (-player.total)))
                values.append(-player.total)
                print('wynik gracza {}: {}'.format(player.name,player.total))
            else:
                totalScores.append((player.name, player.total))
                values.append(player.total)
                print('wynik gracza {}: {}'.format(player.name, player.total))
        values.sort()
        remisNumber=values.count(values[len(values)-1])
        winner = sorted(totalScores, key=lambda player: player[1])
        if remisNumber >1:
            b=1
            print("remis graczy:")
            for a in range(remisNumber):
                print(winner[len(winner)-b][0])
                b+=1
        else:
            print('zwycieza gracz {} z liczba punktow {}'.format(winner[len(winner)-1][0],winner[len(winner)-1][1]))

    def __init__(self,name):
        self.hand=[]
        self.name=name
        self.turn=Player.PlayerTurn
        self.total=0
        Player.PlayerTurn+=1
        listOfPlayers.append(self)
        self.isActive=True

    def MakeDecision(self,tally):
        self.Count_Hand()
        option=0
        if self.total >21:
            option='2'
        else:
            print("kolej gracza {}\n1:dobierz karte\n2:pasuj".format(self.name))
            option = input('wybierz opcje: ')

        if option == "2":
            print("gracz {} spasowal.".format(self.name))
            self.isActive = False
            Player.PlayerTurn -= 1
        elif option=='1':
            self.Pick_Card(tally)
        else:
            print('dupa naucz sie czytac debilu - tracisz kolejke')

    def Pick_Card(self,deck):
        card=random.choice(deck)
        print('gracz {} wylosowal karte {}'.format(self.name,card))
        self.hand.append(card)
        deck.remove(card)
    def Count_Hand(self):
        self.total=0
        values=[]
        for CardType,CardValue in self.hand:
            values.append(CardValue)
            match CardValue:
                case 'walet':
                    self.total+=2
                case 'dama':
                    self.total+=3
                case 'krol':
                    self.total += 4
                case 'as':
                    self.total+=11
                case _:
                    self.total+=CardValue
        if "as" in values and self.total<21:
            self.total-=10
        if  len(values)==2 and values[0]=='as' and values[1]=='as':
            self.total=21
        print('wartosc kart gracza {} w rece: {}'.format(self.name,self.total))
        print('karty gracza {} w rece: {}'.format(self.name,self.hand))

#=========================================== FUNKCJE, LOGIKA GRY

def create_deck():
    typ = ['karo', 'trefl', 'kier', 'pik']
    numer = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'walet', 'dama', 'krol', 'as']
    deck = []
    for t in typ:
        for n in numer:
            deck.append((t, n))
    random.shuffle(deck)
    return deck.copy()

def LetsGame(Pl_list, Cardtalia):
    while Player.PlayerTurn >0:
        for player in Pl_list:
            if player.isActive:
                print("="*20)
                player.MakeDecision(Cardtalia)
    print('koniec gry')
    Player.comparePlayers(Pl_list)

def utworzGracza(a,imionaGraczy):
    imie = input('podaj nazwe gracza numer {}: '.format(a + 1))
    try:
        if imie in imionaGraczy:
            raise exception('')
        exec("{}=Player('{}')".format(imie,imie))
        imionaGraczy.append(imie)

    except:
        print('cos poszlo nie tak, podaj inne imie')
        utworzGracza(a,imionaGraczy)

def Create_Players(anop):
    imionaGraczy=[]
    for a in range(anop):
        utworzGracza(a,imionaGraczy)

def Set_Player_Number():
    numberOfPlayers=''
    numberOfPlayers = input('Podaj liczbę graczy: ')
    try:
        int(numberOfPlayers)
        if int(numberOfPlayers) < 1:
            print("za mala liczba graczy")
            return Set_Player_Number()
        elif int(numberOfPlayers) >4:
            print("za duza liczba graczy")
            return Set_Player_Number()
        elif (int(numberOfPlayers) <=4) and (int(numberOfPlayers) >=1):
            return  int(numberOfPlayers)
    except:
        print("cos poszlo nie tak")
        return Set_Player_Number()

# ===================================== CZESC WYWOLAWCZA

listOfPlayers = []
talia=create_deck()
print("Witaj w grze BlackJack")
nop=Set_Player_Number()
Create_Players(nop)
LetsGame(listOfPlayers, talia)
