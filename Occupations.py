import csv, random
from collections import defaultdict

total = 99.8
occs = dict()


def initVars():
    f = open("Occupations.csv")
    reader = csv.DictReader(f)
    for row in reader:
        occs[row['Job Class']] = float(row['Percentage'])        


def randOcc():
    pick = random.uniform(0, total)
    for occ in occs.keys():
        pick -= occs[occ]
        if pick <= 0.1:
            return occ

def testRand():
    occsTest = defaultdict(lambda: 0)
    total = 0
    while (total < (10 ** 6)):
        occ = randOcc()
        occsTest[occ] += 1
        total += 1

    error = 0
        
    for occ in occs.keys():
        error += occsTest[occ] / (10 ** 4) - occs[occ]
    error /= len(occs.keys())
    print("Avg error of %.2f%% from ideal weights" % error)
    
        

def main():
    initVars()
    print randOcc()
    testRand()

if __name__ == "__main__":
    main()

