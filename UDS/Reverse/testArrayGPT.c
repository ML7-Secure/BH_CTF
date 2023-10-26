#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

int main(void) {
    uint32_t DAT_004ee0f0[16] = {0x7F, 0xFF, 0xFF, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x00, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00};
    uint32_t tmp = 56161561;

    printf("Value at index 2: %08x\n", DAT_004ee0f0[2]);

    uint32_t index = tmp & 1;  // Get the least significant bit of tmp
    uint32_t value = DAT_004ee0f0[index + 8];  // Retrieve value from index 8 or 9 based on LSB

    printf("Retrieved value: %08x\n", value);

    return 0;
}
