import matplotlib.pyplot as plt
import numpy as np
import subprocess

plt.rcParams["font.family"] = "monospace"

plt.style.use("ggplot")

matrix_sizes = [2 ** x for x in range(2, 12)]

means_seq = [0.0018, 0.0032, 0.0074, 0.0369, 0.2762, 2.4222, 23.2958, 259.6764, 10020.0315, 88398.8450]
means_con = [0.2129, 0.2912, 0.6439, 1.2316, 0.5539, 1.9905, 12.8657, 125.2099, 5196.9255, 44531.8250]

plt.xticks(range(len(matrix_sizes)), [str(size) for size in matrix_sizes])
plt.xlabel('Workload')
plt.ylabel('Tempo de execução (ms)')
plt.title('Tempo de execução para workloads diferentes')
plt.semilogy(means_seq, 'o', label="Sequencial")
plt.grid(True, which="both", color='0.80')
plt.semilogy(means_con, 'o', label="Concorrente")
ax = plt.gca()
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels)
plt.show()
