from subprocess import call

filenamePrefix = "matrizes/"
filenameSuffix = ".txt"

sizes = [2 ** x for x in range(2, 12)]

for s in sizes:
    print("{prefix}A{mat_size}x{mat_size}{suffix}".format(prefix = filenamePrefix,\
                                                          mat_size = s,\
                                                          suffix = filenameSuffix))
