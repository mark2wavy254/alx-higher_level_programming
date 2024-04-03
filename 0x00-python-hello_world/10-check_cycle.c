#include "lists.h"

/**
 * check_cycle - checks whether a linked listint_t has a cycle
 * @list: the list to be checked
 *
 * Return: If a cycle is present, 1.
 * Otherwise, 0.
 */

int check_cycle(listint_t *list)
{
	listint_t *a = list;

	listint_t *b = list;

	if (!list)
		return (0);
	while(a && b && b->next)
	{
		a = a->next;
		b = b->next->next;
		if (a == b)
			return (1);
	}

	return (0);
}
