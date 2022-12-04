#include "lists.h"

/**
* check_cycle - Checks if the singly linked list has a cycle in it
* @list: The singly linked list
* Return: 1 if there is a cycle, 0 if not
*/
int check_cycle(listint_t *list)
{
listint_t *fast = list;
listint_t *slow = list;
if (!list)
return (0);
while (slow && fast && fast->next)
{
slow = slow->next;
fast = fast->next->next;
if (slow == fast)
return (1);
}
return (0);
}
