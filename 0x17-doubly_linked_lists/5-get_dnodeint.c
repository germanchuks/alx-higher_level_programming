#include "lists.h"

/**
 * get_dnodeint_at_index - Returns the nth node of a dlistint_t linked list.
 * @head: Pointer to first node of dlistint_t list.
 * @index: Index of the node, starting from 0
 * Return: The nth node, otherwise NULL.
 */
dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
	dlistint_t *temp = head;

	if (!temp)
		return (NULL);

	while (index && index > 0)
	{
		temp = temp->next;
		index--;
	}

	return (temp);
}
