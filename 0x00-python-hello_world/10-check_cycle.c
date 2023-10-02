#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *slow_ptr, *fast_ptr;

	if (list == NULL)
		return (0);

	slow_ptr = list;
	fast_ptr = list;

	while (fast_ptr != NULL && fast_ptr->next != NULL)
	{
		slow_ptr = slow_ptr->next;
		fast_ptr = fast_ptr->next->next;

		if (slow_ptr == fast_ptr)
			return (1);
	}

	return (0);
}
