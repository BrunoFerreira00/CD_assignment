#include <stdio.h>

void count_bits(int val){
    int mask = 1;
    int countOnes = 0;
    int countZeros = 0;
    while(val != 0){
        if (val & mask){
            countOnes++;
        } else {
            countZeros++;
        }
        val = val >> 1;
    }
    printf("Number of ones: %d\n", countOnes);
    printf("Number of zeros: %d\n", countZeros);
}

int main(){
    int val = 5;
    count_bits(val);
    return 0;
}