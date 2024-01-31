#Part 2

call_score = 10
meeting_score = 30
sale_score = 100

jordan_belfort = {
    'calls': 178,
    'meetings':17,
    'sales':6
}

#A

# Create a function called get_score taking a dictionary of a person as input (like the
# jordan_belfort dictionary above), uses the logic above to calculate the score and 
# returns the total score for that person.
#  Call the get_score function using the jordan_belfort dictionary and print
# the result. Verify that the score is correct.

def get_score_A(dictionary):
    calls = dictionary.get("calls") * call_score
    meetings = dictionary.get("meetings") * meeting_score
    sales = dictionary.get("sales") * sale_score

    return calls+meetings+sales 

result = get_score_A(jordan_belfort)
print(result)

# B (Level 1)
# There is also a 100-point bonus for each, if you make more than 150 calls, 20 meetings or 5 sales.
# Add the logic to you get_score function and again verify that it is correct using jordan_belfort..
# HINT: Compared to A the score should now be 200 higher.
call_amount = 150
meeting_amount = 20
sale_amount = 5
bonus = 100

def get_score_B(dictionary):
    total = 0
    calls = dictionary.get("calls") 
    meetings = dictionary.get("meetings")
    sales = dictionary.get("sales")
    if (calls > call_amount):
        total += bonus
    if (meetings > meeting_amount):
        total += bonus
    if (sales > sale_amount):
        total += bonus
        
    total += (calls*call_score)+(meetings*meeting_score)+(sales*sale_score)

    return total 

result = get_score_B(jordan_belfort)
print(result)