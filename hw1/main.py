import sys

function = sys.argv[1]

if function == "cone_calc":
    cone_calc(sys.argv[2],sys.argv[3],)


def check(toCheck):
    if toCheck is None:
        return False
    return (isinstance(toCheck, int) or isinstance(toCheck, float))


def cone_calc(height, radius, areaVolume):
    height = float(height)
    radius = float(radius)
    ## Move none check to different loop
    pi = 3.141

    if check(height) or check(radius): ## Either is true then run
        if areaVolume == 'area':
            value = (pi * radius * height) + (pi * pow(radius, 2))
        if areaVolume == 'volume':
            value = pi * pow(radius, 2) * (height / 3)
        #print(type(areaVolume),type(radius),type(value))

    else:
       raise Exception("An argument was invalid.")

    print("The %s of a cone of radius %f is %f" % (areaVolume, radius, value))
