cmake_minimum_required(VERSION 3.0)
add_executable(main main.cpp mylib.cpp)
find_package(GTest REQUIRED)
target_link_libraries(main gtest ${GTEST_LIBRARIES} pthread)
