#include "lists.h"
/**
 * insert_node - Inserts a node with a given number into a sorted linked list.
 * @head: Pointer to the head of the linked list.
 * @number: Value to be inserted into the linked list.
 * Return: Pointer to the newly inserted node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current_node;
	/* Check if the head pointer is NULL */
	if (head == NULL)
		return (NULL);
	/* Allocate memory for the new node */
	new_node = malloc(sizeof(listint_t));
	/* Check if memory allocation was successful */
	if (new_node == NULL)
		return (NULL);
	/* Initialize new node's values */
	new_node->n = number;
	new_node->next = NULL;
	/* Check if the linked list is empty */
	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}
	/* Set current_node to the head of the linked list */
	current_node = *head;
	/* Check if the new node should be the new head */
	if (current_node->n > number)
	{
		new_node->next = current_node;
		*head = new_node;
		return (new_node);
	}
	/* Traverse the linked list to find the correct position for insertion */
	while (current_node->next != NULL)
	{           /* Insert the new node at the correct position */
		if (current_node->next->n > number)
		{
			new_node->next = current_node->next;
			current_node->next = new_node;
			return (new_node);
		} /* Move to the next node in the linked list */
		current_node = current_node->next;
	}       /* Insert the new node at the end of the linked list */
	current_node->next = new_node;
	return (new_node);
}
