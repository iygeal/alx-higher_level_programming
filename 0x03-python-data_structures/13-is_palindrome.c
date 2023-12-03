#include "lists.h"
#include <stddef.h>

/**
 * is_palindrome - Function that checks if a singly linked list is a palindrome
 * @head: Pointer to a pointer to first element in the list
 * Return: 0 if it is not a palindrome, 1 if it is
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (fast->next != NULL && fast->next->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	listint_t *prev = NULL;
	listint_t *current = slow->next;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	listint_t *left = *head;
	listint_t *right = prev;

	while (right != NULL)
	{
		if (left->n != right->n)
			return (0);
		left = left->next;
		right = right->next;
	}
	return (1);
}
