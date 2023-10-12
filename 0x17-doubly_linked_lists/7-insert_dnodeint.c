#include "lists.h"

/**
 * insert_dnodeint_at_index - Inserts a new node at a given position.
 * @h: Double pointer to first node of dlistint_t list.
 * @idx: Index of the list where new node should be added, starting from 0.
 * @n: Integer value to be included in the new node.
 * Return: Address of the new node, or NULL if it failed.
 */
dlistint_t *insert_dnodeint_at_index(dlistint_t **h, unsigned int idx, int n)
{
	dlistint_t *temp = *h;
	dlistint_t *newPtr = malloc(sizeof(dlistint_t));
	unsigned int i;

	if (!h || !newPtr)
		return (NULL);

	newPtr->n = n;
	newPtr->next = NULL;
	newPtr->prev = NULL;

	if (idx == 0)
	{
		newPtr->next = *h;
		if (*h)
			(*h)->prev = newPtr;
		*h = newPtr;
		return (newPtr);
	}

	for (i = 0; i < idx - 1 && temp; i++)
		temp = temp->next;

	if (!temp)
	{
		free(newPtr);
		return (NULL);
	}

	newPtr->prev = temp;
	newPtr->next = temp->next;

	if (temp->next)
		temp->next->prev = newPtr;

	temp->next = newPtr;

	return (newPtr);
}
