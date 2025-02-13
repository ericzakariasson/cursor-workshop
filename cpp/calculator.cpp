#include "calculator.h"
#include <sstream>
#include <stdexcept>

double Calculator::evaluate(const std::string& expr) {
    std::istringstream iss(expr);
    double num1, num2;
    char op;

    iss >> num1 >> op >> num2;
    if (iss.fail()) {
        throw std::invalid_argument("Invalid input format");
    }

    switch (op) {
        case '+': result = num1 + num2; break;
        case '-': result = num1 - num2; break;
        case '*': result = num1 * num2; break;
        case '/':
            if (num2 == 0) throw std::runtime_error("Division by zero");
            result = num1 / num2;
            break;
        default:
            throw std::invalid_argument("Invalid operator");
    }
    return result;
}

void Calculator::clear() {
    result = 0;
} 