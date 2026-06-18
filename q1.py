attendance = ['P', 'A', 'P', 'P', 'A']

count = 0
for i in attendance:
    if i == 'P':
        count += 1

print("Present Students:", count)