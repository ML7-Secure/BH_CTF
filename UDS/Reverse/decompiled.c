#include <stdio.h>
#include <string.h>
#include <stdint.h> 

#include <stdlib.h> // malloc

//#define ulong uint32_t
#define undefined4 uint32_t
#define uint uint32_t

#define undefined8 uint32_t
#define undefined uint32_t

#define ulong uint64_t

void FUN_00401b5c(ulong *param_1,ulong param_2){

  *param_1 = param_2 & 0xffffffff;
  *(undefined4 *)(param_1 + 0x270) = 1;
  while (*(int *)(param_1 + 0x270) < 0x270) {
    param_1[*(int *)(param_1 + 0x270)] =
         (ulong)(uint)((int)param_1[*(int *)(param_1 + 0x270) + -1] * 0x17b5);
    *(int *)(param_1 + 0x270) = *(int *)(param_1 + 0x270) + 1;
  }
  /*
  for (int i = 0x0; i <= 0x270; ++i) {
    printf("%lu,",param_1[i]);
  }
  printf("\n");
  */

  //return;
}

ulong FUN_00401c74(ulong *param_1,int param_2){
  int iVar1;
  int local_14;
  ulong local_10;


  // IS IT CORRECT ????
  //int DAT_004ee0f0[16] = {0x00, 0x00, 0x00, 0x00, 0x7F, 0xFF, 0xFF, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x03};
  
  if ((0x26f < *(int *)(param_1 + 0x270)) || (*(int *)(param_1 + 0x270) < 0)) {
    if ((0x270 < *(int *)(param_1 + 0x270)) || (*(int *)(param_1 + 0x270) < 0)) {
      FUN_00401b5c((ulong *)param_1,0x1105);
    }
    /*
    for (local_14 = 0; local_14 < 0xe3; local_14 = local_14 + 1) {
      param_1[local_14] =
           param_1[local_14 + 0x18d] ^
           (ulong)(((uint)param_1[local_14 + 1] & 0x7fffffff | (uint)param_1[local_14] & 0x80000000)
                  >> 1) ^ *(ulong *)(&DAT_004ee0f0 + (ulong)((uint)param_1[local_14 + 1] & 1) * 8);
    }
    */

    uint32_t constant_value = 0;
    int j = 0;
    
    for (j = 0; j < 0xe3; j = j + 1) {
      
      if (param_1[j + 1] & 1 == 0) {
        // If LSB is 0, use constant value 0x7FFFFFFF00000000
        constant_value = 0x7FFFFFFF;
      } else {
          // If LSB is 1, use constant value 0x00000000000003
          constant_value = 0x00000003;
      }
      param_1[j] = param_1[j + 0x18d] ^
                  (ulong)(((uint)param_1[j + 1] & 0x7fffffff | (uint)param_1[j] & 0x80000000) >> 1)
                  ^ constant_value;
    }

    /*
    for (; local_14 < 0x26f; local_14 = local_14 + 1) {
      param_1[local_14] =
           param_1[local_14 + -0xe3] ^
           (ulong)(((uint)param_1[local_14 + 1] & 0x7fffffff | (uint)param_1[local_14] & 0x80000000)
                  >> 1) ^ *(ulong *)(&DAT_004ee0f0 + (ulong)((uint)param_1[local_14 + 1] & 1) * 8);
    }
    */

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


    *(undefined4 *)(param_1 + 0x270) = 0;

  }
  if (param_2 == 1) {
    local_10 = param_1[*(int *)(param_1 + 0x270) + 1];
  }
  else {
    iVar1 = *(int *)(param_1 + 0x270);
    *(int *)(param_1 + 0x270) = iVar1 + 1;
    local_10 = param_1[iVar1];
  }
  local_10 = local_10 ^ local_10 >> 0xb;
  //printf("DEBUG local_10 : %lu\n", local_10);
  local_10 = local_10 ^ (uint)(local_10 << 7) & 0x9d2c5680;
  //printf("DEBUG local_10 : %lu\n", local_10);
  local_10 = local_10 ^ (uint)(local_10 << 0xf) & 0xefc60000;
  //printf("DEBUG local_10 : %lu\n", local_10);
  //printf("DEBUG local_10 : %lu\n", local_10 ^ local_10 >> 0x12);
  return local_10 ^ local_10 >> 0x12;
}




void UDS_27(ulong *param_1,undefined4 param_2,undefined8 *param_3)

{
  undefined4 uVar4; // DOUBT ulong -> uint32_t ??
  //int iVar5;
  //undefined8 uVar6;
  //long in_FS_OFFSET;
  //int local_7c;
  //int local_78;
  //int local_74;
  //char submitKey [4];

  //long local_20;  
  //local_20 = *(long *)(in_FS_OFFSET + 0x28);

  uVar4 = FUN_00401c74(param_1 + 0x2070,0);
  //printf("Seed : %08x\n", uVar4);
  //printf("Seed : %lu\n", uVar4);
  
  if (uVar4 == 0xFD50A60E){
    printf("************** YES **************");
    uVar4 = FUN_00401c74(param_1 + 0x2070,0);
    printf("Following value : %08x\n", uVar4); 
    return;
  }
  /*
  undefined generatedKeyKey [4];
  undefined seed [4];

  generatedKeyKey[1] = (char)((uint)uVar4 >> 0x10);
  generatedKeyKey[0] = (char)((uint)uVar4 >> 0x18);
  generatedKeyKey[2] = (char)((uint)uVar4 >> 8);
  generatedKeyKey[3] = (char)uVar4;
      
  for (int i = 0; i < 4; ++i) {
    seed[i] = generatedKeyKey[i];
    printf("Seed : %02x\n", seed[i]); 
  }
  */

  //uVar6 = (*(code *)param_3[3])(param_1,generatedKeyKey,4);
    
  //submitKey[0] = *(char *)param_3[1];
  //submitKey[1] = *(undefined *)(param_3[1] + 1);
  //submitKey[2] = *(undefined *)(param_3[1] + 2);
  //submitKey[3] = *(undefined *)(param_3[1] + 3);
  uVar4 = FUN_00401c74(param_1 + 0x2070,0);
  //printf("Key : %08x\n", uVar4); 
  //printf("Key : %lu\n", uVar4);

  if (uVar4 == 0xC91DFF42){
    printf("************** YES **************");
    uVar4 = FUN_00401c74(param_1 + 0x2070,0);
    printf("Following value : %08x\n", uVar4); 
    return;
  }

  /*
  generatedKeyKey[1] = (char)((uint)uVar4 >> 0x10);
  generatedKeyKey[0] = (char)((uint)uVar4 >> 0x18);
  generatedKeyKey[2] = (char)((uint)uVar4 >> 8);
  generatedKeyKey[3] = (char)uVar4;
  
  for (int i = 0; i < 4; ++i) {
    printf("Key : %02x\n", generatedKeyKey[i]); 
  }
  */
}

void main(){
  ulong *param_1 = (ulong *)malloc(0x22e0 * sizeof(ulong));
  //memset(param_1, 0, 0x22e0 * sizeof(ulong));
  *(int *)(param_1 + 0x2070 + 0x270) = 0x271;
  for (int i = 0; i < 1000000000 /*4294967295 == 2^32 -1 */; ++i){
    UDS_27(param_1,0,NULL);
  }

  free(param_1);
}
