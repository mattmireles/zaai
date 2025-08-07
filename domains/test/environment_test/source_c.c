// === source_c.c ===
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Function declarations
int add_numbers(int a, int b);
void print_greeting(const char* name);
int factorial(int n);

// Global variable
int global_counter = 0;

/**
 * Main function - entry point of the program
 */
int main(int argc, char *argv[]) {
    printf("C Test File - Basic Operations\n");
    printf("==============================\n");
    
    // Test arithmetic
    int result = add_numbers(5, 3);
    printf("5 + 3 = %d\n", result);
    
    // Test string operations
    print_greeting("World");
    
    // Test recursive function
    int fact = factorial(5);
    printf("Factorial of 5 = %d\n", fact);
    
    // Test array operations
    int numbers[] = {1, 2, 3, 4, 5};
    int sum = 0;
    for (int i = 0; i < 5; i++) {
        sum += numbers[i];
    }
    printf("Sum of array: %d\n", sum);
    
    return 0;
}

/**
 * Add two integers
 */
int add_numbers(int a, int b) {
    global_counter++;
    return a + b;
}

/**
 * Print a greeting message
 */
void print_greeting(const char* name) {
    printf("Hello, %s!\n", name);
}

/**
 * Calculate factorial recursively
 */
int factorial(int n) {
    if (n <= 1) {
        return 1;
    }
    return n * factorial(n - 1);
}