#pragma once
#include <string>

class Calculator {
public:
    double evaluate(const std::string& expr);
    void clear();
private:
    double result = 0;
}; 