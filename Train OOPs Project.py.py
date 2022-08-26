class Train:
    def __init__(self,name,seats,fare,start,end,dtime,atime):
        self.name=name
        self.seat= len(seats)
        self.fare= fare
        self.start= start
        self.end= end
        self.dtime= dtime
        self.atime=atime
        self.aseats=seats
        self.bookedseats=set()

    def getInfo(self):
        print(f"Train name     : {self.name}")
        print(f"Seat available : {self.seat}")
        print(f"Fare           : {self.fare}")
        print(f"From           : {self.start}")
        print(f"To             : {self.end}")
        print(f"Departure Time : {self.dtime}")
        print(f"Arrival Time   : {self.atime}")
    
    def book(self):
        if self.seat>0:
            seatNo=int(input(f"Please select your seat from {self.aseats}"))
            self.bookedseats.add(seatNo)
            self.aseats.remove(seatNo)
            print("Please make the payment")
            pay=input("You can pay using following options:\nUPI\nNet Banking\nCredit/Debit card\nWallet\n")
            if pay=="upi":
                a=input("Enter your upi id")
                if a:
                    print("Your Payment has been done")
                    print("Your ticket has been booked. Your seat no is",seatNo)
                    self.seat=self.seat-1
            elif pay == "card":
                a=input("Enter your card details")
                if a:
                    print("Your Payment has been done")
                    print("Your ticket has been booked. Your seat no is",seatNo)
                    self.seat=self.seat-1
            elif pay=="net banking":
                a=input("Select your bank")
                if a:
                    print("Your Payment has been done")
                    print("Your ticket has been booked. Your seat no is",seatNo)
                    self.seat=self.seat-1
            elif pay=="wallet":
                a=input("Select your wallet")
                if a:
                    print("Your Payment has been done")
                    print("Your ticket has been booked. Your seat no is",seatNo)
                    self.seat=self.seat-1
        else:
            print("Sorry the train is full, Please wait for tatkal ticket")
            
    def cancel(self):
        sno=int(input("Please enter your seat no: "))
        if sno in self.bookedseats:
            print("Your ticket has been cancelled")
            self.bookedseats.remove(sno)
            self.aseats.add(sno)
            self.seat=self.seat+1
        else:
            print("Record not found")
            


rajdhaniExpress=Train("Rajdhani Express",{1,2,3,4,5,6,7,8,9,10},"Rs 2500","Delhi","Mumbai","1 a.m.","11 p.m")
# narmadaExpress=Train("Narmada Express", 400, "Rs 2000", "Lucknow", "Bengaluru", "2 p.m", "1 p.m.")

rajdhaniExpress.getInfo()
rajdhaniExpress.book()
rajdhaniExpress.book()
rajdhaniExpress.cancel()
rajdhaniExpress.getInfo()
rajdhaniExpress.book()
rajdhaniExpress.getInfo()