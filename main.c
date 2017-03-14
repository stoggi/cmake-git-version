#include <stdio.h>
#include "commithash.h"

int main(void) {
    printf("The current version: %s\n", version.string);
    printf("Major version: %d\n", version.major);
    printf("Minor version: %d\n", version.minor);
    printf("Patch version: %d\n", version.patch);
    printf("Commits since last tag: %d\n", version.commits);
    printf("Latest commit hash: %s\n", version.hash);
    if (version.dirty) {
        printf("The working tree was: dirty\n");
    } else {
        printf("The working tree was: clean\n");
    }
    return 0;
}
