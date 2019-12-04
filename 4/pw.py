def check_pw(pw):
    if (len(pw) == 6 and
        any(pw[idx] == pw[idx + 1] for idx in range(5)) and
        all(pw[idx] <= pw[idx + 1] for idx in range(5))):

        return True

    else:
        return False

# Test suite:

for pw in ['111111','234450','123789']:
    print(pw, check_pw(pw))

matching_pws = []

# Part 1:

for pw in range(272091, 815432 + 1): # adding one to the end to make it 'inclusive'
    if check_pw(str(pw)):
        matching_pws.append(pw)

print(len(matching_pws))

# Part 2:

matching_pws2 = []

for pw in matching_pws:
    if any(str(pw).count(str(digit)) == 2 for digit in range(10)):
        matching_pws2.append(pw)

print(len(matching_pws2))
