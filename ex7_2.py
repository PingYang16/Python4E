fname = input("Enter file name: ")
fh = open(fname)
total = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count += 1
    pos = line.find(':')
    num = float(line[pos+1:].strip())
    total += num

average = total / count
print("Average spam confidence:", average)