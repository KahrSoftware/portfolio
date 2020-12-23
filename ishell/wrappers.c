/*
 * Justin Kahr
 * wrappers.c
 * Various wrapper functions
 * compile with: make
 */

#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <sys/socket.h>



#include "wrappers.h"

int Read(int fd, void *buf, size_t count) {
  int ret_val;
  if(-1 == (ret_val = read(fd, buf, count))) {
    perror("READ ERROR: ");
    exit(-1);
  }
  return ret_val;
}

int Write(int fd, const void *buf, size_t count) {
  int ret_val;
  if(-1 == (ret_val = write(fd, buf, count))) {
    perror("WRITE ERROR: ");
    exit(-1);
  }
  return ret_val;
}

pid_t Fork(void) {
  pid_t id;
  if(-1 == (id = fork())) {
    perror("FORK ERROR: ");
    exit(-1);
  }
  return id;
}

int Pipe(int pipefd[2]) {
  int ret_val;
  if(-1 == (ret_val = pipe(pipefd))) {
    perror("PIPE ERROR: ");
    exit(-1);
  }
  return ret_val;
}

pid_t Wait(int *wstatus) {
  pid_t id;
  if(-1 == (id = wait(wstatus))) {
    perror("WAIT ERROR: ");
    exit(-1);
  }
  return id;
}


pid_t Waitpid(pid_t pid, int *wstatus, int options) {
  pid_t id;
  if(-1 == (id = waitpid(pid, wstatus, options))) {
    perror("WAITPID ERROR: ");
    exit(-1);
  }
  return id;
}

int Open(const char *pathname, int flags, mode_t mode) {
  int ret_val;
  if(-1 == (ret_val = open(pathname, flags, mode))) {
    perror("OPEN ERROR: ");
    exit(-1);
  }
  return ret_val;
}

int Close(int fd) {
  int ret_val;
  if(-1 == (ret_val = close(fd))) {
    perror("CLOSE ERROR: ");
    exit(-1);
  }
  return ret_val;
}

int Connect(int sockfd, const struct sockaddr *addr, socklen_t addrlen) {
  int ret_val;
  if(-1 == (ret_val = connect(sockfd, addr, addrlen))) {
    perror("CONNECT ERROR: ");
    exit(-1);
  }
  return ret_val;
}

int Bind(int sockfd, const struct sockaddr *addr, socklen_t addrlen) {
  int ret_val;
  if(-1 == (ret_val = bind(sockfd, addr, addrlen))) {
    perror("BIND ERROR: ");
    exit(-1);
  }
  return ret_val;
}

int Listen(int sockfd, int backlog) {
  int ret_val;
  if(-1 == (ret_val = listen(sockfd, backlog))) {
    perror("LISTEN ERROR");
    exit(-1);
  }
  return ret_val;
}

