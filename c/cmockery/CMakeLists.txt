cmake_minimum_required(VERSION 3.0.0)
project(cmockery_test
  VERSION 0.0.0.1
  DESCRIPTION "cmockery测试")

link_libraries(cmockery)

add_executable(overview ${CMAKE_CURRENT_SOURCE_DIR}/overview.c)
add_executable(assert ${CMAKE_CURRENT_SOURCE_DIR}/assert.c)
add_executable(expect_assert_failure ${CMAKE_CURRENT_SOURCE_DIR}/expect_assert_failure.c)
add_executable(assert_macro ${CMAKE_CURRENT_SOURCE_DIR}/assert_macro.c)
add_executable(mock_func ${CMAKE_CURRENT_SOURCE_DIR}/mock_func.c)
add_executable(mock_func_param ${CMAKE_CURRENT_SOURCE_DIR}/mock_func_param.c)
add_executable(setup_teardown ${CMAKE_CURRENT_SOURCE_DIR}/setup_teardown.c)
