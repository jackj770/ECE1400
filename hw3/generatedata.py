# Jack Fernald
# Assignment: hw3 Generate Data , Gene Sequencing - generatedata.py
# Dr. Eric Gibbons
# ECE 1400 Engineering Computing
# Created on February 01, 2022

import sys
import numpy


class Generate:
    """
    Generate class outlines the methods for easy 'sequence' generation
    to a file specified by the user
    """

    def __init__(self, ref_file, reads_file):
        """
        Parameters
        --------
            ref_file : file for the reference string to go once it is generated
            reads_file : file for the reads to go once generated from sequence
        """
        self.f = ref_file
        self.r = reads_file
        self.ref = ""

    def __exit__(self):
        """
        Closes files once user is done with object
        """
        self.f.close()
        self.r.close()

    def generateref(self, n, write):
        """
        Generates the reference sequence used for the generated reads and searching for the reads
        Parameters
        --------
            n : Desired length of the reference sequence
            write : An option internally used to write to the ref file or not.
            user does not use this parameter
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
        Generates reads from the sequence and writes to a file specified by the user
            Parameters
            --------
                n : Desired amount of reads
                length : Desired length of individual reads
        """

        f = open(self.f, "r")
        r = open(self.r, "w")
        n = int(n)
        length = int(length)
        seq = f.read()
        print("number reads: %i" % (n))
        print("read length: %i" % (length))
        reflength = len(seq)
        singlereads = int(n * 0.75)
        doublereads = int(n * 0.1)
        noreads = int(n * 0.15)

        for x in range(0, singlereads):
            pos = numpy.random.randint(0, (reflength / 2))
            read = seq[pos:pos + length]
            r.write(read + "\n")
        for x in range(0, int(doublereads)):
            pos = numpy.random.randint(0, int(reflength / 4))
            start = pos + int(reflength / 2)
            read = seq[start:start + length]
            r.write(read + "\n")
            # print(x, read, length)
        for x in range(0, noreads):
            self.ref = ""
            self.generateref(length, False)
            r.write(self.ref + "\n")


def main():
    try:
        newdata = Generate(sys.argv[4], sys.argv[5])
        newdata.generateref(sys.argv[1], True)
        newdata.generatereads(sys.argv[2], sys.argv[3])
    except IndexError:
        print("Usage:\n $ python generatedata.py <ref_length> <nreads> <read_len> <ref_file> <reads_file>\n")


if __name__ == "__main__":
    main()
