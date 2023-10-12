#include "lists.h"

/**
 * print_dlistint - Prints all the elements of a list.
 * @h: Pointer to first node of dlistint_t list
 * Return: Number of nodes
 */
size_t print_dlistint(const dlistint_t *h)
{
	int count = 0;

	while (h)
	{
		printf("%d\n", h->n);
		h = h->next;
		count++;
	}
	return (count);
}
