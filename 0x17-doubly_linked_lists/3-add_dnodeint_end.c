#include "lists.h"

/**
 * add_dnodeint_end - adds a new node at the end of a dlistint_t list.
 * @head: Pointer to first node of dlistint_t list.
 * @n: Integer to be included in new node.
 * Return: Address of the new element, or NULL if it failed.
 */
dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)
{
	dlistint_t *temp, *ptr;

	temp = malloc(sizeof(dlistint_t));

	if (!temp)
		return (NULL);

	temp->n = n;
	temp->prev = NULL;
	temp->next = NULL;

	if (!*head)
		*head = temp;
	else
	{
		ptr = *head;
		while (ptr->next)
			ptr = ptr->next;

		temp->prev = ptr;
		ptr->next = temp;
	}

	return (temp);
}
