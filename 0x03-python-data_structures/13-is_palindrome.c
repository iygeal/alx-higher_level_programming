#include "lists.h"
#include <stddef.h>
/**
 * reverse_list - Function that reverses a singly linked list
 * @head: Pointer to a pointer to the first node in the list
 * Return: Returns pointer to the first node of the reversed list
 */
void reverse_list(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}

/**
 * is_palindrome - Function that checks if a singly linked list is a palindrome
 * @head: Pointer to a pointer to the first node in the list
 * Return: 1 if it is a palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *aux = *head;
	listint_t *dup = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			dup = slow->next;
			break;
		}
		if (!fast->next)
		{
			dup = slow->next->next;
			break;
		}
		slow = slow->next;
	}
	reverse_list(&dup);

	while (dup != NULL && aux != NULL)
	{
		if (aux->n == dup->n)
		{
			dup = dup->next;
			aux = aux->next;
		}
		else
			return (0);
	}
	if (!dup)
		return (1);
	else
		return (0);
}
