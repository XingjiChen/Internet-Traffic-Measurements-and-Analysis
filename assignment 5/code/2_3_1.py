import matplotlib.pyplot as plt

data_point = []
with open('file/flows.txt', 'r') as file:
    for line in file:
        data_point.append(int(line))

plt.boxplot(data_point, sym='b+')
plt.ylabel('Data Values')
plt.title('Boxplot (linear)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
