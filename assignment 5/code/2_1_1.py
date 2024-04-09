import matplotlib.pyplot as plt

data_points = []
with open('file/flows.txt', 'r') as file:
    for line in file:
        data_points.append(int(line))

x_values = list(range(1, len(data_points) + 1))

plt.scatter(x_values, data_points, marker='o', alpha=0.7)
plt.xlabel('Number of Observations')
plt.ylabel('Data Values')
plt.title('Scatterplot (linear)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
