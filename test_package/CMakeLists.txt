project(LinuxDeployCoreTest CXX)

find_package(linuxdeploy REQUIRED)

add_executable(example example.cpp)
target_link_libraries(example linuxdeploy::linuxdeploy )

