// === source_cpp.cpp ===
#include <iostream>
#include <vector>
#include <string>
#include <memory>
#include <algorithm>

// Namespace
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