C89_HEADERS = [
    "assert.h",
    "ctype.h",
    "errno.h",
    "float.h",
    "limits.h",
    "locale.h",
    "math.h",
    "setjmp.h",
    "signal.h",
    "stdarg.h",
    "stddef.h",
    "stdio.h",
    "stdlib.h",
    "string.h",
    "time.h",
]

C95_HEADERS = [
    "iso646.h",
    "wchar.h",
    "wctype.h",
]

C99_HEADERS = [
    "complex.h",
    "fenv.h",
    "inttypes.h",
    "stdbool.h",
    "stdint.h",
    "tgmath.h",
    "stdalign.h",
]

# not yet in use
C11_HEADERS = [
    "stdatomic.h",
    "stdnoreturn.h",
    "threads.h",
    "uchar.h",
]


POSIX_HEADERS = [
    "aio.h",
    "arpa/inet.h",
    "cpio.h",
    "dirent.h",
    "dlfcn.h",
    "fcntl.h",
    "fmtmsg.h",
    "fnmatch.h",
    "ftw.h",
    "glob.h",
    "grp.h",
    "iconv.h",
    "langinfo.h",
    "libgen.h",
    "monetary.h",
    "mqueue.h",
    "ndbm.h",
    "net/if.h",
    "netdb.h",
    "netinet/in.h",
    "netinet/tcp.h",
    "nl_types.h",
    "poll.h",
    "pthread.h",
    "pwd.h",
    "regex.h",
    "sched.h",
    "search.h",
    "semaphore.h",
    "spawn.h",
    "strings.h",
    "stropts.h",
    "sys/ipc.h",
    "sys/mman.h",
    "sys/msg.h",
    "sys/resource.h",
    "sys/select.h",
    "sys/sem.h",
    "sys/shm.h",
    "sys/socket.h",
    "sys/stat.h",
    "sys/statvfs.h",
    "sys/time.h",
    "sys/times.h",
    "sys/types.h",
    "sys/uio.h",
    "sys/un.h",
    "sys/utsname.h",
    "sys/wait.h",
    "syslog.h",
    "tar.h",
    "termios.h",
    #"trace.h",
    "ulimit.h",
    "unistd.h",
    "utime.h",
    "utmpx.h",
    "wordexp.h",
]


DEFAULT_HEADERS = C89_HEADERS + C95_HEADERS + C99_HEADERS + POSIX_HEADERS


# taken from https://gcc.gnu.org/onlinedocs/cpp/Search-Path.html
INCLUDE_PATHS = [
    "/usr/local/include/",
    "/usr/target/include/",
    "/usr/include/",
]
