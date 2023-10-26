#include <stdio.h>
#include <string.h>
#include <stdint.h> 
#include <stdlib.h>

#define ulong uint64_t
#define uint uint32_t

void main(void){ // TO TRY ONE BY ONE !
    ulong DAT_004ee0f0[16] = {0xFF, 0xFF, 0xFF, 0x7F, 0x00, 0x00, 0x00, 0x00, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00};
    
    //ulong DAT_004ee0f0[16] = {0x7F, 0xFF, 0xFF, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00};

    //ulong DAT_004ee0f0[16] = {0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x03, 0x7F, 0xFF, 0xFF, 0xFF, 0x00, 0x00, 0x00, 0x00};

    //ulong DAT_004ee0f0[16] = {0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x03, 0xFF, 0xFF, 0xFF, 0x7F, 0x00, 0x00, 0x00, 0x00};
    
    //ulong DAT_004ee0f0[16] = {0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x03, 0x00, 0x00, 0x00, 0x00, 0xFF, 0xFF, 0xFF, 0x7F};


    //uint32_t DAT_004ee0f0[2] = {0x7FFFFFFF, 0x03};
    
    uint32_t tmp = 56161561;

    //printf("%lu\n", (ulong *)(&DAT_004ee0f0));
    //printf("%lu\n", (ulong *)(&DAT_004ee0f0 + (ulong)((uint)tmp & 1) * 8));

    printf("%lu\n", ((uint)tmp & 1) * 8);
    printf("%lu\n", *(ulong *)(&DAT_004ee0f0 + (ulong)((uint)tmp & 1) * 8));
    printf("%08x\n", *(ulong *)(&DAT_004ee0f0 + (ulong)((uint)tmp & 1) * 8));
    exit(1);

    printf("LSB : %d\n",(uint32_t)tmp & 1);
    
    printf("%u\n", DAT_004ee0f0[tmp & 1]);
    printf("%08x\n", DAT_004ee0f0[tmp & 1]);
    //printf("%08x\n", *(uint32_t *)(&DAT_004ee0f0 + (tmp & 1)));

    if (tmp & 1 == 0) {
        // If LSB of *param_1 is 0, use constant value 0x7FFFFFFF00000000
          printf("%u\n", DAT_004ee0f0[tmp & 1]);
    } else {
        // If LSB of *param_1 is 1, use constant value 0x0000000000000003
          printf("%u\n", DAT_004ee0f0[tmp & 1]);
    }

}