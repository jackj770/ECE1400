# Jack Fernald
# Assignment: hw3 Generate Data , Gene Sequencing
# Dr. Eric Gibbons
# ECE 1400 Engineering Computing
# Created on February 01, 2022
import sys

import numpy


class Generate:
    def __init__(self, ref_file, reads_file):
        self.f = ref_file
        self.r = reads_file
        self.ref = ""

    def __exit__(self):
        self.f.close()
        self.r.close()

    def generateref(self, n, write):

        """
        Parameters
        --------
            n : Desired length of the reference sequence
    
        Return
        -------
            return : string
                The generated length of the reference sequence
        """

        n = int(n)
        randlengen = int(n)
        if write:
            print("reference length: %i" % (n))
            f = open(self.f, "w")
            randlengen = int(int(n) * 0.75)
            half = int(int(n) * 0.5)

        for x in range(0, randlengen):
            i = numpy.random.randint(0, 4, None, int)
            if i == 0:
                self.ref += 'A'
            if i == 1:
                self.ref += 'T'
            if i == 2:
                self.ref += 'G'
            if i == 3:
                self.ref += 'C'
        if (write):
            lastfourth = self.ref[half:randlengen]
            self.ref += lastfourth
            f.write(self.ref)
            f.close()

    def generatereads(self, n, length):
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

        f = open(self.f, "r")
        r = open(self.r, "w")
        n = int(n)
        length = int(length)
        seq = f.read()
        print("number reads: %i" % (n))
        print("read length: %i" % (length))
        reflength = len(seq)
        print(n)
        singlereads = int(n * 0.75)
        doublereads = int(n * 0.1)
        noreads = int(n * 0.15)
        print(noreads, singlereads, doublereads)

        # print(noreads, singlereads, doublereads)

        # First half of ref
        print("ref", reflength)
        for x in range(0, singlereads):
            pos = numpy.random.randint(0, (reflength / 2))
            read = seq[pos:pos + length]
            r.write(read + "\n")
            # print(x)
        # last half
        for x in range(0, int(doublereads/2)):
            pos = numpy.random.randint(0, (reflength / 2))
            start = int(pos + (reflength / 2))
            read = seq[start:start + length]
            r.write(read + "\n")
            # print(x, read)
        for x in range(0, noreads):
            self.ref = ""
            self.generateref(length, False)
            r.write(self.ref + "\n")
            # print(x)


def main():
    try:
        newdata = Generate(sys.argv[4], sys.argv[5])
        newdata.generateref(sys.argv[1], True)
        newdata.generatereads(sys.argv[2], sys.argv[3])
    except:
        print("Usage:\n $ python generatedata.py <ref_length> <nreads> <read_len> <ref_file> <reads_file>\n")


if __name__ == "__main__":
    main()
