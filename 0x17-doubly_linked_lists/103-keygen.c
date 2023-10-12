#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/**
 * main - generate a key depending on a username for crackme5
 * @argc: number of arguments passed
 * @argv: arguments passed to main
 *
 * Return: 0 on success, 1 on error
 */
int main(int argc, char *argv[])
{
	size_t username_len, sum;
	unsigned int index, product;
	char *charset =
		"A-CHRDw87lNS0E9B2TibgpnMVys5XzvtOGJcYLU+4mjW6fxqZeF3Qa1rPhdKIouk";
	char key[7] = "      ";

	if (argc != 2)
	{
		printf("Correct usage: ./keygen5 username\n");
		return (1);
	}
	username_len = strlen(argv[1]);
	key[0] = charset[(username_len ^ 59) & 63];
	for (index = 0, sum = 0; index < username_len; index++)
		sum += argv[1][index];

	key[1] = charset[(sum ^ 79) & 63];

	for (index = 0, product = 1; index < username_len; index++)
		product *= argv[1][index];

	key[2] = charset[(product ^ 85) & 63];

	for (product = argv[1][0], index = 0; index < username_len; index++)
		if ((char)product <= argv[1][index])
			product = argv[1][index];
	srand(product ^ 14);
	key[3] = charset[rand() & 63];

	for (product = 0, index = 0; index < username_len; index++)
		product += argv[1][index] * argv[1][index];

	key[4] = charset[(product ^ 239) & 63];

	for (product = 0, index = 0; (char)index < argv[1][0]; index++)
		product = rand();

	key[5] = charset[(product ^ 229) & 63];
	printf("%s\n", key);
	return (0);
}
