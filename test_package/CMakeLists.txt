project(LinuxDeployCoreTest CXX)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(linuxdeploy REQUIRED)

add_executable(example example.cpp)
target_link_libraries(example linuxdeploy::linuxdeploy )

