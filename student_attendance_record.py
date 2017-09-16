record = "LALL"
absent = 0
late = 0

for i in xrange(len(record)):
    if record[i] == 'A':
        absent += 1
        late = 0
    elif record[i] == 'L':
        late += 1
    else:
        late = 0

    if absent > 1 or late > 2:
        print "False"

print "True"

print absent
print late
