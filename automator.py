import numpy as np
import subprocess

filenamePrefix = "matrizes/"
filenameSuffix = ".txt"

sizes = [2 ** x for x in range(2, 12)][:-1]

repeats = 10

times_sequential = {}
times_concurrent = {}

print("Sequencial")
for i in range(repeats):
    for s in sizes:
        #print("{size}x{size}: ".format(size=s).rjust(15), end="")
        result_str = subprocess.check_output("./multimat_sequencial {}".format(s), shell=True)
        # Output é bytestring e ultimo caractere é um newline
        result_str = result_str[:-1].decode("utf-8")
        result = {}
        # Divide a saída do programa pelos "|", remove os dois últimos caracteres (unidade) e converte pra inteiro
        result["ms"], result["us"], result["ns"] = [int(string.strip()[:-2]) for string in result_str.split("|")]

        k = "t" + str(s)
        if k not in times_sequential:
            times_sequential[k] = {"mat_size": str(s) + "x" + str(s), "times": []}
        times_sequential[k]["times"].append(result)
        print(k)

#print(times_sequential)
#print(times_sequential["t512"]["times"])
print(np.mean([time["ms"] for time in times_sequential["t1024"]["times"]]))

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

#"{prefix}A{mat_size}x{mat_size}{suffix}".format(prefix = filenamePrefix, \
#                                                mat_size = s, \
#                                                suffix = filenameSuffix))
#"{prefix}B{mat_size}x{mat_size}{suffix}".format(prefix = filenamePrefix, \
#				                                 mat_size = s, \
#				                                 suffix = filenameSuffix))
