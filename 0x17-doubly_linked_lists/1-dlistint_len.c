#include "lists.h"

/**
 * dlistint_len - Returns the number of elements in a linked list.
 * @h: Pointer to first node of dlistint_t list
 * Return: Number of elements
 */
size_t dlistint_len(const dlistint_t *h)
{
	int count = 0;

	while (h)
	{
		count++;
		h = h->next;
	}
	return (count);
}
