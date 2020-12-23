## ishell

This program is a custom unix shell I wrote. It takes in a unix command and spawns a child process. The child process then uses the c command execv to run the original command.

ishell supports unix commands in `/usr/bin`. It can also perform two commands in sequence using the syntax `a; b`. The command `[tab] [tab]` is a wrapper for `ls .` and `!!` is a shortcut to repeat the previous command. This program is not cross platform, and will not work on Windows or MacOS.

To compile and run this project:

- From the `ishell` directory:
- Run `make` to automatically compile.
- Run `./ishell` to start the program.