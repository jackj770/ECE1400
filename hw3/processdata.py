# Jack Fernald
# Assignment: hw3 - Gene Sequencing processdata.py
# Dr. Eric Gibbons
# ECE 1400 Engineering Computing
# Created on February 03, 2022
import sys
import time
import numpy


class Detect:
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
        index = ""
        initindex = 0
        foundindex = 0
        while foundindex != -1:
            foundindex = self.seq.find(read, initindex)
            if foundindex != -1:
                if foundindex > len(self.seq) / 2:
                    self.doublematch = self.doublematch + 1
                    # print(self.doublematch, foundindex)
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
        print(self.singlematch, self.doublematch, self.nomatch)
        singlematch = self.singlematch / lines
        doublematch = self.doublematch / lines
        nomatch = self.nomatch / lines
        print("aligns 0: %f" % (nomatch))
        print("aligns 1: %f" % (singlematch))
        print("aligns 2: %f" % (doublematch))
        end = time.time()
        print("elapsed time: %.6f" % (end - start))
        self.a.close()
        self.f.close()
        self.ref.close()

        print(numpy.unique(self.temp))


def main():
    # try:
        newsequence = Detect(sys.argv[1], sys.argv[2], sys.argv[3])
        newsequence.detectmatch()
    # except:
    #     print("Usage:\n $ python processdata.py <ref_file> <reads_file> <align_file>\n")


if __name__ == "__main__":
    main()
