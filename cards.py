from faker import Faker
fake = Faker()

class Card():
    
    def __init__ (self, first_name, last_name, company, e_mail):
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.e_mail = e_mail

    @property
    def name_lenght(self):
        return len(self.first_name+' '+self.last_name)

    def __str__(self):
       return f'{self.first_name}, {self.last_name}, {self.e_mail}'

    def contact(self):
        return print(f'Kontaktuję się z {self.first_name}, {self.last_name}, {self.e_mail}')



def fake_card() :
    first_name = fake.first_name()
    last_name = fake.last_name()
    company = fake.company()
    e_mail = first_name+last_name+'@'+company.lower().replace(",","-").replace(" ", "")+'.com'
    name = first_name+" "+last_name
    name = Card(first_name, last_name, company, e_mail) 
    return name


#cards = []
#numb = int(input('How many fake cards: '))
#for i in range (numb):
#    card = fake_card()
 #   card = Card(card.first_name, card.last_name, card.company, card.e_mail)
  #  cards.append(card)

#for card in cards:
#    print(card)

#by_first_name = sorted(cards, key=lambda card: card.first_name)
#by_last_name = sorted(cards, key=lambda card: card.last_name)
#by_e_mail = sorted(cards, key=lambda card: card.e_mail)
