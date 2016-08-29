#include <stdio.h>
#include "commithash.h"

int main(void) {
    printf("The current version is %s", COMMIT_HASH);
}