import subprocess

filenamePrefix = "matrizes/"
filenameSuffix = ".txt"

sizes = [2 ** x for x in range(2, 12)][:-2]

times_sequential = {}
times_concurrent = {}

# Sequencial
print("Sequencial")
for s in sizes:
    print("{size}x{size}: ".format(size=s).rjust(15), end="")
    out = subprocess.check_output("./multimat_sequencial {}".format(s), shell=True)
    # Output é bytestring e ultimo caractere é um newline
    out = out[:-1].decode("utf-8")
    print(out)
    times_sequential["n" + str(s)] = out

# Concorrente
print()
print("Concorrente (4 threads)")
for s in sizes:
    print("{size}x{size}: ".format(size=s).rjust(15), end="")
    out = subprocess.check_output("./multimat_concorrente {} {}".format(s, 4), shell=True)
    out = out[:-1].decode("utf-8")
    print(out)

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
