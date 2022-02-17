# Jack Fernald
# Assignment: hw4 - Movie Similarity
# Dr. Eric Gibbons
# ECE 1400 Engineering Computing
# Created on February 07, 2022
import math
import sys
import time

def progressbar(current, total):
    progress = int(current/total * 50)
    barstatus = "│" + ("█" * progress) + ("░" * (49 - progress)) + "│ " + str(int((progress/50*100)+0)) + "%"
    print(f'\r{barstatus}', end='')

class MovieData:
    """
    Class MovieData, create object that contains the methods to import and data file, compute similarities and write
    them to a file
    """

    def __init__(self, inputfile, outputfile, threshold, debug):
        """
        __init__ method. opens files and sets some class variables.

        Parameters
        ----------
        inputfile : string
            File name for data file
        outputfile : string
            File to write data to
        threshold : int
            Threshold parameter, will skip movies that do not meet this common number of reviewers
        debug : boolean
            Sorta boolean. Will enable verbose mode for debugging

        """
        self.moviedatafile = open(inputfile, "r")
        self.matchdata = open(outputfile, "w")
        self.moviedata = {}
        self.revieweramount = set()
        if int(threshold) is None:
            self.threshold = 5
        else:
            self.threshold = int(threshold)
        if bool(debug):
            print(" -------- Verbose mode enabled! --------")
            self.debug = True
        else:
            self.debug = False

    def importmoviedata(self):
        """
        Imports and builds a dictionary with the movie ID as the key with reviewer id and respective rating
        """
        start = time.time()
        print("Input MovieLens files:", self.moviedatafile.name)
        print("Output file for similarity data:", self.matchdata.name)
        print("Minimum number of common users:", self.threshold)
        start = time.time()
        linenumber = 0
        end = time.time()
        if self.debug:
            print("Time to import:", end - start)
        for lines in self.moviedatafile:
            linenumber = linenumber + 1
            row = lines.split()
            movieid = int(row[1])
            reviewer = int(row[0])
            review = int(row[2])

            if reviewer not in self.revieweramount:
                self.revieweramount.add(reviewer)

            if movieid not in self.moviedata:
                self.moviedata[movieid] = {reviewer: reviewer}

            if movieid in self.moviedata:
                self.moviedata[movieid][reviewer] = review
            # progressbar(lines, len(self.moviedatafile))
        sorted(self.moviedata)
        print("Read %i lines with total of %i movies and %i users" % (
            linenumber, len(self.moviedata.keys()), len(self.revieweramount)))

    def computesims(self):
        """
        Finds the movie with the highest coefficient rating. Writes it to file specified by user.
        """
        start = time.time()

        # Main loop for Movie A
        for keyA in sorted(self.moviedata.keys()):
            if self.debug:
                progressbar(keyA, len(self.moviedata.keys()))
            if len(self.moviedata[keyA].keys()) < self.threshold:
                if self.debug:
                    print("  Skipped movie:", keyA, "Common Users:", (len(self.moviedata[keyA].keys())), "Requried:",
                          self.threshold, end = '')
                continue
            self.moviedata[keyA].values()
            movieavga = self.getavg(keyA)
            bestmatch = 0

            # Main loop for movie B
            currentbestmatch = 0
            previousmatch = 0
            currentbestmatchmovieid = 0
            ratinga = []
            for ratings in self.moviedata[keyA]:
                ratinga.append(self.moviedata[keyA][ratings])
            if len(ratinga) >= self.threshold:
                for keyB in self.moviedata.keys():
                    # If MovieA and MovieB are the same, skip
                    if keyB == keyA:
                        continue
                    movieavgb = self.getavg(keyB)
                    ratingb = []
                    for ratings in self.moviedata[keyB]:
                        ratingb.append(self.moviedata[keyB][ratings])

                    if (len(ratingb)) >= self.threshold:

                        # Constants for finding similarity
                        bottoma = 0.00
                        bottomb = 0.00
                        top = 0.00
                        bottom = 0.00

                        # Generate top of equations
                        for x in range(self.threshold - 1):
                            top = top + ((int(ratinga[x]) - movieavga) * (int(ratingb[x]) - movieavgb))

                        # Generate bottom of equation
                        for y in range(self.threshold - 1):
                            bottoma = bottoma + math.pow((int(ratinga[y]) - movieavga), 2)
                            bottomb = bottomb + math.pow((int(ratingb[y]) - movieavgb), 2)

                        bottom = bottoma * bottomb
                        bottom = math.sqrt(bottom)

                        # Calc Similarity coefficient
                        if bottom != 0:
                            sim = top / bottom
                        else:
                            sim = -1

                        sim = round(sim, 4)
                        if sim == -1:
                            continue
                        elif sim > previousmatch:
                            currentbestmatch = sim
                            currentbestmatchmovieid = keyB
                            previousmatch = sim

                if currentbestmatchmovieid != 0:
                    self.matchdata.write(
                        "%i (%i, %6.4f, %i)\n" % (int(keyA), currentbestmatchmovieid, currentbestmatch, self.threshold))
            end = time.time()

        print("\rComputed similarities in %.4f seconds %s" % (end - start, " " * 70))

    def getavg(self, moviekey):
        movieavg = 0
        moviecount = 0
        for ratings in self.moviedata[moviekey].values():
            movieavg = movieavg + ratings
            moviecount = moviecount + 1
        movieavg = movieavg / moviecount
        return movieavg

    # Manual settings
    def printmoviedata(self, movie):
        print(self.moviedata[movie])

    # Run all methods
    def run(self):
        self.importmoviedata()
        self.computesims()


def main():
    movielist = MovieData('u.data', 'sim.txt', 5, True)
    # try:
    #     if len(sys.argv) < 4:
    #         movielist = MovieData(sys.argv[1], sys.argv[2], 5, False)
    #     elif len(sys.argv) < 5:
    #         movielist = MovieData(sys.argv[1], sys.argv[2], sys.argv[3], False)
    #     else:  # Verbose mode Enabled
    #         movielist = MovieData(sys.argv[1], sys.argv[2], sys.argv[3], True)
    movielist.run()
    # except IndexError as err:
    #     print(err)
    #     print("Usage:\n      $python similarity.py <data_file> <output_file> [user_thresh (default = 5)]")


if __name__ == "__main__":
    main()
