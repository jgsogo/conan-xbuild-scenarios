
set(CMAKE_CXX_COMPILER_WORKS 1)
set(CMAKE_CXX_ABI_COMPILED 1)

cmake_minimum_required(VERSION 3.10)
project(android LANGUAGES CXX)


include(GenerateExportHeader)
include(${CMAKE_CURRENT_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()
find_package(zlib REQUIRED)

# We have a library
file(WRITE ${CMAKE_CURRENT_SOURCE_DIR}/android_ndk.h "#pragma once\nconst char* const android_ndk_MESSAGE=\"${MESSAGE}\";")
add_library(android_ndk android_ndk/lib.cpp android_ndk/lib.h)
generate_export_header(android_ndk)
target_include_directories(android_ndk
    PUBLIC
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}>)
target_link_libraries(android_ndk PUBLIC zlib::zlib )
set_target_properties(android_ndk PROPERTIES OUTPUT_NAME android_ndk)


# We have a executable
add_executable(android_ndk_exe android_ndk/main.cpp)
target_link_libraries(android_ndk_exe PUBLIC android_ndk )
set_target_properties(android_ndk PROPERTIES OUTPUT_NAME android_ndk_exe)
