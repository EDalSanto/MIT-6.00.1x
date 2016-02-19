def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
    '''
    def f(x):#defines f(x) for curve
        import math
        return 10*math.e**(math.log(0.5)/5.27 * x)
    def frange(x, y, jump):#function that enables floats to be used in range function
        while x < y:
            yield x
            x += jump
    total_radiation = 0#amount of radiation one will be exposed to
    for x in frange(start,stop, step):#iterate for all x values in the start-stop range, "step distance apart"
        total_radiation += (f(x)*step)#increase total_radiation by area of each rectangle)
    return total_radiation#returns final value of total radiation, area of x rectangles
        