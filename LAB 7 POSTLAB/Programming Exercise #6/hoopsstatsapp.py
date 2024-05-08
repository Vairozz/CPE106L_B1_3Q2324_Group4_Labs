import pandas as pd
from hoopstatsview import HoopStatsView

def cleanStats(frame):
    frame.dropna(inplace=True)
    frame.reset_index(drop=True, inplace=True)
    return frame

def main():
    frame = pd.read_csv("cleanbrogdonstats.csv")
    cleaned_frame = cleanStats(frame)
    hoop_stats_view = HoopStatsView(cleaned_frame)
    hoop_stats_view.mainloop()

if __name__ == "__main__":
    main()
