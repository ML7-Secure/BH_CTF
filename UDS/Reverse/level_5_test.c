#include <stdio.h>
#include <string.h>
#include <stdint.h> 

#include <stdlib.h> // malloc

#define ulong uint32_t
#define undefined4 uint32_t
#define uint uint32_t

void INIT_STATE(ulong *param_1,ulong param_2)

{
  *param_1 = param_2 & 0xffffffff;
  *(undefined4 *)(param_1 + 0x270) = 1;
  while (*(int *)(param_1 + 0x270) < 0x270) {
    param_1[*(int *)(param_1 + 0x270)] =
         (ulong)(uint)((int)param_1[*(int *)(param_1 + 0x270) + -1] * 0x17b5);
    *(int *)(param_1 + 0x270) = *(int *)(param_1 + 0x270) + 1;
  }
  return;
}

#define undefined8 uint32_t
ulong RNG(undefined8 *param_1,int param_2)

{
  int iVar1;
  int j;
  ulong nextKey;
  
  uint32_t constant_value = 0;

  //printf("DEBUG *(int *)(param_1 + 0x270) : %u\n", *(int *)(param_1 + 0x270));

  //if ((0x26f < *(int *)(param_1 + 0x270)) || (*(int *)(param_1 + 0x270) < 0)) {
    //if ((0x270 < *(int *)(param_1 + 0x270)) || (*(int *)(param_1 + 0x270) < 0)) {
      //printf("DEBUG *(int *)(param_1 + 0x270) : %u\n", *(int *)(param_1 + 0x270));
      //INIT_STATE(param_1,0x1105);
      /*
      for (int ii = 0; ii < 0x272; ii = ii + 1) {
        printf("param_1[%d] : %u\n", ii, param_1[ii]);
      }*/

    //}

    /*
    for (j = 0; j < 0xe3; j = j + 1) {
      param_1[j] = param_1[j + 0x18d] ^
                   (ulong)(((uint)param_1[j + 1] & 0x7fffffff | (uint)param_1[j] & 0x80000000) >> 1)
                   ^ *(ulong *)(&DAT_004ee0f0 + (ulong)((uint)param_1[j + 1] & 1) * 8);
    }*/

    for (j = 0; j < 0xe3; j = j + 1) {
      
      if (param_1[j + 1] & 1 == 0) {
        // If LSB is 0, use constant value 0x7FFFFFFF00000000
        constant_value = 0x7FFFFFFF;
      } else {
          // If LSB is 1, use constant value 0x0003000000000000
          constant_value = 0x00000003;
      }
      param_1[j] = param_1[j + 0x18d] ^
                  (ulong)(((uint)param_1[j + 1] & 0x7fffffff | (uint)param_1[j] & 0x80000000) >> 1)
                  ^ constant_value;
    }

    /*
    for (; j < 0x26f; j = j + 1) {
      param_1[j] = param_1[j + -0xe3] ^
                   (ulong)(((uint)param_1[j + 1] & 0x7fffffff | (uint)param_1[j] & 0x80000000) >> 1)
                   ^ *(ulong *)(&DAT_004ee0f0 + (ulong)((uint)param_1[j + 1] & 1) * 8);
    }*/

    for (; j < 0x26f; j = j + 1) {
    
      if (param_1[j + 1] & 1 == 0) {
          // If LSB of param_1[j + 1] is 0, use constant value 0x7FFFFFFF00000000
          constant_value = 0x7FFFFFFF;
      } else {
          // If LSB of param_1[j + 1] is 1, use constant value 0x0000000000000003
          constant_value = 0x00000003;
      }

      param_1[j] = param_1[j + -0xe3] ^
                  (ulong)(((uint)param_1[j + 1] & 0x7fffffff | (uint)param_1[j] & 0x80000000) >> 1)
                  ^ constant_value;
    }

    /*
    param_1[0x26f] =
         param_1[0x18c] ^
         (ulong)(((uint)*param_1 & 0x7fffffff | (uint)param_1[0x26f] & 0x80000000) >> 1) ^
         *(ulong *)(&DAT_004ee0f0 + (ulong)((uint)*param_1 & 1) * 8);
    */

    if (*param_1 & 1 == 0) {
        // If LSB of *param_1 is 0, use constant value 0x7FFFFFFF00000000
          constant_value = 0x7FFFFFFF;
    } else {
        // If LSB of *param_1 is 1, use constant value 0x0000000000000003
          constant_value = 0x00000003;
    }

    param_1[0x26f] = param_1[0x18c] ^
                    (ulong)(((uint)*param_1 & 0x7fffffff | (uint)param_1[0x26f] & 0x80000000) >> 1)
                    ^ constant_value;
    
    //printf("DEBUG param_1[0x26f] : %u\n", param_1[0x26f]);

    *(undefined4 *)(param_1 + 0x270) = 0;
  //}

  if (param_2 == 1) {
    nextKey = param_1[*(int *)(param_1 + 0x270) + 1];
  }

  else {
    iVar1 = *(int *)(param_1 + 0x270);
    *(int *)(param_1 + 0x270) = iVar1 + 1;
    nextKey = param_1[iVar1];
  }
  //printf("DEBUG nextKey : %u\n", nextKey);
  nextKey = nextKey ^ nextKey >> 0xb;
  nextKey = nextKey ^ (uint)(nextKey << 7) & 0x9d2c5680;
  nextKey = nextKey ^ (uint)(nextKey << 0xf) & 0xefc60000;
  //printf("DEBUG nextKey : %u\n", nextKey);
  return nextKey ^ nextKey >> 0x12;
}

#define undefined uint32_t
void main(void){
  ulong preKey;
  undefined genKey[4];
  int ii;

  // Allocate memory for param_1
  ulong *param_1 = (ulong *)malloc(0x271 * sizeof(ulong));
  
  INIT_STATE(param_1,0x1105);
  /*
  for (ii = 0; ii <= 0x270; ii = ii + 1) {
    printf("%u, ", param_1[ii]);
  }
  printf("\n");
  */

  for (int kk = 0; kk < 4294967295 ; ++kk){  
    //preKey = RNG(param_1 + 0x2070,0);
    preKey = RNG(param_1,0);
    //printf("%08x\n", preKey);

    uint32_t res = 0xA411AC0E;
    if (preKey == res){
      printf("Last seed found");
      printf("%08x\n", preKey);

      preKey = RNG(param_1,0);
      printf("Following seed :");
      printf("%08x\n", preKey);
    }
    /*
    genKey[0] = (char)((uint)preKey >> 0x18);
    genKey[1] = (char)((uint)preKey >> 0x10);
    genKey[2] = (char)(uint)((preKey >> 8));
    genKey[3] = (char)preKey;
    
    printf("\n");
    for (ii = 0; ii < 4; ii = ii + 1) {
      //printf("%u/", (char)genKey[ii]);
      printf("%02x", (char)genKey[ii]);
    }
    printf("\n");
    */
  }
  free(param_1);
}
