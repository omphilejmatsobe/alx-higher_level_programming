#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inputs a number sorted in a list
 * @head: input type double pointer
 * @number: data type int number to be added
 * Return: 0 if no cycle, 1 if there is cycle
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *i = *head;
	listint_t *r;

	r = malloc(sizeof(listint_t));
	if (r == NULL)
		return (NULL);
	r->n = number;

	if (i == NULL || i->n >= number)
	{
		r->next = i;
		*head = r;
		return (r);
	}
	while (i && i->next && i->next->n < number)
		i = i->next;

	r->next = i->next;
	i->next = r;

	return (r);
}
