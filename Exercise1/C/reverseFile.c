#include <stdio.h>
#include <stdlib.h>
#include <string.h>


void reverse_file( char *input_file_name, char *output_file_name){
    FILE * input_file = fopen(input_file_name, "r");
    if (input_file == NULL) {
        printf("Error: file not found\n");
        return;
    }
    FILE * output_file = fopen(output_file_name, "w");
    if (output_file == NULL) {
        printf("Error: file not found\n");
        return;
    }
    fseek(input_file, 0, SEEK_END);
    long size = ftell(input_file);
    char c;
    for (long i = size - 1; i >= 0; i--) {
        fseek(input_file, i, SEEK_SET);
        c = fgetc(input_file);
        fputc(c, output_file);
    }
    fclose(input_file);
    fclose(output_file);
    return;
}

int main(){
    char *input_file_name = "example.txt";
    char *output_file_name = "example_reverse.txt";
    reverse_file(input_file_name, output_file_name);
    return 0;
}
