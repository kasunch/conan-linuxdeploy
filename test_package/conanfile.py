import os
from conans import ConanFile, CMake, tools


class LinuxdeployTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = ("cmake_find_package")
    # build_requires = "cmake_installer/3.13.0@conan/stable"
    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        if not tools.cross_building(self.settings):
            self.run(".%sexample" % os.sep)
            self.run("linuxdeploy --help", run_environment=True)
            self.run("linuxdeploy --list-plugins", run_environment=True)
