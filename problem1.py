#Problem 1

students = [65, 66, 70, 80, 90, 95, 85, 75, 69, 72, 79, 89, 88, 86, 100, 70, 80, 90]
gold_medal = 0
silver_medal = 0
bronze_medal = 0
participation_award = 0
for s in students:
    if 0 < s < 70:
        participation_award += 1
    elif 70 <= s <= 80:
        bronze_medal += 1
    elif 80 < s <= 90:
        silver_medal += 1
    else:
        gold_medal += 1
print("Gold Medal:", gold_medal)
print("Silver Medal:", silver_medal)
print("Bronze Medal:", bronze_medal)
print("Participation Award:", participation_award, "\n")
