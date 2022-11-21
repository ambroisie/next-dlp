#include <limits.h>
#include <stddef.h>

static unsigned char reverse_byte(unsigned char c) {
    unsigned char res = 0;
    for (size_t i = 0; i < CHAR_BIT; ++i) {
        res <<= 1;
        res |= c & 1;
        c >>= 1;
    }
    return res;
}

static void swap_bytes(unsigned char* lhs, unsigned char* rhs) {
    unsigned char tmp = *lhs;
    *lhs = *rhs;
    *rhs = tmp;
}

void reverse_bytes(unsigned char* buf, size_t n) {
    if (!buf || !n)
        return;

    // No need to worry about applying reverse_byte twice in the middle by
    // mistake if done in a preliminary pass
    for (size_t i = 0; i < n; ++i) {
        buf[i] = reverse_byte(buf[i]);
    }

    for (size_t i = 0; i < ((n + 1) / 2); ++i) {
        swap_bytes(&buf[i], &buf[n - 1 - i]);
    }
}
