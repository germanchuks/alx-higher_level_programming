#include "lists.h"

/**
 * sum_dlistint - Returns the sum of all the data (n) of a
 * dlistint_t linked list.
 * @head: Pointer to first node of dlistint_t list.
 * Return: Sum of all data, otherwise 0.
 */
int sum_dlistint(dlistint_t *head)
{
	dlistint_t *temp = head;
	int sum = 0;

	if (!head)
		return (0);

	while (temp)
	{
		sum += temp->n;
		temp = temp->next;
	}

	return (sum);
}
