cmake_minimum_required(VERSION 3.0.0)
project(libevent_test
  VERSION 0.0.0.1
  DESCRIPTION "libevent函数测试")

link_libraries(event)

add_executable(globals ${CMAKE_CURRENT_SOURCE_DIR}/globals.c)
add_executable(sock ${CMAKE_CURRENT_SOURCE_DIR}/sock.c)
add_executable(timer ${CMAKE_CURRENT_SOURCE_DIR}/timer.c)
add_executable(signal ${CMAKE_CURRENT_SOURCE_DIR}/signal.c)
add_executable(echo_server ${CMAKE_CURRENT_SOURCE_DIR}/echo_server.c)
add_executable(evhttp ${CMAKE_CURRENT_SOURCE_DIR}/evhttp.c)
