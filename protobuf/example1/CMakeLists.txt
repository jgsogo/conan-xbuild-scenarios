
set(CMAKE_CXX_COMPILER_WORKS 1)
set(CMAKE_CXX_ABI_COMPILED 1)

cmake_minimum_required(VERSION 3.10)
project(example1 LANGUAGES CXX)


include(${CMAKE_CURRENT_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()
find_package(protobuf REQUIRED)


# We have a executable
add_executable(example main.cpp)
target_link_libraries(example PUBLIC protobuf::protobuf)
set_target_properties(example PROPERTIES OUTPUT_NAME example01)
