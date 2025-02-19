#include <gtest/gtest.h>
#include "calculator.h"

TEST(CalculatorTest, BasicArithmetic) {
    Calculator calc;
    
    EXPECT_DOUBLE_EQ(calc.evaluate("2 + 3"), 5.0);
    EXPECT_DOUBLE_EQ(calc.evaluate("4 - 1"), 3.0);
    EXPECT_DOUBLE_EQ(calc.evaluate("3 * 4"), 12.0);
    EXPECT_DOUBLE_EQ(calc.evaluate("8 / 2"), 4.0);
}

TEST(CalculatorTest, DecimalOperations) {
    Calculator calc;
    
    EXPECT_DOUBLE_EQ(calc.evaluate("2.5 + 1.5"), 4.0);
    EXPECT_DOUBLE_EQ(calc.evaluate("3.3 * 2"), 6.6);
}

TEST(CalculatorTest, NegativeNumbers) {
    Calculator calc;
    
    EXPECT_DOUBLE_EQ(calc.evaluate("-5 + 3"), -2.0);
    EXPECT_DOUBLE_EQ(calc.evaluate("2 * -4"), -8.0);
}

TEST(CalculatorTest, Clear) {
    Calculator calc;
    
    EXPECT_DOUBLE_EQ(calc.evaluate("5 + 3"), 8.0);
    calc.clear();
    EXPECT_DOUBLE_EQ(calc.evaluate("2 + 2"), 4.0);
}

int main(int argc, char **argv) {
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
} 