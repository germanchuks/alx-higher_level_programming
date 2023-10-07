#include "lists.h"

/**
 * reverse_list - Reverse a linked list
 * @head: Pointer to the head of the list
 * Return: Pointer to the new head of the reversed list
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return (prev);
}

/**
 * is_palindrome - Check if a linked list is a palindrome
 * @head: Pointer to a pointer to the head of the list
 * Return: 1 if it is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow_ptr = *head;
	listint_t *fast_ptr = *head;
	listint_t *prev_slow = *head;
	listint_t *second_half = NULL;

	if (head == NULL || *head == NULL)
		return (1);

	while (fast_ptr && fast_ptr->next)
	{
		fast_ptr = fast_ptr->next->next;
		prev_slow = slow_ptr;
		slow_ptr = slow_ptr->next;
	}

	second_half = reverse_list(slow_ptr);

	while (second_half)
	{
		if ((*head)->n != second_half->n)
			return (0);
		*head = (*head)->next;
		second_half = second_half->next;
	}

	prev_slow->next = reverse_list(slow_ptr);

	return (1);
}
