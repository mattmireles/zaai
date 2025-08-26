// === source_header.h ===
/**
 * ZAAI Environment Test - C/C++ Header File
 * 
 * This C/C++ header file serves as a comprehensive test artifact for validating
 * the ZAAI system's ability to process, parse, and understand C/C++ header
 * files with declarations, definitions, and preprocessor directives. It
 * demonstrates header organization patterns while following AI-first
 * documentation principles established in the ZAAI codebase.
 * 
 * Architecture Purpose:
 * This file is referenced by the test domain (domains/test/test.yaml) as
 * part of the environment validation benchmark. It validates the system's
 * capability to handle C/C++ header files with complex preprocessor usage,
 * type definitions, and function declarations in the workspace environment.
 * 
 * Cross-file Dependencies:
 * - Referenced by: domains/test/test.yaml (env benchmark)
 * - Used by: Environment test functions that validate header file processing
 * - Part of: Multi-language source code validation test suite
 * 
 * Header File Features Demonstrated:
 * - Include guards for multiple inclusion prevention
 * - Preprocessor macros and conditional compilation
 * - Type definitions (typedef, struct, enum)
 * - Function prototypes and extern declarations
 * - Inline function definitions
 * - Constant definitions and symbolic names
 * - Memory safety patterns and utilities
 * 
 * AI Comprehension Notes:
 * This file contains representative C/C++ header patterns that demonstrate
 * interface design, API organization, and preprocessor usage. An AI system
 * should be able to understand header/source file separation, declaration
 * vs definition concepts, and preprocessor metaprogramming patterns.
 * 
 * Compilation Requirements:
 * This header is designed to be compatible with both C99+ and C++11+
 * compilers, demonstrating cross-language header design practices.
 */

#ifndef SOURCE_HEADER_H
#define SOURCE_HEADER_H

#include <stddef.h>
#include <stdbool.h>

// Constants
#define MAX_BUFFER_SIZE 1024
#define PI 3.14159265359
#define VERSION_MAJOR 1
#define VERSION_MINOR 0

// Type definitions
typedef struct {
    int x;
    int y;
} Point;

typedef struct {
    Point top_left;
    Point bottom_right;
} Rectangle;

typedef enum {
    STATUS_SUCCESS = 0,
    STATUS_ERROR = -1,
    STATUS_INVALID_INPUT = -2,
    STATUS_MEMORY_ERROR = -3
} Status;

// Function prototypes
extern int initialize_system(void);
extern void cleanup_system(void);
extern Status process_data(const char* input, char* output, size_t output_size);

// Math utilities
extern double calculate_distance(Point p1, Point p2);
extern double calculate_area(Rectangle rect);
extern bool point_in_rectangle(Point point, Rectangle rect);

// String utilities
extern size_t safe_string_copy(char* dest, const char* src, size_t dest_size);
extern bool string_contains(const char* haystack, const char* needle);
extern void string_to_upper(char* str);

// Memory utilities
extern void* safe_malloc(size_t size);
extern void safe_free(void** ptr);

// Inline functions (C99+)
static inline int min(int a, int b) {
    return (a < b) ? a : b;
}

static inline int max(int a, int b) {
    return (a > b) ? a : b;
}

static inline bool is_valid_coordinate(int x, int y) {
    return (x >= 0 && y >= 0 && x < MAX_BUFFER_SIZE && y < MAX_BUFFER_SIZE);
}

// Macros
#define ARRAY_SIZE(arr) (sizeof(arr) / sizeof((arr)[0]))
#define CLAMP(value, min_val, max_val) \
    ((value) < (min_val) ? (min_val) : ((value) > (max_val) ? (max_val) : (value)))

// Conditional compilation
#ifdef DEBUG
    #define DEBUG_PRINT(fmt, ...) printf("DEBUG: " fmt "\n", ##__VA_ARGS__)
#else
    #define DEBUG_PRINT(fmt, ...)
#endif

#endif // SOURCE_HEADER_H