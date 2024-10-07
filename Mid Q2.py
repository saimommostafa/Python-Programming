""" Here the input is not in integer
st_scores = list(map(int, input("Enter student scores (comma separated): ").split(",")))
print(st_scores)
"""

n = int(input("Enter the number of students: "))
scores = []

for i in range(n):
    number = int(input(f"Enter the score of student {i+1}: "))
    scores.append(number)

max_score = 0
#setting maximum score to 100
for h_sc in scores:
    if max_score < h_sc:
        max_score = h_sc

percent_increase = 100 / max_score

final_score=[]
for x in scores:
    x = round(x * percent_increase,2)
    if x < 60:
        x = 60.00
    final_score.append(x)

print(f"Original Scores: {scores}")
print(f"Maximum Score: {round(max_score)}")
print(f"Final Scores: {final_score}")