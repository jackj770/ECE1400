# Jack Fernald
# Assignment: logicgates
# Dr. Eric Gibbons
# ECE 1400 Engineering Computing
# Created on January 25, 2022


def andgate(x, y):  # And Gate
    """
    Function returns the intersection of x and y:
    if x and y are either 0 or 1 then return true, else false

    Parameters
    ----------
    x : bool
        element one to compare against
    y : bool
        element two to compare against

    Return
    ------
    return: boolean
        The intersection of x and y 

    """
    return x and y


def orgate(x, y):  # Or Gate
    """
    Function returns the union of x and y:
    if x or y or both are 1 then return true, else false

    Parameters
    ----------
    x : bool
        element one to compare against
    y : bool
        element two to compare against
    
    Return
    ------
    return: boolean
        The union of x and y 

    """
    return x or y


def notgate(x):
    """
    Function returns the inverse of x:

    Parameters
    ----------
    x : bool
        Value to invert
    
    Return
    ------
    return: boolean
        Inverse of x, either true or false 

    """
    return not x


def counttable(amount, binlist):
    """
    Function returns a list of the next line of a truth table that was passed.

    Parameters
    ----------
    amount : int
        nth row of a truth table (with x amount of bits)
    binlist : list
        The current iteration of the truth table, used to generate the next line.
    
    Return
    ------
    return: list
        The next iteration of the truth table based on the previous row

    """
    mod = 1
    for ii in range(1, 6):  # Scans over rows
        if amount % mod == 0:
            if binlist[5 - ii] == 0:
                binlist[5 - ii] = 1
            else:
                binlist[5 - ii] = 0
        mod = mod * 2
    return binlist


def truthtablegen(n):
    """
        Function builds a table based on the in the gate configuration with the help of the counttable function. Does
        this by passing the array from the counttable function into the gate configuration (q).

        Parameters
        ----------
        n : int
            Number of times you want the generator to run

        Return
        ------
        return: null
            returns nothing but prints during its cycle

        """
    binlist = [0, 0, 0, 0, 0]
    print("A | B | C | D | E || Q\n----------------------")
    for n in range(1, n + 2):  # Row counter
        # Below is gate configuration as per homework assignment
        q = andgate(orgate(andgate(binlist[0], binlist[1]), notgate(binlist[2])), andgate(binlist[3], binlist[4]))
        # Below is print statement for truth table
        print("%i | %i | %i | %i | %i || %i    %i" % (binlist[0], binlist[1], binlist[2], binlist[3], binlist[4], q, n))
        counttable(n, binlist)


if __name__ == '__main__':
    truthtablegen(31)  # Function call to the truth table generator function


