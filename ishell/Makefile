CC = gcc
CFLAGS = -std=gnu99 -Wall -g #-DDEBUG

EXECS = ishell

all: ${EXECS}

#wrappers.c
wrappers.o: wrappers.c wrappers.h
	${CC} ${CFLAGS} -c wrappers.c -o wrappers.o

#ishell.c
ishell: ishell.c wrappers.o
	${CC} ${CFLAGS} ishell.c wrappers.o -o ishell

.PHONY: clean
clean:
	/bin/rm -rf ${EXECS} *.o
