class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy Birthday to you",
    "I don't want to get sued",
    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
    "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

enten_song = ["Alle meine Entchen", "Schwimmen auf dem See",
    "Schwimmen auf dem See", "Koepfchen unter Wasser",
    "Schwaenzen in die Hoeh"]

alle_meine_entchen = Song(enten_song)

alle_meine_entchen.sing_me_a_song()

