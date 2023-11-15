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

# Here's how binary search can be applied to our problem:

# Find the middle element of the list.
# If it matches queried number, return the middle position as the answer.
# If it is less than the query number, then search the first half of the list
# If it is greater than the queried number, then search the second half of the list
# If no more elements remain, return -1.

def test_location(cards, query, mid):
    mid_number = cards[mid]
    if mid_number == query:
        print("mid: ", mid, " mid_number: ", mid_number)
        if mid - 1 >= 0 and cards[mid - 1] == query:
            return "left"
        else:
            return "found"
    elif mid_number < query:
        return "left"
    else:
        return "right"


def locate_card2(cards, query):
    
    low = 0
    high = len(cards) - 1
    
    #Finds the middle number of the list
    while low <= high:
        print("low: ", low, ", high: ", high)
        # double // is used in case where (low + high) is not divisible by 2
        mid = (low + high) // 2 # this can also be done as: math.floor((start + end) / 2).. math needs to be imported for this to work.
        
        result = test_location(cards, query, mid)
        
        if result == "found":
            return mid
        elif result == "left":
            high = mid - 1
        elif result == "right":
            low = mid + 1
    
    # if query is not found            
    return -1
        
        
locate_card2([13, 11, 10, 7, 4, 3, 1, 0], 11)