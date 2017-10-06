import matplotlib.pyplot as plt
import numpy as np
import subprocess

plt.rcParams["font.family"] = "monospace"

plt.style.use("ggplot")

filenamePrefix = "matrizes/"
filenameSuffix = ".txt"

n_size = 512
thread_sizes = range(1, 20)

repeats = 20

def run_program(name, args):
    args = " ".join(args)
    command = "".join(["./", name, " ", args])
    result_str = subprocess.check_output(command, shell=True)
    # Output é bytestring e ultimo caractere é um newline
    result_str = result_str[:-1].decode("utf-8")
    # Remove os dois últimos caracteres (unidade) e converte pra inteiro
    return float(result_str[:-2])

means = []
for t in thread_sizes:
    times = []
    print("#", t)
    for i in range(repeats):
        print(i)
        result_threaded = run_program("multimat_concorrente", [str(n_size), str(t)])
        times.append(result_threaded)
    means.append(np.mean(times))

plt.plot(means, 'o')
plt.xticks(range(len(thread_sizes)), [str(size) for size in thread_sizes])
plt.xlabel('Número de threads')
plt.ylabel('Tempo de execução (ms)')
plt.title('Tempo de execução para matrizes {n}x{n}'.format(n=n_size))
plt.show()
print(means)
