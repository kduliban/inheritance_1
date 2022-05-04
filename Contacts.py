class BaseContact:
    def __init__ (self, first_name, last_name, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email


    def __str__(self):
       return f'{self.first_name}, {self.last_name}, {self.phone_number}, {self.email}'

    
    def contact(self):
        return f'Wybieram numer {self.phone_number} i dzwonię do {self.first_name} {self.last_name}'


    @property
    def name_lenght(self):
        return len(self.first_name+' '+self.last_name)


    
class BusinessContact(BaseContact):
    def __init__(self, first_name, last_name, phone_number, email, position, company, business_phone):
        super().__init__(first_name, last_name, phone_number, email)
        self.position = position
        self.company = company
        self.business_phone = business_phone

    
    def __str__(self):
       return f'{self.first_name}, {self.last_name}, {self.phone_number}, {self.email}, {self.position}, {self.company}, {self.business_phone}'


    def contact(self):
        return f'Wybieram numer {self.business_phone} i dzwonię do {self.first_name} {self.last_name}'



from faker import Faker
fake = Faker()
import random


def create_contacts(sort = None, numb = None):
    sort = input('What type of card: base(1) or business(2): ')
    numb = int(input('How many cards?: '))

    if sort == '1':
        for i in range (numb):    
            first_name = fake.first_name()
            last_name = fake.last_name()
            phone_number = f'+48 {random.randint(100000000,999999999)}'
            email = first_name+last_name+fake.ascii_company_email()
            name = first_name.title()+last_name.title()
            name = BaseContact(first_name, last_name, phone_number, email)
            #print(name) 
    elif sort =='2':
        for i in range (numb): 
            first_name=fake.first_name()
            last_name=fake.last_name()
            phone_number=f'+48 {random.randint(100000000,999999999)}'
            email=first_name+last_name+fake.ascii_company_email()
            name = first_name.title()+last_name.title()
            position=fake.job()
            company=fake.company()
            business_phone=f'+48 {random.randint(100000000,999999999)}'
            name=BusinessContact(first_name, last_name, phone_number, email, position, company, business_phone)
            #print(name)
    else:
        return 'Zły input. Proszę spróbować jeszcze raz.'

#name_1=BusinessContact('mark', 'smith', '48 999999999', 'mark@gmail.com', 'boss', 'somthing ltd', '48 900000000')
