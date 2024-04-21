#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int file_symbol_freq( char *file_name, char symbol ){
    FILE *file = fopen(file_name, "r");
    if (file == NULL) {
        return -1;
    }
    int count = 0;
    int total = 0;
    char c;
    while ((c = fgetc(file)) != EOF) {
        if (c == symbol) {
            count++;
        }
        total++;
    }
    if(count == 0){
        fclose(file);
        return -1;
    }
    fclose(file);
    printf("Total symbols in file %s is %d\n", file_name, total);
    return count;
}

int main(){
    char *file_name = "example.txt";
    char symbol = 'j';
    int freq = file_symbol_freq(file_name, symbol);
    if (freq == -1) {
        printf("Error: file not found or symbol not found\n");
    } else {
        printf("Frequency of symbol %c in file %s is %d\n", symbol, file_name, freq);
    }
    return 0;
}