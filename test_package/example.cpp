#include <iostream>
#include <linuxdeploy/core/appdir.h>
#include <linuxdeploy/core/elf.h>
#include <linuxdeploy/core/log.h>
#include <linuxdeploy/util/util.h>

using namespace linuxdeploy::core;
using namespace linuxdeploy::util::misc;
using namespace linuxdeploy::core::log;

int main(int argc, char** argv) {

    appdir::AppDir appDir(std::string("."));
    std::cout << "AppDir path: " << appDir.path() << std::endl;

    return 0;
}
