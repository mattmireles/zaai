// === source_c.c ===
/**
 * ZAAI Environment Test - C Language Source File
 * 
 * This C source file serves as a comprehensive test artifact for validating
 * the ZAAI system's ability to process, parse, and understand C language
 * source code. It demonstrates fundamental C programming concepts and
 * patterns while following AI-first documentation principles.
 * 
 * Architecture Purpose:
 * This file is referenced by the test domain (domains/test/test.yaml) as
 * part of the environment validation benchmark. It tests the system's
 * capability to handle C source files in the workspace environment.
 * 
 * Cross-file Dependencies:
 * - Referenced by: domains/test/test.yaml (env benchmark)
 * - Used by: Environment test functions that validate C file processing
 * - Part of: Multi-language source code validation test suite
 * 
 * C Language Features Demonstrated:
 * - Standard library includes and system headers
 * - Function declarations and implementations
 * - Global variable management and state
 * - Recursive algorithm implementation (factorial)
 * - Array processing and iteration patterns
 * - String manipulation and printf formatting
 * - Memory-safe programming practices
 * 
 * AI Comprehension Notes:
 * This file contains representative C code that an AI system should be
 * able to analyze, understand, and potentially modify. It includes
 * common C idioms, memory management patterns, and structured
 * programming approaches typical in C development.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Constants - Following AI-first documentation philosophy
#define MAX_NAME_LENGTH 256
#define ARRAY_SIZE 5
#define SUCCESS_EXIT_CODE 0

// Function declarations with comprehensive documentation
/**
 * Add two integer values and increment global counter
 * @param a First integer operand
 * @param b Second integer operand
 * @return Sum of a and b
 */
int add_numbers(int a, int b);

/**
 * Print a personalized greeting message
 * @param name Null-terminated string containing the name to greet
 */
void print_greeting(const char* name);

/**
 * Calculate factorial of a number recursively
 * @param n Non-negative integer to calculate factorial for
 * @return Factorial of n, or 1 if n <= 1
 */
int factorial(int n);

// Global variable with explicit purpose documentation
/**
 * Global counter tracking the number of arithmetic operations performed.
 * This demonstrates global state management in C programs and provides
 * a simple mechanism for operation counting across function calls.
 */
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
    
    return SUCCESS_EXIT_CODE;
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