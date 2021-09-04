# Documentation: https://cmake.org/cmake/help/v3.16/guide/tutorial/index.html

cmake_minimum_required(VERSION 3.10)
project(test_libtorch)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++14 -Wall")

# specify the C++ standard
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED True)

set(CMAKE_PREFIX_PATH "/home/mhy/libtorch") # version 1.5.1+cu101
set(Torch_DIR libtorch/share/cmake/Torch)
find_package(Torch REQUIRED)

# file to be executed
add_executable(test_libtorch test_libtorch.cpp)

target_link_libraries(test_libtorch ${TORCH_LIBRARIES})
