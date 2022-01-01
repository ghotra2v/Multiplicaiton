''' prints out the multoplication with wrong wrong index
    one function will write the multiplication table 
    second function will find which index is wrong'''


import random

# function to print the multiplication table 
def rohanMulitplication(number):
    wrong = random.randint(0, 9)
    table = [i * number for i in range(1, 11)]
    table[wrong] = table[wrong] + random.randint(0, 10)
    return table
# function to print the wrong index of table 

def isCorrect(table, number):
    for i in range(1, 11):
        if table[i - 1] != i * number:
            return i -1
    return None


if __name__ == "__main__":

    # print(rohanMulitplication(7))
    number = int(input("Enter a number: "))
    myTable = rohanMulitplication(number)
    print(myTable)
    wrongIndex = isCorrect(myTable, number)
    print(f"The table is wrong at index {wrongIndex}")
