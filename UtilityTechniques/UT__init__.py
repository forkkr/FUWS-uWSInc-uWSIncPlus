from UtilityTechniques.ProbabilityWeightAssign import ProbabilityAssign, checkCSV


if __name__ == '__main__':
    where = '../LEVIATHAN/LEVIATHAN_sp.txt'
    read = '../LEVIATHAN/LEVIATHAN_s.txt'
    probs = '../Files/probs.csv'
    
    # for i in range(0, 11):
    #     fwhere = where+str(i)+'.txt'
    #     fread = read+str(i)+'.txt'

    ProbabilityAssign(read, probs, where).Assigning()
    # checkCSV.file = open('../Files/probs.csv', 'r')
    # checkCSV.run()
