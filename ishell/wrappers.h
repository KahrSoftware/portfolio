/*
 * Justin Kahr
 * wrappers.h
 * header file for various wrappers
 */

#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>

/**
 * read(2) wrapper
 *
 * @return bytes read
 */
int Read(int fd, void *buf, size_t count);

/**
 * write(2) wrapper
 *
 * @return bytes written
 */
int Write(int fd, const void *buf, size_t count);

/**
 * fork(2) wrapper
 *
 * @return pid of child to parent, 0 to child, -1 on error
 */
pid_t Fork(void);

/**
 * pipe(2) wrapper
 *
 * @return 0 on success, -1 on fail
 */
int Pipe(int pipefd[2]);


/**
 * wait(2) wrapper
 *
 * @return ID of terminated child, or -1 on error
 */
pid_t Wait(int *wstatus);

/**
 * waitpid(2) wrapper
 *
 * @return on success, returns PID of the child whose state has changed, or -1 on error
 */
pid_t Waitpid(pid_t pid, int *wstatus, int options);

/**
 * open(2) wrapper
 *
 * @return new file descriptor on success, -1 on error
 */
int Open(const char *pathname, int flags, mode_t mode);

/**
 * close(2) wrapper
 *
 * @return 0 on success, -1 on error
 */
int Close(int fd);

/**
 * connect(2) wrapper
 *
 * @return 0 on success, -1 on error
 */
int Connect(int sockfd, const struct sockaddr *addr, socklen_t addrlen);

/**
 * bind(2) wrapper
 *
 * @return 0 on success, -1 on error
 */
int Bind(int sockfd, const struct sockaddr *addr, socklen_t addrlen); 

/**
 * listen(2) wrapper
 *
 */
int Listen(int sockfd, int backlog);

/**
 * accept(2) wrapper
 *
 * @return file descriptor for socket on success, -1 on error
 */
int Accept(int sockfd, struct sockaddr *addr, socklen_t *addrlen);
