#include <stdio.h>
#include "commithash.h"

int main(void) {
    printf("The current version is %s\n", COMMIT_HASH);
    return 0;
}
