/*
 * Justin Kahr
 * CSCI 315 Lab09
 * ishell.c
 * A custom shell using the c exec function
 * compile with: make
 */

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <sys/wait.h>
#include <errno.h>

#include "wrappers.h"

int main(int argc, char* argv[]) {

  // input, 100 char max size
  char input[100];
  int in_count;
  char cmd[100];
  char cmd2[100];
  char prev_cmd[100];
  char *cmdtok;
  char *pass_args[100];
  char *pass_args2[100];
  char * prev_pass_args[100];
  int pass_argsc = 0;
  int pid = 1;
  int child_status;

  // while not exit
  while(1) {
    
    // first, print ishell, get user input
    if(0 != pid) {

      printf("ishell> ");
      // get user input
      //fgets(input, 500, stdin);
      
      // trying to make tab tab work, very not easy
      in_count = 0;
      while(in_count < 100) {
	//printf("%d",in_count);
	input[in_count] = fgetc(stdin);
	if('\0' == input[in_count] || '\n' == input[in_count]) {
	  //printf("Input done\n");
	  input[in_count+1] = '\0';
	  if(1 < in_count && '\t' == input[in_count-2] && '\t' == input[in_count-1] ) {
	    input[0] = 'l';
	    input[1] = 's';
	    input[2] = '\n';
	    input[3] = '\0';
	  }
	break;
	}
	in_count+=1;
      }

      //printf("%s\n", input);
      //printf("%d\n", strcmp(input, "exit\n"));

      // exit
      if(0 == strcmp(input, "exit\n")) {
	printf("BYE\n");
	return 0;
      }
      // cut off the \n
      strtok(input, "\n");
      
      // tokenize the command by spaces
      cmdtok = strtok(input, " ");

      pass_argsc = 0;
      while(NULL != cmdtok) {
	pass_args[pass_argsc++] = cmdtok;
	cmdtok = strtok(NULL, " ");
	//printf(">%s\n", pass_args[pass_argsc-1]);
      }
      pass_args[pass_argsc] = NULL;

      // reset commands
      memset(cmd, '\0', sizeof(cmd));
      // add /usr/bin to the front
      strcpy(cmd, "/usr/bin/");
      strcat(cmd, pass_args[0]);
      pass_args[0] = cmd;

      // if first cmd is /usr/bin/!!, do the last command
      if(0 == strcmp(pass_args[0], "/usr/bin/!!")) {
	//use the last command as this one
	strcpy(cmd, prev_cmd);
	int counter = 0;
	while(1) {
	  if(NULL == prev_pass_args[counter])
	    break;
	  pass_args[counter] = strdup(prev_pass_args[counter]);
	  counter++;
	}
	pass_args[counter] = NULL;
      }
      // else if the command is /usr/bin/sudo !!, try and sudo the last command
      // I can't really test to make sure this works, as I don't have sudo access
      // but the sudo password prompt comes up so hopefully good enough?
      else if(NULL != pass_args[1] && 0 == strcmp(pass_args[1], "!!") && 0 == strcmp(pass_args[0], "/usr/bin/sudo")) {
	// use the last command but shifted over one
	int counter = 0;
	while(1) {
	  if(NULL == prev_pass_args[counter])
	    break;
	  pass_args[counter+1] = strdup(prev_pass_args[counter]);
	  counter++;
	}
	pass_args[counter+1] = NULL;
      }
      // else, save the command we are about to run as the old one
      else {
	strcpy(prev_cmd, cmd);
	int counter = 0;
	while(1) {
	  if(NULL == pass_args[counter])
	    break;
	  prev_pass_args[counter] = strdup(pass_args[counter]);
	  counter++;
	}
	prev_pass_args[counter] = NULL;
      }

    }
    // second, fork
    if(0 == (pid = Fork())) {
      int ret = 0;
      int curr = 0;
      int second = 0;
      while(1) {
	// if we have found a second command start copying it
	if(second > 0) {
	  pass_args2[curr-second-1] = strdup(pass_args[curr]);
	  if(1 == curr-second) {
	    // make sure the first command is null terminated
	    pass_args[curr] = NULL;
	  }
	  
	}
	// if this args ends with ;
	if(0 == second && ';' == pass_args[curr][strlen(pass_args[curr])-1]) {
	  // remember where second command starts
	  second = curr;
	  // remove the ";"
	  pass_args[curr][strlen(pass_args[curr])-1] = '\0';
	  // add /usr/bin to cmd2
	  strcpy(cmd2, "/usr/bin/");
	  strcat(cmd2, pass_args[curr+1]);
	  pass_args[curr+1] = cmd2;
	}
	// incrament current, break when we reach the end of pass_args
	curr++;
	if(NULL == pass_args[curr]) {
	  break;
	}
      }
      // if we are gonna have two commands
      if(second > 0) {
	// fork again, exec cmd 1
	if(0 == Fork()) {
	  ret = execv(cmd, pass_args);
	  exit(ret);
	}
	// wait for cmd 1, if it worked run cmd 2
	else {
	  Wait(NULL);
	  if(0 == ret) {
	    ret = execv(cmd2, pass_args2);
	  }
	  exit(-1);
	}
      }
      // else only 1 command, just run it
      else {
	ret = execv(cmd, pass_args);
	exit(ret);
      }

    }

    // third, wait for fork
    else {
      
      Wait(&child_status);

      // then print out termination message for child
      if(0 == child_status)
	printf("[ishell: program terminated %s successfully]\n", cmd);
      else
	printf("[ishell: program terminated abnormally %d]\n", child_status);

    }

  }

  return 0;
}
