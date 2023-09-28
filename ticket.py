import sample2
print("Welcome to PVR Cinemas\n")

class day():
    def input2(self):
        self.__c=int(input("Choose the date: "))
        
    def date(self):
        print("This month special!!")
        print('''\n1.28/09/2023
2.29/09.2023
3.30/09/2023''')
    def func1(self):
        if self.__c == 1:
            print("The movies available on 28/09/2023 are")
        elif self.__c ==2:
            print("The movies available on 29/09/2023 are")
        elif self.__c == 3:
            print("The movies available on 30/09/2023 are")
        else:
            print("enter correctly")
            
class movies():
    def input(self):
        self.a=int(input("choose the movie: "))
        
    def movie(self):
        print("\nEnjoy movie time with family and friends") 
        print("""1. Titanic
2. One day
3. Before We Go
4. The NoteBook""")
    def func1(self):
            if self.a == 1:
                print("The movie of your choice is Titanic")
            elif self.a ==2:
                print("The movie of your choice is One day")
            elif self.a == 3:
                print("The movie of your choice is Before We Go")
            elif self.a == 4:
                print("The movie of your choice is The NoteBook ")
            else:
                print("enter correctly")
    def func2(self):
        
            if self.a == 1:
                print("Titanic")
            elif self.a ==2:
                print("One day")
            elif self.a == 3:
                print("Before We Go")
            elif self.a == 4:
                print("The NoteBook ")
            else:
                print("enter correctly")
                
class timing():
    def input1(self):
        self.__b=int(input("Choose the timing: "))
    def time(self):
        print("\nTiming is everything pick wisely")
        print('''1)8:30AM - 10.00AM
2)10:30AM - 12.00PM
3)3:15PM - 4:50PM
4)7:20PM - 9:45PM\n''')
    def func1(self):
        if self.__b == 1:
            print("\nThe timing is 8:30AM - 10.00AM")
        elif self.__b ==2:
            print("\nThe timing is 10:30AM - 12.00PM")
        elif self.__b == 3:
            print("\nThe timing is 3:15PM - 4:50PM")
        elif self.__b == 4:
            print("\nThe timing is 7:20PM - 9:45PM")
        else:
            print("enter correctly")
            
class ticket(movies):
    def tick(self):
        self.ticketcount = int(input("\nTicket count: "))
        print("\nTicket for one at top seat Rs:180")
        print("Ticket for one at middle seat Rs:120")
        print("Ticket for one at bottom seat Rs:60\n")
    def price(self):
        
        self.ticketprice = int(input("Enter your price:"))
        self.tot =self.ticketcount * self.ticketprice
        move = objmov.func2()
        print("\nTotal price of your ticket for ", move,"is Rs:",self.tot)

    def intro(self):
        print("To book your ticket choose the payment method\n")
        print('1.Cash On Delivery\t2.Net Banking\n')
        
    def condition(self):
        payment = int(input("payment method: "))
        acc1 = sample2.acc_no
        acc2 = sample2.pin
        balc = sample2.bal
        if payment == 1:
            print('''\nThank you for booking
you can pay after receiving your ticket
visit us often''')
        elif payment == 2:
            acc=int(input("Enter your account number: "))
            pincode=int(input("Enter you pin: "))
            if (acc == acc1 and pincode == acc2):
                print("\nyour account is verified")
                print("tickets are bocked")
                balance = balc - self.tot
                print("Your remaining balace is",balance)
            else:
                print("\nyour account details are not valid try again")
        else:
            print("\nEnter correctly")
objdate=day()

objdate.date()
objdate.input2()
objdate.func1()

objmov=movies()

objmov.movie()
objmov.input()
objmov.func1()


objtime=timing()

objtime.time()
objtime.input1()
objtime.func1()

objtick=ticket()

objtick.tick()
objtick.price()



objtick.intro()
objtick.condition()




    
