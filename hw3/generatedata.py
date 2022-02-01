# Jack Fernald
# Assignment: hw3 Generate Data , Gene Sequencing
# Dr. Eric Gibbons
# ECE 1400 Engineering Computing
# Created on February 01, 2022

import numpy


def generateref(ref, n, write):
    """
    Parameters
    --------
        n : Desired length of the reference sequence

    Return
    -------
        return : string
            The generated length of the reference sequence
    """
    randlengen = int(n * 0.75)
    half = int(n * 0.5)

    for x in range(0, randlengen):
        i = numpy.random.randint(0, 4, None, int)
        if i == 0:
            ref += 'A'
        if i == 1:
            ref += 'T'
        if i == 2:
            ref += 'G'
        if i == 3:
            ref += 'C'

    if(write):
        lastfourth = ref[half:randlengen]
        ref += lastfourth

        f = open("reference0.txt", "w")
        f.write(ref)
        f.close()
    return ref



def generatereads(n, length):
    """
        Parameters
        --------
            n : Desired amount of reads
            len : Desired length of individual reads
            ref : Freshly generated reference list

        Return
        -------
            return : string
                The generated length of the reference sequence
    """
    r = open("reads0.txt", 'a')
    ref = open("reference0.txt", "r")

    seq = ref.readline()
    reflength = len(seq)
    print(seq)

    # First half of 50% reads
    halfref = int(reflength/2)
    quarterref = int(reflength/4)

    majorityreads = int(n * 0.75)
    doublereads = int(n * 0.1)
    print(doublereads)
    print(quarterref)
    noreads = int(n*0.15)




    # First half of ref
    # f.write("75% of reads\n")
    for x in range(0, majorityreads):
        pos = numpy.random.randint(0, halfref-1)
        read = seq[pos:pos + length]
        r.write(read + "\n")
    # last half
    # f.write("10% of reads\n")
    for x in range(0, doublereads):
        pos = numpy.random.randint(0, quarterref-1)
        start = pos+halfref
        read = seq[start:start+length]
        r.write(read + "\n")
    # # f.write("15% of reads\n")
    for x in range(0, noreads):
        read = ""
        read = generateref(read, length+2, False)
        r.write(read + "\n")
    r.close()
    ref.close()


def detectmatch(n):
    f = open("reads0.txt",'r')
    a = open("alignments0.txt",'a')
    ref = open("reference0.txt", "r")
    seq = ref.readline()

    for x in range(n):
        read = f.readline().strip()
        index = str(seq.find(read, 0, len(seq)))
        a.write(index + "\n")
    a.close()
    f.close()
    ref.close()



def main():
    with open("reference0.txt", 'w') as f:
        f.close()
    with open("reads0.txt", 'w') as f:
        f.close()
    with open("alignments0.txt", 'w') as f:
        f.close()


    ref = ""
    generateref(ref, 100, True)
    generatereads(60, 5)
    detectmatch(60)


if __name__ == "__main__":
    main()
