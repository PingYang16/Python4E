name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
count = dict()
for line in handle:
    if not line.startswith("From "):
        continue
    word = line.split()[1]
    count[word] = count.get(word, 0) + 1
most = None
committer = None
for word, time in count.items():
    if most is None or most < time:
        most = time
        committer = word
print(committer, most)