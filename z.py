import statistics
import plotly.graph_objects as go
import plotly.figure_factory as ff
import pandas as pd
import random

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

population_mean = statistics.mean(data)
print("Population mean is:", population_mean)

population_sd = statistics.stdev(data)
print("Population mean is:", population_sd)

def random_set_of_mean(counter):
    dataset=[]
    for i in range(0, counter):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean1 = statistics.mean(dataset)
    return mean1


mean_list = []
for i in range(0, 100):
    set_of_means = random_set_of_mean(30)
    mean_list.append(set_of_means)

mean = statistics.mean(mean_list)
print("Mean of sampling dist:", mean)

sd = statistics.stdev(mean_list)
print("Sd of sampling dist:", sd)

first_std_deviation_start, first_std_deviation_end = mean-sd, mean+sd
second_std_deviation_start, second_std_deviation_end = mean-(2*sd), mean+(2*sd)
third_std_deviation_start, third_std_deviation_end = mean-(3*sd), mean+(3*sd)
print("std1",first_std_deviation_start, first_std_deviation_end)
print("std2",second_std_deviation_start, second_std_deviation_end)
print("std3",third_std_deviation_start,third_std_deviation_end)

# plotting the graph with teaces
fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.7], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[population_mean, population_mean], y=[0, 0.7], mode="lines", name="MEAN OF STUDENTS WHO GOT TABLETS"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.7], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end], y=[0, 0.7], mode="lines", name="STANDARD DEVIA1ION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.7], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()

z_score = (population_mean-mean)/sd
print("The z score is = ", z_score)