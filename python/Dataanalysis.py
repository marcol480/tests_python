import numpy as np
import pandas as pd
import sys 

def computeMSD2(trajectory, t_step):
    """ Base commands for the regular unit test suite
        Example with artificial data
    ---------
    >>> x = np.arange(0,100,0.1)
    >>> y = np.cumsum(np.zeros(1000) )
    >>> df = pd.DataFrame(y, index=x)
    >>> np.mean(computeMSD2(df, 1)[1])
    0.0
    """ 
    assert t_step > 0, 'timestep should be positive'
    assert len(trajectory.index) > 0, 'not enough points'
    
    delays = trajectory.index.copy()
    shifts = np.floor(delays/t_step).astype(np.int)
    msds = np.zeros(shifts.size)

    for i, shift in enumerate(shifts):
        diffs = trajectory - trajectory.shift(-shift)
        sqdist = np.square(diffs)
        msds[i] = sqdist.mean()

    return delays, msds
#

if __name__ == "__main__":
    import doctest
    sys.exit(doctest.testmod()[0])
    


