## Cashier Simulation
This project is a simulation of a checkout at a store. Customers arrive, wait in line, and perform transactions with cashiers. The simulation is event based, rather than time based. Instead of checking every "tick" of time to see if something needs to be done, events stored in a priority queue by time. Effectively, the simulation jumps to the next event which will take place.

The code to run the simulation is in `Simulation.py`. `Queue.py` is an implementation of a FIFO queue ADT as a singly linked list. `PriorityQ.py` implements a priority queue and is a child of the queue class. I wrote the two queues as part of a lab in a computer science course.

To run the project:

- Ensure you have Python installed.
- From the `CashierSimulation` directory:
- Run the command `python Simulation.py`.