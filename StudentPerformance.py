from os import name
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import csv

df = pd.read_csv("StudentsPerformance.csv")
data = df["reading score"].tolist()
mean = sum(data)/len(data)
std_deviation = statistics.stdev(data)
median = statistics.median(data)
mode = statistics.mode(data)

first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)

fig = ff.create_distplot([data], ["Students Performance"], show_hist= False)
fig.add_trace(go.Scatter(x=[mean,mean], y=[0, 0.17], mode="lines", name="Mean"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.17], mode="lines", name="First std deviation Start"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="First std deviation End"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start, first_std_deviation_start], y=[0, 0.17], mode="lines", name="Second std deviation Start"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="Second std deviation End"))
fig.show()
list_of_first_std = [
                        result for result in data if result > first_std_deviation_start and result < first_std_deviation_end
                        ]

list_of_second_std = [
                        result for result in data if result > second_std_deviation_start and result < second_std_deviation_end
                        ]

list_of_third_std = [
                        result for result in data if result > third_std_deviation_start and result < third_std_deviation_end
                        ]

print("Mean of this data is {}".format(mean))
print("Median of this data {}".format(median))
print("Mode of this data is {}". format(mode))
print("Standard deviation of this data is {}". format(std_deviation))
print("{}% of the data lies within 1 standard deviation".format(len(list_of_first_std) * 100.0/len(data)))
print("{}% of the data lies within 2 standard deviation".format(len(list_of_second_std) * 100.0/len(data)))
print("{}% of the data lies within 3 standard deviation".format(len(list_of_third_std) * 100.0/len(data)))