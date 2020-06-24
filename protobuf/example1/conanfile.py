from conans import ConanFile, CMake

class Recipe(ConanFile):
    name = "example01"

    settings = "os", "arch", "compiler", "build_type"
    generators = "cmake", "cmake_find_package"

    requires = "protobuf/0.1@xbuild/scenario"
    build_requires = "protobuf/0.1@xbuild/scenario"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
