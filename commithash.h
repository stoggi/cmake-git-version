#ifndef COMMITHASH_H
#define COMMITHASH_H

#include <stdint.h>
#include <stdbool.h>

typedef struct {
    const uint32_t major;
    const uint32_t minor;
    const uint32_t patch;
    const uint32_t commits;
    const bool dirty;
    const char hash[8];
    const char string[24];
} tVersion;

extern const tVersion version;

#endif