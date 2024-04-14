#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void file_histogram(char *file_name){
    FILE *file = fopen(file_name, "r");
    if (file == NULL) {
        printf("Error: file not found\n");
        return;
    }
    
    int freq[256] = {0};
    char c;
    while ((c = fgetc(file)) != EOF) {
        freq[c]++;
    }
    fclose(file);
    for (int i = 0; i < 256; i++) {
        if (freq[i] > 0) {
            printf("%c: ", i);
            for (int j = 0; j < freq[i]; j++) {
                printf("#");
            }
            printf(" %d\n", freq[i]);
        }
    }

}

int main(){
    char *file_name = "example.txt";
    file_histogram(file_name);
    return 0;
}