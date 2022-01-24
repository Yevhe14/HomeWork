class footballClub:
    title = ''
    city = ''
    soccer = 0

class championship:
    country = ''
    title_championship = ''
    list_comand = dict()

    def func(self):
        lose = 0
        for i in self.list_comand.values():
            if lose == 0:
                lose = i
            if i < lose:
                lose = i
        return lose

    def print(self):
        for i in self.list_comand:
            print(f"{i} - {self.list_comand.get(i)}")
        print(f"Командв з найгіршим результатом - {i} - {self.func(self)}")
            
LaLiga = championship
LaLiga.country = 'Spain'
LaLiga.title_championship = 'LaLiga'

RealMadrid = footballClub
RealMadrid.title = 'Real Madrid'
RealMadrid.city = 'Madrid'
RealMadrid.soccer = 14
LaLiga.list_comand['Real Madrid'] = RealMadrid.soccer

Barcelona = footballClub
Barcelona.title = 'Barcelona'
Barcelona.city = 'Barcelona'
Barcelona.soccer = 17
LaLiga.list_comand[Barcelona.title] = Barcelona.soccer

Atletiko = footballClub
Atletiko.title = 'Atletiko'
Atletiko.city = 'Madrid'
Atletiko.soccer = 12
LaLiga.list_comand[Atletiko.title] = Atletiko.soccer



LaLiga.print(LaLiga,)