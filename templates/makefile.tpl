CFLAGS  = -shared -fpic
LDFLAGS = -ldl
CC = gcc

all: {{library_name}}.so

{{library_name}}.so: {{library_name}}.c
	$(CC) $(LDFLAGS) $(CFLAGS) -o $@ $<
