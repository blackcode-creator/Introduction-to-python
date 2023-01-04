
# Logical operator are like AND OR
# example:
# AND both conditions should be true
# OR at least one condition should be true
# NOT inverses any boolean value
has_high_income = False
has_good_credit = True

if has_high_income and has_good_credit:
    print('Eligible for loan')
elif has_high_income or has_good_credit:
    print('We might consider after second application')


# NOT operator inverses boolean value if it was true inverse it false
# examples:
has_criminal_record = False
has_good_credit = True
if has_good_credit and not has_criminal_record:
    print("Eligible for loan")