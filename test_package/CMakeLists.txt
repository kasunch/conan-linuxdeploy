project(LinuxDeployCoreTest CXX)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(NO_OUTPUT_DIRS)

find_package(linuxdeploy REQUIRED)

add_executable(example example.cpp)
target_link_libraries(example linuxdeploy::linuxdeploy )

