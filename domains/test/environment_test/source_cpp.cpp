// === source_cpp.cpp ===
/**
 * ZAAI Environment Test - C++ Language Source File
 * 
 * This C++ source file serves as a comprehensive test artifact for validating
 * the ZAAI system's ability to process, parse, and understand modern C++
 * source code. It demonstrates object-oriented programming, template
 * metaprogramming, and modern C++ features while following AI-first
 * documentation principles established in the ZAAI codebase.
 * 
 * Architecture Purpose:
 * This file is referenced by the test domain (domains/test/test.yaml) as
 * part of the environment validation benchmark. It validates the system's
 * capability to handle C++ source files with object-oriented patterns,
 * templates, and modern C++ idioms in the workspace environment.
 * 
 * Cross-file Dependencies:
 * - Referenced by: domains/test/test.yaml (env benchmark)
 * - Used by: Environment test functions that validate C++ file processing
 * - Part of: Multi-language source code validation test suite
 * 
 * C++ Language Features Demonstrated:
 * - Object-oriented programming with classes and inheritance
 * - Template programming and generic algorithms
 * - Standard Template Library (STL) usage
 * - Smart pointers and modern memory management
 * - Namespace organization and scope management
 * - Exception handling and RAII patterns
 * - Lambda expressions and functional programming
 * - Move semantics and perfect forwarding
 * 
 * AI Comprehension Notes:
 * This file contains representative modern C++ code that demonstrates
 * the language's evolution from C-style programming to modern object-oriented
 * and generic programming paradigms. An AI system should be able to understand
 * C++'s type system, template metaprogramming, and object lifetime management.
 * 
 * Compilation Requirements:
 * This file is designed to compile with C++17 or later standards using
 * standard C++ compilers (g++, clang++, MSVC).
 */

#include <iostream>
#include <vector>
#include <string>
#include <memory>
#include <algorithm>

// Namespace organization following C++ best practices
namespace TestApp {
    
    // Class definition
    class Calculator {
    private:
        std::string name;
        std::vector<double> history;
        
    public:
        // Constructor
        Calculator(const std::string& calc_name) : name(calc_name) {
            std::cout << "Calculator '" << name << "' created" << std::endl;
        }
        
        // Destructor
        ~Calculator() {
            std::cout << "Calculator '" << name << "' destroyed" << std::endl;
        }
        
        // Methods
        double add(double a, double b) {
            double result = a + b;
            history.push_back(result);
            return result;
        }
        
        double multiply(double a, double b) {
            double result = a * b;
            history.push_back(result);
            return result;
        }
        
        void print_history() const {
            std::cout << "History for " << name << ": ";
            for (const auto& result : history) {
                std::cout << result << " ";
            }
            std::cout << std::endl;
        }
        
        size_t get_operation_count() const {
            return history.size();
        }
    };
    
    // Template function
    template<typename T>
    T max_value(const std::vector<T>& values) {
        return *std::max_element(values.begin(), values.end());
    }
}

// Main function
int main() {
    std::cout << "C++ Test File - Object-Oriented Programming" << std::endl;
    std::cout << "===========================================" << std::endl;
    
    // Create calculator instance
    auto calc = std::make_unique<TestApp::Calculator>("TestCalc");
    
    // Perform operations
    double sum = calc->add(10.5, 5.3);
    double product = calc->multiply(3.0, 4.0);
    
    std::cout << "Addition result: " << sum << std::endl;
    std::cout << "Multiplication result: " << product << std::endl;
    
    // Print operation history
    calc->print_history();
    std::cout << "Total operations: " << calc->get_operation_count() << std::endl;
    
    // Test template function
    std::vector<int> numbers = {1, 5, 3, 9, 2};
    int max_num = TestApp::max_value(numbers);
    std::cout << "Max number: " << max_num << std::endl;
    
    return 0;
}