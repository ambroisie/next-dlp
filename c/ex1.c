#include <stdbool.h>
#include <stddef.h>

struct node_t {
    unsigned v;
    struct node_t* next;
};

struct node_t* even_nodes(struct node_t** list) {
    struct node_t* res = NULL;

    while (true) {
        struct node_t* next = (*list)->next;

        if ((*list)->v % 2 == 0) {
            // Pop element from the list, add it to head of the other
            (*list)->next = res;
            res = *list;
        }

        *list = next;
    }

    // NOTE: this is in reverse order from the input list
    return res;
}
