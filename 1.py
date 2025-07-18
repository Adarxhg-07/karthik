import pandas as pd

df = pd.read_excel("steps.xlsx")  # replace with your file name if different

steps = df['Steps walked'].tolist()

updated_steps = list(map(lambda x: x + 2000, steps))
more_than_9000 = list(filter(lambda x: x > 9000, updated_steps))
sorted_steps = sorted(updated_steps)

print("Updated steps (after adding 2000):", updated_steps)
print("Steps more than 9000:", more_than_9000)
print("Sorted steps:", sorted_steps)
mport pandas as pd

# Sample DataFrame
data = {
    'Department': ['IT', 'HR', 'IT', 'HR', 'Finance', 'Finance'],
    'Name': ['John', 'Amy', 'Robert', 'Alice', 'Tom', 'Jerry']
}
df = pd.DataFrame(data)

# Group by Department and get first and last
print(df.groupby('Department').agg(['first', 'last']))
