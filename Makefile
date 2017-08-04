NAME=hasher
INCLUDES=-I.
CFLAGS=-g -Wall -pedantic $(shell pkg-config --cflags libglade-2.0) -export-dynamic -std=c99
LDFLAGS=-lssl $(shell pkg-config --libs libglade-2.0) -export-dynamic

all:
	gcc ${CFLAGS} -c ${NAME}.c -o ${NAME}.o
	gcc ${NAME}.o -o ${NAME} ${LDFLAGS}

asm: 
	objdump -Sx ${NAME}.o > ${NAME}.asm

mingw:
	mingcc ${CFLAGS} -c ${NAME}.c -o ${NAME}.o
	mingcc ${NAME}.o -o ${NAME}.exe ${LDFLAGS}
	
clean:
	rm -f *.o ${NAME} *~ *.exe
