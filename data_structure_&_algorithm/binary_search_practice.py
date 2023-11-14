# Alice has some cards with numbers written on them.
# She arranges the cards in decreasing order and lays them out face down in a sequence on a table.
# She challenges Bob to pick out the card containing a given number by turning over as few cards as possible.
# Write a function to help Bob locate the card.


# To solve this problem we will treat the sequence of cards as a list of numbers.
# then the obvious solution here can be done using linear search (brute force) which enables Bob to turn over each card individually until it finds the given number in the sequence of cards (list of numbers in this case).

# - step 1, create a variable named "position" with the value 0 which serves as the index of the current card in the list of cards
# - step 2, check whether the currrent card in "position" is equal to the "query" card
# - step 3, if it equals, output the current position
# - step 4, if it does not equal, add 1 to position and repeat step 2 to 5 until we reach the last position
# - step 5, if the card was not found, return -1

def locate_card(cards, query):
    # Create a variable named "position" with the value 0
    position = 0
    
    # set a loop that helps go through the list of cards(numbers in this case)
    while position < len(cards):
        # Check if the number in "position" matches the query
        if cards[position] == query:
            # Returns position and ends loop
            return position
        
        # increase position if position does not match query
        position += 1
        
    # number not found, return -1
    return -1
    

locate_card([13, 11, 10, 7, 4, 3, 1, 0], 11)
