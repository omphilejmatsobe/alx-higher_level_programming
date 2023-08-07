#include "lists.h"
/**
 * check_cycle - check for the loop in a linked list
 * @list: input listint_t pointer of list
 * Return: 0 if success, 1 if there is cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *one;
	listint_t *two;

	if (list == NULL || list->next == NULL)
		return  (0);

	one = list->next;
	two = list->next->next;

	while (one && two && two->next)
	{
		if (one == two->next)
		{
			return (1);
		}
		one = one->next;
		two = two->next->next;
	}

	return (0);
}

