ino=int(input())
def next_distinct_year(ino):
    while True:
        ino += 1
        if len(set(str(ino))) == len(str(ino)):
            return ino

print(next_distinct_year(ino))