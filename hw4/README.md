# Assignment: hw4 - Movie Similarity
Jack Fernald

Dr. Eric Gibbons

ECE 1400 Engineering Computing

Created on February 07, 2022

Command Line Output
-------------------

    C:\ECE1400\Homework\hw4> python .\similarity.py .\u.data .\similarities.txt 7       
    Input MovieLens files: .\u.data
    Output file for similarity data: .\similarities.txt
    Minimum number of common users: 7
    Read 100000 lines with total of 1682 movies and 943 users
    Computed similarities in 32.4209 seconds

Similarities.txt Sample
-------------------

    1 (238, 1.0000, 7)
    2 (1187, 0.9995, 7)
    3 (175, 0.9398, 7)
    4 (42, 0.9676, 7)
    5 (1001, 0.9974, 7)
    6 (175, 0.9121, 7)
    7 (507, 0.9997, 7)
    8 (618, 0.9334, 7)
    9 (280, 0.8621, 7)
    10 (1038, 0.9597, 7)

Seven was used because in the assignment pdf sample of output used 7

Decomposition of Program
-----------------------------
There are three parts to my code:

* __init__ : This method opens the files specified by the users and sets some other variables for the object.
* __getavg__ : When requested by __computesims__, it will return the average user ratings for a single movie.
* __computesims__ : Main method the class. This is what computes and finds the high similarity coeffiect for each movie
  in the data file.

Import -> Sort and search -> write to file



### Files submitted:
* __test.data__ : Test data
* __similarity.py__ : Main code
* __README.md__
* __.gitignore__ : (Just in the same repo)