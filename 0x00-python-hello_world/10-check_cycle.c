#include "lists.h"
/**
 * check_cycle - Function that checks if a singly linked list
 * has a cycle or not
 * @list: Pointer to the first node in the singly linked list
 * Return: Function returns 1 if cycle exists or 0 if not
 */

int check_cycle(listint_t *list)
{
	listint_t *fast_ptr = list;
	listint_t *slow_ptr = list;

	while (slow_ptr && fast_ptr && fast_ptr->next)
	{
		slow_ptr = slow_ptr->next;
		fast_ptr = fast_ptr->next->next;
		if (slow_ptr == fast_ptr)
			return (1);
	}
	return (0);
}
