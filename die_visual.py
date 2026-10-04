import plotly.express as px
from die import Die

# Create a D6
die = Die()

# Make some roles, and store results in a list.
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

    # Analize the results.
    frequencies = []
    poss_results = range(1, die.num_sides + 1)
    for value in poss_results:
        frequency = results.count(value)
        frequencies.append(frequency)


# visualiese the results.
title = "Frequensies of Numbers from 1 to 6"
labels = {"x": "Result", "y": "Frequency of Result"}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.show()
