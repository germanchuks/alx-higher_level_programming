#include "lists.h"

/**
 * add_dnodeint - adds a new node at the beginning of a dlistint_t list.
 * @head: Pointer to first node of dlistint_t list.
 * @n: Integer to be included in new node.
 * Return: Address of the new element, or NULL if it failed.
 */
dlistint_t *add_dnodeint(dlistint_t **head, const int n)
{
	dlistint_t *temp;
	dlistint_t *ptr = *head;

	temp = malloc(sizeof(dlistint_t));
	if (!temp)
		return (NULL);

	temp->n = n;
	temp->next = ptr;
	temp->prev = NULL;

	if (ptr)
		ptr->prev = temp;

	*head = temp;
	return (temp);
}
