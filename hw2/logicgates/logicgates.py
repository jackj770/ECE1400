# Jack Fernald
# Assignment: logicgates
# Dr. Eric Gibbons
# ECE 1400 Engineering Computing
# Created on January 25, 2022


binlist = [0, 0, 0, 0, 0]


def andgate(x, y):                                  # And Gate
    """
    Function returns the intersection of x and y:
    if x and y are either 0 or 1 then return true, else false

    Parameters
    ----------
    x : bool
        element one to compare against
    y : bool
        element two to compare against

    """
    return x and y


def orgate(x, y):                                   # Or Gate
    return x or y


def notgate(x):                                     # Not Gate
    return not x


def counttable(amount):
    mod = 1
    for ii in range(1, 6):                          # Scans over rows
        if amount % mod == 0:
            if binlist[5 - ii] == 0:
                binlist[5 - ii] = 1
            else:
                binlist[5 - ii] = 0
        mod = mod * 2


def truthtablegen(n):
    print("A | B | C | D | E || Q\n----------------------")
    for n in range(1, n + 2):                       # Row counter
        # Below is gate configuration as per homework assignment
        q = andgate(orgate(andgate(binlist[0], binlist[1]), notgate(binlist[2])), andgate(binlist[3], binlist[4]))
        # Below is print statement for truth table
        print("%i | %i | %i | %i | %i || %i    %i" % (binlist[0], binlist[1], binlist[2], binlist[3], binlist[4], q, n))
        counttable(n)


truthtablegen(31)                                   # Function call to the truth table generator function

