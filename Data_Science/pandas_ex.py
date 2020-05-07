import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('~/Desktop/Python_Learning/Data_Science/estimates_15item_N500_rep1.csv')

print(df.info())
print(df.head())
print(df.tail())

# select columns
a = df['a.parm']
a_se = df['a.se']
print("The mean of a is " + str(a.mean()))
print("The mean SE of a is " + str(a_se.mean()))

# select row
## select a is larger than 1
df[df['a.parm'] > 1]
### select item 2's parameter

# plot using pyplot
plt.plot(df['a.parm'], df['a.se'], label = "a")
plt.plot(df['d.parm'], df['d.se'], label = "d", color = "green")
plt.xlabel("Parameter")
plt.ylabel("Standard Error")
plt.title("Estimates with SE")
plt.text(1.2, 0.25, "a is monotonic", color = "Darkgrey")
plt.legend()
plt.show()