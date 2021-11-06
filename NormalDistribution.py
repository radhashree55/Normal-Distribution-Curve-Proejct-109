# Normal Distribution for Readinhg Scores in the CSV File.
import csv
import pandas as pd
import statistics as st
import plotly.graph_objects as go
import plotly.figure_factory as ff

df = pd.read_csv("StudentsPerformance.csv")
data = df["reading score"].tolist()

mean = st.mean(data)
print("Mean of the data is {}.".format(mean))

median = st.median(data)
print("Median of the data is {}.".format(median))

mode = st.mode(data)
print("Mode of the data is {}.".format(mode))

stdev = st.stdev(data)
print("Standard Deviation of the data is {}.".format(stdev))

std1Start, std1End = mean - stdev, mean + stdev
std2Start, std2End = mean - (2 * stdev), mean + (2 * stdev)
std3Start, std3End = mean - (3 * stdev), mean + (3 * stdev)

listOFstd1 = [result for result in data if result > std1Start and result < std1End]
listOFstd2 = [result for result in data if result > std2Start and result < std2End]
listOFstd3 = [result for result in data if result > std3Start and result < std3End]

print(
    "{}% of data lies within 1 Standard Deviation.".format(
        len(listOFstd1) * 100 / len(data)
    )
)
print(
    "{}% of data lies within 2 Standard Deviations.".format(
        len(listOFstd2) * 100 / len(data)
    )
)
print(
    "{}% of data lies within 3 Standard Deviations.".format(
        len(listOFstd3) * 100 / len(data)
    )
)

fig = ff.create_distplot([data], ["reading scores"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="Mean"))
fig.add_trace(
    go.Scatter(
        x=[std1Start, std1Start],
        y=[0, 0.17],
        mode="lines",
        name="1 Standard Deviation",
    )
)
fig.add_trace(
    go.Scatter(
        x=[std2End, std2End],
        y=[0, 0.17],
        mode="lines",
        name="1 Standard Deviation",
    )
)
fig.add_trace(
    go.Scatter(
        x=[std2Start, std2Start],
        y=[0, 0.17],
        mode="lines",
        name="2 Standard Deviations",
    )
)
fig.add_trace(
    go.Scatter(
        x=[std3End, std3End],
        y=[0, 0.17],
        mode="lines",
        name="2 Standard Deviations",
    )
)
fig.show()
