from conans import ConanFile, CMake, tools


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

    def deploy(self):
        self.copy("*", dst="bin", src="bin")
