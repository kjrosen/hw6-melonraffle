"""Randomly pick customer and print customer info"""
from customers import Customer
from customers import get_customers_from_file
from random import choice

def raffle(customers):
    '''pulls a randomly selected winner from the customer list'''

    chosen_customer = choice(customers)
    message = f"""{chosen_customer.name} has won the raffle!
    Reach them at {chosen_customer.email}"""
    
    return message

contestants = get_customers_from_file("customers.txt")
print(raffle(contestants))
