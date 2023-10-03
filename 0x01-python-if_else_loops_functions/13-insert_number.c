#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - Inserts a node with a value into a sorted linked list.
 * @head: A pointer to the head of the linked list.
 * @number: The value to insert.
 *
 * Return: A pointer to the new node, or NULL if it fails.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode, *currentNode, *prevNode;

	if (!head)
		return (NULL);
	newNode = malloc(sizeof(listint_t));
	if (!newNode)
		return (NULL);
	newNode->n = number;
	newNode->next = NULL;
	if (!*head)
	{
		*head = newNode;
		return (newNode);
	}
	currentNode = *head;
	prevNode = NULL;
	while (currentNode && currentNode->n < number)
	{
		prevNode = currentNode;
		currentNode = currentNode->next;
	}
	if (!prevNode)
	{
		newNode->next = *head;
		*head = newNode;
	}
	else
	{
		prevNode->next = newNode;
		newNode->next = currentNode;
	}
	return (newNode);
}
