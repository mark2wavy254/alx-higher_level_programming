#include "lists.h"
#include <stdio.h>

void reverse(listint_t **head);
int compare_lists(listint_t *head, listint_t *middle, int len);

/**
 * is_palindrome - checks for a palindrome
 * head: double pointer to a list
 *
 * Return: 0 if the list is not a palindrome.
 * 1 if it is.
 */

int is_palindrome(listint_t **head)
{
	int len, i;
	listint_t *temp;
	listint_t *middle;

	if (head == NULL || *head == NULL)
	{
		return (1);
	}
	temp = *head;
	middle = *head;

	for (len = 0; temp != NULL; len++)
	{
		temp = temp->next;
	}
	len = len / 2;

	for (i = 1; i < len; i++)
	{
		middle = middle->next;
	}
	if (len % 2 == 0 && len != 1)
	{
		middle = middle->next;
		len = len - 1;
	}
	reverse(&middle);
	i = compare_lists(*head, middle, len);

	return (i);
}

/**
 * compare_lists - compare the lists
 * @head: pointer to the head node
 * @middle: pointer to the middle node
 * @len: length of the list
 *
 * Return: if the same 1, if not 0.
 */

int compare_lists(listint_t *head, listint_t *middle, int len)
{
	int i;

	if (head == NULL || middle == NULL)
	{
		return (1);
	}

	for (i = 0; i < len; i++)
	{
		if (head->n != middle->n)
		{
			return (0);
		}
		head = head->next;
		middle = middle->next;
	}
	return (1);
}

/**
 * reverse - reverse a list
 * @head: pointer to the head of a list to reverse
 */

void reverse(listint_t **head)
{
	listint_t *current;
	listint_t *next;
	listint_t *previous;

	if (head == NULL || *head == NULL)
	{
		return;
	}
	previous = NULL;
	current = *head;

	while (current != NULL)
	{
		next = current->next;
		current->next = previous;
		previous = current;
		current = next;
	}
	*head = previous;
}
