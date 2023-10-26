#include <stdio.h>
#include <string.h>
#include <stdint.h> 

const uint32_t a = 1103515245;
const uint32_t c = 12345;
const uint32_t m = 2147483647;
uint32_t seed = 1337;

const uint32_t STATE[4] = {0x1e48add6, 0xaaa7550c, 0x18df53bf, 0xe6af1116};

uint32_t gen_random(void) {
  seed = (uint32_t)(((uint32_t)a * (uint32_t)seed + (uint32_t)c) % m);
  printf("seed : %u\n", (uint32_t)a * (uint32_t)seed + (uint32_t)c);
  printf("seed : %u\n", seed);
  return (uint32_t)seed;
}


void main(void){
    gen_random();gen_random(); // 0
    gen_random();gen_random(); // 1
    gen_random();gen_random(); // 2
    gen_random();gen_random(); // 3
}


