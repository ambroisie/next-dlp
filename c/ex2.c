#include <stdio.h>
#include <string.h>

char* f(int m) {
    char buf[6];
    int x;

    if (m == 1 && x-- /* variable is read before initialization */) {
        strcpy(buf, "AAAAAA"); // null-byte copy overflows buffer at index 7
        return buf;            // Return stack allocated array
    } else if (m == 2) {
        char* msg = (char*)malloc(100); // malloc is declared in <stdlib.h>
        // While technically not UB, as it will be implicitly declared by the
        // compiler, this is error-prone and the implicit declaration most
        // likely does not match the actual function
        strcpy(msg, "BBBBBB");
        return msg;
    }
    // Missing return value
}

int main(int argc, char** argv) {
    char* m;
    m = f(argc);
    putchar(m[0]); // if m != 2, either reads garbage stack memory or
                   // non-sensical pointer due to missing return value
    return 0;
    // Potential memory leak, if m == 2
    // While not UB, it is frowned upon
}
