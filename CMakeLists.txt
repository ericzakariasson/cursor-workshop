cmake_minimum_required(VERSION 3.10)

project(CursorWorkshop)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Google Test
include(FetchContent)
FetchContent_Declare(
  googletest
  URL https://github.com/google/googletest/archive/refs/tags/v1.14.0.zip
)
FetchContent_MakeAvailable(googletest)

add_library(calculator cpp/calculator.cpp)
add_executable(main cpp/main.cpp)
target_link_libraries(main calculator)

add_executable(calculator_test cpp/calculator_test.cpp)
target_link_libraries(calculator_test calculator GTest::gtest_main) 