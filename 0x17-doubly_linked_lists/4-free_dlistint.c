#include "lists.h"

/**
 * free_dlistint - frees a dlistint_t list.
 * @head: Pointer to first node of dlistint_t list.
 * Return: Nothing
 */
void free_dlistint(dlistint_t *head)
{
	dlistint_t *temp, *ptr;

	ptr = head;

	while (ptr)
	{
		temp = ptr;
		ptr = ptr->next;
		free(temp);
	}
}
