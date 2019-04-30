import os

from conans import ConanFile, CMake, tools


class LinuxdeployTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def test(self):
        self.run("linuxdeploy --help", run_environment=True)
        self.run("linuxdeploy --list-plugins", run_environment=True)
