
set(CMAKE_CXX_COMPILER_WORKS 1)
set(CMAKE_CXX_ABI_COMPILED 1)

cmake_minimum_required(VERSION 3.10)
project(protobuf LANGUAGES CXX)


include(GenerateExportHeader)
include(${CMAKE_CURRENT_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()
find_package(zlib REQUIRED)

# We have a library
file(WRITE ${CMAKE_CURRENT_SOURCE_DIR}/protobuf.h "#pragma once\nconst char* const protobuf_MESSAGE=\"${MESSAGE}\";")
add_library(protobuf protobuf/lib.cpp protobuf/lib.h)
generate_export_header(protobuf)
target_include_directories(protobuf
    PUBLIC
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}>)
target_link_libraries(protobuf PUBLIC zlib::zlib )
set_target_properties(protobuf PROPERTIES OUTPUT_NAME protobuf)


# We have a executable
add_executable(protoc protobuf/main.cpp)
target_link_libraries(protoc PUBLIC protobuf )
set_target_properties(protoc PROPERTIES OUTPUT_NAME protoc)
