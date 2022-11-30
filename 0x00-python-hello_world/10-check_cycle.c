#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - checks if a linked list has a cycle
 * @list: linked list to be checked
 *
 * Return: 1 if linked list has a cycle or
 * 0 if linked list does not have a cycle or
 * -1 if there are any other errors
 */
int check_cycle(listint_t *list)
{
	listint_t *head;

	head = list;
	while (list->next != head && list->next != NULL)
		list = list->next;

	if (list->next == head)
	{
		return (1);
	}

	else if (list->next == NULL)
	{
		return (0);
	}

	else
	{
		return (-1);
	}
}
