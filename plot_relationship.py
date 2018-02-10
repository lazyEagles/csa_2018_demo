
import pandas as pd
import matplotlib.pyplot as plt

def main():
    locations = list(range(10))
    for location in locations:
        df = pd.read_csv("measurement_{}.csv".format(location))
        plt.plot(df["length"], df["period"])
        plt.axis([0.1,0.8,0,2])
        plt.grid()
        plt.xlabel("Length (m)")
        plt.ylabel("Period (sec)")
        plt.title("Location {}".format(location))
        plt.savefig("plot_{}.png".format(location))

if __name__ == "__main__":
    main()