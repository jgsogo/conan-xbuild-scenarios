import os
from conans import ConanFile, CMake

class AndroidNDK(ConanFile):
    name = "android_ndk"

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
        self.copy("*android_ndk_exe*", src="bin", dst="bin", keep_path=False)

        self.copy("*.cmake", src="toolchains", dst="lib/toolchains", keep_path=False)

    def package_info(self):
        self.cpp_info.exes = ["android_ndk"]
        self.env_info.PATH.append(os.path.join(self.package_folder, 'bin'))
