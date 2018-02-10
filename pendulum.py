
import numpy as np
import scipy.constants
import pandas as pd

def oscillation_time(length, times):
    time = times*2*np.pi*np.sqrt(length/scipy.constants.g) + np.random.random()
    return time

def main():
    locations = list(range(10))
    lengths = np.arange(0.1, 0.85, 0.05)
    for location in locations:
        recorders = []
        for length in lengths:
            time_30 = [oscillation_time(length, 30) for i in range(3)]
            period = np.mean(time_30) / 30
            recorder = {
                "length": length,
                "time_30_1": time_30[0],
                "time_30_2": time_30[1],
                "time_30_3": time_30[2],
                "period": period
            }
            recorders.append(recorder)
        df = pd.DataFrame(recorders)
        df.to_csv("measurement_{}.csv".format(location), index=False, float_format="%.3f")

if __name__ == "__main__":
    main()