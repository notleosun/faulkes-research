import pandas as pd
import numpy as np
import re

appropriateIdentifiers = ['C', 'N', 'A']
listOfDataS = ["XH57_merged.csv", "XX84_merged.csv", "XM156_merged.csv", "XR31_merged.csv", "XO18_merged.csv"]


for j in listOfDataS:
    elevT = 0
    apMagT = 0
    times = []
    numFits = 0
    df = pd.read_csv(j)

    for i in range(len(df)):
        #11hours + UTC time = local time, i.e. 00:00 -> 03:00 local time, sliding springs australia
        if ((int(df.iloc[i].time.replace(":", "")) >= 1300) and (int(df.iloc[i].time.replace(":", "")) <= 1700)) and df.iloc[i].elev > 30 and df.iloc[i].observatory == 'ssf':
            numFits += 1
            elevT += float(df.iloc[i].elev)
            apMagT += float(df.iloc[i].apmag)
            times.append(f"|{df.iloc[i].date}, local time: {(int(df.iloc[i].time.replace(':', ''))+1100)%2400}, uk time: {df.iloc[i].time}, {df.iloc[i].elev}, S|")
        elif ((int(df.iloc[i].time.replace(":", "")) >= 1000) and (int(df.iloc[i].time.replace(":", "")) <= 1400)) and df.iloc[i].elev > 30 and df.iloc[i].observatory == 'hf':
            numFits += 1
            elevT += float(df.iloc[i].elev)
            apMagT += float(df.iloc[i].apmag)
            times.append(f"|{df.iloc[i].date}, local time: {(int(df.iloc[i].time.replace(':', '')) -1000)%2400}, uk time: {df.iloc[i].time}, {df.iloc[i].elev}, N|")
    if numFits == 0:
        numFits = 1

    f = open("eval.txt", 'a')
    f.write(f"{j} \n")
    f.write(f"Av elev: {elevT/numFits}\n")
    f.write(f"Av apmag: {apMagT/numFits}\n")
    f.write(f"Total possible observation time: {0.5*numFits} hours\n")
    f.write(f"Times: {times}")
    f.write("---------------------------------\n\n\n")