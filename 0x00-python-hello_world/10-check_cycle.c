#include "lists.h"
#include <stdlib.h>

/**
 * _realloc - reallocates a memory block
 * @ptr: pointer to the previous memory block
 * @old_size: size of the old memory block
 * @new_size: size of the new memory block
 *
 * Return: pointer to the new memory block, else NULL
 */

void *_realloc(void *ptr, unsigned int old_size, unsigned int new_size)
{
	void *new_ptr;
	unsigned int min_size = old_size < new_size ? old_size : new_size;
	unsigned int i;

	if (new_size == old_size)
		return (ptr);
	if (ptr)
	{
		if (new_size == 0)
		{
			free(ptr);
			return (NULL);
		}
		new_ptr = malloc(new_size);
		if (new_ptr != NULL)
		{
			for (i = 0; i < min_size; i++)
				*((char *)new_ptr + i) = *((char *)ptr + 1);
			free(ptr);
			return (new_ptr);
		}

		free(ptr);
		return (NULL);
	}
	else
	{
		new_ptr = malloc(new_size);
		return (new_ptr);
	}
}


/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: the list to check
 *
 * Return: 0 if no cycle found, 1 if cycle is found
 */
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow = list;

	if (list == NULL)
		return (0);

	fast = list->next;
	while (slow != NULL && fast != NULL && fast->next != NULL)
	{
		if (slow == fast)
			return (1);
		fast = fast->next->next;
		slow = slow->next;
	}

	return (0);
}
