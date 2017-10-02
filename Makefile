CFLAGS = -std=c++11 -O3 -g -Wall

UNAME_S := $(shell uname -s)
ifeq ($(UNAME_S),Linux)
	CC = g++
	CFLAGS += -pthread
endif
ifeq ($(UNAME_S),Darwin)
	CC = clang++
	CFLAGS += -stdlib=libc++
endif

.PHONY: all clean

all: multimat_sequencial multimat_concorrente

multimat_sequencial: multimat_sequencial.o common.h
	$(CC) $(CFLAGS) $< -o $@

multimat_concorrente: multimat_concorrente.o common.h
	$(CC) $(CFLAGS) $< -o $@

%.o: %.cpp
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	-rm -f *.o
	-rm -f multimat_concorrente
	-rm -f multimat_sequencial
