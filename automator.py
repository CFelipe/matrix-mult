import matplotlib.pyplot as plt
import numpy as np
import subprocess

plt.style.use("ggplot")

filenamePrefix = "matrizes/"
filenameSuffix = ".txt"

sizes = [2 ** x for x in range(2, 12)][:-2]

repeats = 20

times_sequential = {}
times_concurrent = {}

print("Sequencial")
for i in range(repeats):
    for s in sizes:
        #print("{size}x{size}: ".format(size=s).rjust(15), end="")
        result_str = subprocess.check_output("./multimat_sequencial {}".format(s), shell=True)
        # Output é bytestring e ultimo caractere é um newline
        result_str = result_str[:-1].decode("utf-8")
        # Remove os dois últimos caracteres (unidade) e converte pra inteiro
        result = float(result_str[:-2])

        k = "t" + str(s)
        if k not in times_sequential:
            times_sequential[k] = {"mat_size": str(s) + "x" + str(s), "times": []}
        times_sequential[k]["times"].append(result)
        print(k)
    print("---")

print(repeats, "repetições")
for s in sizes:
    print("Médias para " + str(s) + "x" + str(s) + ":")
    print(np.mean(times_sequential["t" + str(s)]["times"]), "ms", sep="")

boxplot_data = [times_sequential["t" + str(s)]["times"] for s in sizes]
boxplot_labels = [str(s) for s in sizes]
plt.figure()
plt.boxplot(boxplot_data, labels=boxplot_labels)
plt.show()

## Concorrente
#print()
#print("Concorrente (4 threads)")
#for s in sizes:
#    print("{size}x{size}: ".format(size=s).rjust(15), end="")
#    out = subprocess.check_output("./multimat_concorrente {} {}".format(s, 4), shell=True)
#    out = out[:-1].decode("utf-8")
#    print(out)

#print()
#print("Sequencial")
#for size, time in times_sequential.items():
#    print(size.rjust(5), ":", time.rjust(5))
