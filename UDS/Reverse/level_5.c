// CALL IS LIKE THIS ===> uVar4 = FUN_00401c74(param_1 + 0x2070,0) //


ulong FUN_00401c74(undefined8 *param_1,int param_2)

{
  int iVar1;
  int i;
  ulong preKey;
  
  if ((0x26f < *(int *)(param_1 + 0x270)) || (*(int *)(param_1 + 0x270) < 0)) {
    if ((0x270 < *(int *)(param_1 + 0x270)) || (*(int *)(param_1 + 0x270) < 0)) {
      FUN_00401b5c(param_1,0x1105);
    }
    for (i = 0; i < 0xe3; i = i + 1) {
      param_1[i] = param_1[i + 0x18d] ^
                   (ulong)(((uint)param_1[i + 1] & 0x7fffffff | (uint)param_1[i] & 0x80000000) >> 1)
                   ^ *(ulong *)(&DAT_004ee0f0 + (ulong)((uint)param_1[i + 1] & 1) * 8);
    }
    for (; i < 0x26f; i = i + 1) {
      param_1[i] = param_1[i + -0xe3] ^
                   (ulong)(((uint)param_1[i + 1] & 0x7fffffff | (uint)param_1[i] & 0x80000000) >> 1)
                   ^ *(ulong *)(&DAT_004ee0f0 + (ulong)((uint)param_1[i + 1] & 1) * 8);
    }
    param_1[0x26f] =
         param_1[0x18c] ^
         (ulong)(((uint)*param_1 & 0x7fffffff | (uint)param_1[0x26f] & 0x80000000) >> 1) ^
         *(ulong *)(&DAT_004ee0f0 + (ulong)((uint)*param_1 & 1) * 8);
    *(undefined4 *)(param_1 + 0x270) = 0;
  }
  if (param_2 == 1) {
                    /* Seed update */
    preKey = param_1[*(int *)(param_1 + 0x270) + 1];
  }
  else { /* Seed update */
    iVar1 = *(int *)(param_1 + 0x270);
    *(int *)(param_1 + 0x270) = iVar1 + 1;
    preKey = param_1[iVar1];
  }
  preKey = preKey ^ preKey >> 0xb;
  preKey = preKey ^ (uint)(preKey << 7) & 0x9d2c5680;
  preKey = preKey ^ (uint)(preKey << 0xf) & 0xefc60000;
  return preKey ^ preKey >> 0x12;
}



void FUN_00401b5c(ulong *param_1,ulong param_2)

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



void UDS_27(long param_1)

if (bVar1 == 5) {
    uVar4 = FUN_00401c74(param_1 + 0x2070,0);
    generatedKeyKey[1] = (char)((uint)uVar4 >> 0x10);
    generatedKeyKey[0] = (char)((uint)uVar4 >> 0x18);
    generatedKeyKey[2] = (char)((uint)uVar4 >> 8);
    generatedKeyKey[3] = (char)uVar4;
    
    for (local_74 = 0; local_74 < 4; local_74 = local_74 + 1) {
      if (generatedKeyKey[local_74] != submitKey[local_74]) {
        uVar6 = 0x35;
      }
   }
      
}
      
