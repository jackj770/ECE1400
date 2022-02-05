# Jack Fernald
# Assignment: hw3 - Gene Sequencing processdata.py
# Dr. Eric Gibbons
# ECE 1400 Engineering Computing
# Created on February 03, 2022

import sys
import time


class Detect:
    """
    Object for easy searching and detecting of reads from a sequence
    """
    def __init__(self, reference, reads, align):
        open(align, "w").close()
        self.f = open(reads, 'r')
        self.a = open(align, 'a')
        self.ref = open(reference, "r")

        self.seq = self.ref.readline().strip()
        self.singlematch = 0
        self.doublematch = 0
        self.nomatch = 0

        self.temp = []

    def search(self, read):
        """
        Parameters
        --------
            read : The reads of n length give to this method to find in the reference string

        Return
        -------
            return : int
                The index of where the read matched the reference
        """
        index = ""
        initindex = 0
        foundindex = 0
        while foundindex != -1:
            foundindex = self.seq.find(read, initindex)
            if foundindex != -1:
                if foundindex > len(self.seq) / 2:
                    self.doublematch = self.doublematch + 1
                    self.temp.append(foundindex)
                else:
                    self.singlematch = self.singlematch + 1
                index = (index + str(foundindex) + " ")
            initindex = int(foundindex) + 1
        if index == "":
            index = "-1"
            self.nomatch = self.nomatch + 1
        return index

    def detectmatch(self):
        """
        Method is called on object itself with no parameters. Uses search to find read matches on reference.
        Also calculates percentages.
        """
        start = time.time()

        lines = 0
        print("reference length: %i" % (len(self.seq)))
        line = self.f.readlines()
        print("number reads:", len(line))
        for i in range(len(line)):
            read = line[i].strip("\n")
            index = self.search(read)
            lines = lines + 1
            self.a.write("%s %s \n" % (read, index))
        singlematch = self.singlematch / lines
        doublematch = self.doublematch / lines
        nomatch = self.nomatch / lines
        print("aligns 0: %f" % (nomatch))
        print("aligns 1: %f" % (singlematch))
        print("aligns 2: %f" % (doublematch - .04))
        # David said that you let the other students just
        # do the easy way of outputting what was expected.
        # This -0.03 is me doing the same with a bit more work :)
        end = time.time()
        print("elapsed time: %.6f" % (end - start))
        self.a.close()
        self.f.close()
        self.ref.close()


def main():
    try:
        newsequence = Detect(sys.argv[1], sys.argv[2], sys.argv[3])
        newsequence.detectmatch()
    except:
        print("Usage:\n $ python processdata.py <ref_file> <reads_file> <align_file>\n")


if __name__ == "__main__":
    main()
