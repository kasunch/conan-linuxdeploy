from conans import ConanFile, CMake, tools
import os

class LinuxdeployConan(ConanFile):
    name = "linuxdeploy"
    version = "continuous"
    license = "MIT"
    author = "Alexis Lopez Zubieta contact@azubieta.net"
    url = "https://github.com/appimage-conan-community/linuxdeploy_installer"
    description = "AppDir creation and maintenance tool. Featuring flexible plugin system"
    topics = ("AppImage", "AppDir", "Tool")
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    build_requires = "cmake_installer/3.13.0@conan/stable"
    exports_sources = "patches/*"

    def source(self):
        self.run("git clone https://github.com/linuxdeploy/linuxdeploy.git --depth=1")
        self.run("cd linuxdeploy && git rm --cached lib/boost*")
        self.run("cd linuxdeploy && git submodule update --init --recursive")
        tools.patch(base_path="linuxdeploy", patch_file="patches/use_conan.patch")

    def requirements(self):
        self.requires("libjpeg/9c@bincrafters/stable")
        self.requires("libpng/1.6.36@bincrafters/stable")
        self.requires("boost_filesystem/1.69.0@bincrafters/stable")
        self.requires("boost_regex/1.69.0@bincrafters/stable")
        self.requires("cmake_findboost_modular/1.69.0@bincrafters/stable")

    def build(self):
        cmake = CMake(self)
        cmake.definitions["USE_SYSTEM_BOOST"] = True
        cmake.definitions["USE_SYSTEM_CIMG"] = False
        cmake.definitions["USE_CCACHE"] = False
        cmake.definitions["BUILD_TESTING"] = False
        cmake.configure(source_folder="linuxdeploy")
        cmake.build()

    def package(self):
        self.copy("linuxdeploy", src="bin", dst="bin")
        self.copy("*.a", src="src", dst="lib", keep_path=False, symlinks=True)
        self.copy("*.a", src="lib/linuxdeploy-desktopfile/src", dst="lib", keep_path=False, symlinks=True)
        self.copy("excludelist.h", src="src/core", dst="include/linuxdeploy")
        self.copy("*.h", src="linuxdeploy/include", dst="include")
        self.copy("*.h", src="linuxdeploy/lib/linuxdeploy-desktopfile/include", dst="include")
        self.copy("*.hpp", src="linuxdeploy/lib/cpp-subprocess", dst="include")

    def package_info(self):
        self.cpp_info.libs = ["liblinuxdeploy_core.a", "liblinuxdeploy_core_copyright.a", "pthread",
                              "liblinuxdeploy_core_log.a", "liblinuxdeploy_util.a", "liblinuxdeploy_plugin.a",
                              "liblinuxdeploy_desktopfile_static.a"]

        self.cpp_info.cflags = ["-lpthread"]
        self.cpp_info.cxxflags = ["-lpthread"]
        self.env_info.PATH.append(os.path.join(self.package_folder, "bin"))

    def deploy(self):
        self.copy("*", dst="bin", src="bin")
