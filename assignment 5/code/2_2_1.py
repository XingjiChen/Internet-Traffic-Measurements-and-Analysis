import matplotlib.pyplot as plt

data_point = []
with open('file/flows.txt', 'r') as file:
    for line in file:
        data_point.append(int(line))

plt.hist(data_point, bins=20, color='skyblue', edgecolor='black', alpha=0.7)
plt.xlabel('Data Values')
plt.ylabel('Frequency')
plt.title('Histogram (linear)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
