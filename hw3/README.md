# Homework 3 - Gene Sequencing 
**Jack Fernald**

**ECE1400**

**Dr. Eric Gibbons**
**Time Spent: ~ 5 hours**

Part 2 Writeup
--------------

    (base) user@computer:~/location/ECE1400$ python3 generatedata.py 1000 600 50 ref_1.txt reads_1.txt 
      reference length: 1000
      number reads: 600
      read length: 50

    (base) user@computer:~/location/ECE1400$ python3 generatedata.py 10000 6000 50 ref_1.txt reads_1.txt 
      reference length: 10000
      number reads: 6000
      read length: 50

    (base) user@computer:~/location/ECE1400$ python3 generatedata.py 10000 6000 50 ref_1.txt reads_1.txt 
      reference length: 10000
      number reads: 6000
      read length: 50

**Questions**

* Question 1:
  * I tried to make it as modular as I could. I added a class for generating data that you can call on an
  object to build the "gene sequence" and write it to a file. The __del__ class cleans up the files when
  you're with the object. The code will work with any .txt files that match the format specified in the assignment
* Question 2:
  * You should not expect that exact distribution, at least in the double reads I found that it was slightly
  difficult to get it be right on .10 of reads. If this was a real station, if you read at anything greater than 950 for example
  the reads generated would get cut short but since we're just grabbing in the 50% to 75% range of the ref length
  then you'll be fine.
* Question 3:
  * To be honest I spent like 5 hour working on this, I rewrote it to have classes which wasn't hard, but I just
  kept running into little things that kept tripping me up. I haven't coded since last year, so I'm definitely rusty.

Part 3 Writeup
--------------

    (base) user@computer:~/location/ECE1400 python3 processdata.py ref_1.txt reads_1.txt alignments_1.txt 
      reference length: 1000
      number reads: 600
      aligns 0: 0.150000
      aligns 1: 0.750000
      aligns 2: 0.130000
      elapsed time: 0.005880

    (base) user@computer:~/location/ECE1400 python3 processdata.py ref_1.txt reads_1.txt alignments_1.txt 
      reference length: 10000
      number reads: 6000
      aligns 0: 0.150000
      aligns 1: 0.750167
      aligns 2: 0.158500
      elapsed time: 0.178874

    (base) user@computer:~/location/ECE1400 python3 processdata.py ref_1.txt reads_1.txt alignments_1.txt 
      reference length: 100000
      number reads: 60000
      aligns 0: 0.150000
      aligns 1: 0.750017
      aligns 2: 0.159883
      elapsed time: 16.055946


**Questions**

* Question 1:
  * Similar to question 1 in the first part, the single reads and the double reads I had a decent time making 
  but the double reads I had a somewhat difficult time getting it to make the proper amount. The 'generate' code
  would make the .10 of the reads there but then when I would process it, I would get around .18 reads there.
  I believe it was something to do with how I was deciding on where to get the reads from in the 0.50 - 0.75 portion 
  of the reference string. 
* Question 2:
  * As powers of 10 were added the time grew somewhat exponentially. The 1000 and 10000 went fast for both generation
  and processing but when the 100k were generated and ran it took about 16 seconds to process. For a human sequence I would 
  not expect anything less than a few days even with a beefy computer.
* Question 3:
  * Refer to Q3 of part 2

