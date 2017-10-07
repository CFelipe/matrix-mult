import matplotlib.pyplot as plt
import numpy as np
import subprocess

plt.style.use("ggplot")

filenamePrefix = "matrizes/"
filenameSuffix = ".txt"

sizes = [2 ** x for x in range(2, 12)]

repeats = 20

times = {}

def run_program(name, args):
    args = " ".join(args)
    command = "".join(["./", name, " ", args])
    result_str = subprocess.check_output(command, shell=True)
    # Output é bytestring e ultimo caractere é um newline
    result_str = result_str[:-1].decode("utf-8")
    # Remove os dois últimos caracteres (unidade) e converte pra inteiro
    return float(result_str[:-2])

for i in range(repeats):
    for s in sizes:
        #result_sequential = run_program("multimat_sequencial", [str(s)])
        result_threaded = run_program("multimat_concorrente", [str(s), '4'])

        k = "t" + str(s)
        if k not in times:
            times[k] = {"mat_size": str(s) + "x" + str(s), "times": []}
        times[k]["times"].append(result_threaded)
        print(k)
    print("---")

with open("resultados.txt", "a") as rfile:
    for s in sizes:
        k = "t" + str(s)
        print(k, file=rfile)
        print("threaded (4)", file=rfile)
        print("med: ", np.mean(times[k]["times"]), file=rfile)
        print("max: ", np.amax(times[k]["times"]), file=rfile)
        print("min: ", np.amin(times[k]["times"]), file=rfile)
        print("std: ", np.std(times[k]["times"]), file=rfile)
        print("---", file=rfile)
