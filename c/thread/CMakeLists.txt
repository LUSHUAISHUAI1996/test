cmake_minimum_required(VERSION 3.0.0)
project(thread_test
  VERSION 0.0.0.1
  DESCRIPTION "线程函数测试")

link_libraries(pthread)

add_executable(thread_create ${CMAKE_CURRENT_SOURCE_DIR}/thread_create.c)
add_executable(main_thread_exit ${CMAKE_CURRENT_SOURCE_DIR}/main_thread_exit.c)
add_executable(main_thread_canceled ${CMAKE_CURRENT_SOURCE_DIR}/main_thread_canceled.c)
add_executable(thread_race ${CMAKE_CURRENT_SOURCE_DIR}/thread_race.c)
add_executable(mutex ${CMAKE_CURRENT_SOURCE_DIR}/mutex.c)
add_executable(rwlock ${CMAKE_CURRENT_SOURCE_DIR}/rwlock.c)
add_executable(cond ${CMAKE_CURRENT_SOURCE_DIR}/cond.c)
add_executable(barrier ${CMAKE_CURRENT_SOURCE_DIR}/barrier.c)
