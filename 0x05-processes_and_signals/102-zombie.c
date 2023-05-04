#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

/**
 * infinite_while - an infinite while loop
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - the main function
 * Return: 0
 */
int main(void)
{
	int a;
	pid_t zombie;

	for (a = 0; a < 5; a++)
	{
		zombie = fork();
		if (!zombie)
			return (0);
		printf("Zombie process created, PID: %i\n", zombie);
	}

	infinite_while();
	return (0);
}

