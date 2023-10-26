#include <stdio.h>
#include <string.h>
#include <stdint.h> 

void main(void){
    uint32_t DAT_004ee0f0[8] = {0x7FFFFFFF, 0x03, 0x112000, 0x112004, 0x56161561, 0x112003, 0x112002, 0x11201};

    for (int i = 0; i < 8; ++i){
      if (DAT_004ee0f0[i] == 0x56161561){
        printf("Yes.\n");
      }
      //printf("No.\n");
    }

}