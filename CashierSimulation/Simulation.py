from PriorityQ import *
from random import *


class Cashier:
    """Defines the cashier object, which remembers if it is busy"""
    def __init__(self):
        self.busy = False

    def isBusy(self):
        return self.busy

    def makeBusy(self):
        self.busy = True

    def makeFree(self):
        self.busy = False


class Customer:
    """Defines customer object, which only needs to remember"""
    def __init__(self, arrival):
        self.arrivalTime = arrival

    def getArrival(self):
        return self.arrivalTime


class Event:
    """Defines event object, keeps track of type, participants, and ending time"""
    def __init__(self, type, time, customer=None, cashier=None):
        self.type = type
        self.time = time
        self.customer = customer
        self.cashier = cashier

    def getType(self):
        return self.type

    def getTime(self):
        return self.time

    def getCustomer(self):
        return self.customer

    def getCashier(self):
        return self.cashier

class Simulation:
    """Runs the simulation"""
    def __init__(self, cashierNum, lm, mu, maxTime):

        # Define user input values
        self.lm = int(lm)
        self.mu = int(mu)
        self.maxTime = int(maxTime)

        # Create the queue of events
        self.eventq = PriorityQueue()

        # Add one customer arrival event
        t = self.customerArrivalTime()
        if t <= self.maxTime:
            self.eventq.enqueue(t, Event("Arrival", t))

        # Create a queue for customers to wait in
        self.customerq = Queue()

        # Set up an array of cashiers
        self.cashiers = []
        for i in range(int(cashierNum)):
            self.cashiers.append(Cashier())

        # Recent time tells us the time of the last event to take place
        self.recentTime = 0
        # Time waited is the total time customers had to wait
        self.timeWaited = 0
        # Data points is the number of customers that contributed to wait time
        self.dataPoints = 0
        # Served is the number of customers that completed transactions
        self.served = 0
        # Leftover is the number of customers that have not completed transactions
        self.leftover = 0

    def run(self):
        # Run as long as there are still events queued
        while not self.eventq.is_empty():
            # "Do" the next event
            curevent = self.eventq.dequeue()
            self.recentTime = curevent.getTime()

            # Uncomment the line below for debug mode
            print("Time: "+str(self.recentTime)+" Event Type: "+curevent.getType())

            # If a customer arrives
            if curevent.getType() == "Arrival":
                # Schedule the next random customer arrival
                t = self.customerArrivalTime(curevent.getTime())
                # But only if it will happen before the simulation ends
                if t <= self.maxTime:
                    self.eventq.enqueue(t, Event("Arrival", t))
                    # Assume the customer will not be served for now
                    self.leftover += 1

                # Create a new customer who will stand in line
                curcustomer = Customer(self.recentTime)
                self.customerq.enqueue(curcustomer)

            # If a transaction finishes
            elif curevent.getType() == "Transaction":
                # Set the cashier to free
                self.cashiers[curevent.getCashier()].makeFree()

                # Update customers served
                self.served += 1
                # One less customer in line
                self.leftover -= 1

            # If there is a customer in line, look for a open cashier
            if not self.customerq.is_empty():
                freecashier = self.findFreeCashier()
                # If there is a free cashier
                if freecashier >= 0:
                    # Get a customer
                    servecustomer = self.customerq.dequeue()
                    # Create a transaction finished event
                    t = self.customerWaitTime(self.recentTime)
                    if t <= self.maxTime:
                        self.eventq.enqueue(t, Event("Transaction", t, servecustomer, freecashier))
                        # Set their cashier to busy
                        self.cashiers[freecashier].makeBusy()
                        #Update average wait time
                        self.timeWaited += self.recentTime - servecustomer.getArrival()
                        self.dataPoints += 1
        # After the loop, compute and print data
        avg = self.average()
        print("Average customer wait time: " + str(avg) + ".")
        print("Customers served: "+str(self.served)+".")
        print("Customers left in line: "+str(self.leftover)+".")

    def findFreeCashier(self):
        # Return the index/number of the first free cashier
        for i in range(len(self.cashiers)):
            if not self.cashiers[i].isBusy():
                return i
        return -1

    def customerArrivalTime(self, prev=0):
        # Return a random arrival time for the next customer
        return randint(1, self.mu)+prev

    def customerWaitTime(self, prev=0):
        # Return a random transaction time for a customer
        return randint(1, self.lm)+prev

    def average(self):
        # Calculate the average
        return self.timeWaited/self.dataPoints

def main():
    n = input("How many cashiers? ")
    m = input("Max interval between customers? ")
    l = input("Max transaction time? ")
    t = input("Simulation time? ")
    sim = Simulation(n, l, m ,t)
    sim.run()
main()