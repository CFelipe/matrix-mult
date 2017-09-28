CC = g++
CFLAGS = -std=c++11 -g -Wall

.PHONY: all clean

all: multimat_sequencial multimat_concorrente

multimat_sequencial: multimat_sequencial.o
	$(CC) $(CFLAGS) $< -o $@

multimat_concorrente: multimat_concorrente.o
	$(CC) $(CFLAGS) $< -o $@ 

%.o: %.cpp
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	-rm -f *.o
	-rm -f multimat_concorrente
	-rm -f multimat_sequencial
