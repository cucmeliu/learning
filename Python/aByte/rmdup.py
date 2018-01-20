
#!/usr/bin/python

inf = file('in.txt') #file('C:\Users\leo\Documents\WXWork\\1688853455296712\\Cache\\File\\2018-01\\201711.txt')
inf2 = file('in.txt') #file('C:\Users\leo\Documents\WXWork\\1688853455296712\\Cache\\File\\2018-01\\201711.txt')
outf = file('out.txt', 'r+')


while True:
    finaline = line = inf.readline()

    phonepair_cur = line.split()
    print phonepair_cur

    if len(line) == 0:
        break
    while True:
        line2 = inf.readline()
        if len(line2) == 0:
            break

        phonepair_it = line2.split()
        if phonepair_cur[0] == phonepair_it[0]:
            finaline = phonepair_it[0] + ',' + phonepair_it[1]

    outf.write(finaline)

f.close()
