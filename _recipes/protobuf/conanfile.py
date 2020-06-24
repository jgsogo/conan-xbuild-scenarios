
import os
from conans import ConanFile, CMake

class Protobuf(ConanFile):
    name = "protobuf"

    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    exports = "*"

    generators = "cmake", "cmake_find_package"
    requires = "zlib/0.1@xbuild/scenario"
    
    def build(self):
        cmake = CMake(self)
        settings = "|".join(map(str, [self.settings.os, self.settings.arch, self.settings.compiler, self.settings.build_type]))
        options = "|".join(map(str, ["shared={}".format(self.options.shared)]))
        cmake.definitions["MESSAGE:STRING"] = "|".join([settings, options])
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", keep_path=True)
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
        self.copy("*protoc_exe*", src="bin", dst="bin", keep_path=False)

        self.copy("*.cmake", src="cmake", dst="lib/cmake", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["protobuf"]
        self.cpp_info.build_modules = [os.path.join("lib", "cmake", "macro.cmake"),]
