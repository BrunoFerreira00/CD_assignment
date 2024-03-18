#include <stdio.h>
#include <stdlib.h>

void print_fibonacci(int n){
        long long *fib = (long long *)malloc((n + 1) * sizeof(long long));
        for(int i = 0 ; i < n ; i ++){
        if (i == 0){
            fib[i] = 0;
            printf("%d\n", fib[i]);
        } else if (i == 1 || i == 2){
            fib[i] = 1;
            printf("%d\n", fib[i]);
        } else {
            fib[i] = fib[i-1] + fib[i-2];
            printf("%d\n", fib[i]);
        }
    }
    free(fib);
}

int main(){
    int n = 20;
    print_fibonacci(n);
    return 0;
}