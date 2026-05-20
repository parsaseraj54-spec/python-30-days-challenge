password = input('Enter a Password: ')

score = 0

if len(password) >= 8:
    score += 1
else:
    score -= 1

has_upper = any(c.isupper() for c in password)

if has_upper:
    score += 1
else:
    score -= 1

has_lower = any(i.islower() for i in password)

if has_lower:
    score += 1
else:
    score -= 1

has_number = any(j.isdigit() for j in password)

if has_number:
    score += 1
else:
    score -= 1

has_others = any(not h.isalnum() for h in password)

if has_others:
    score += 1
else:
    score -= 1

print(score)