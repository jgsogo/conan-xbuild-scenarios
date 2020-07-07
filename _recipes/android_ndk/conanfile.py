import os
from conans import ConanFile, CMake
from conans.errors import ConanInvalidConfiguration


class AndroidNDK(ConanFile):
    name = "android_ndk"

    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    exports = "*"

    generators = "cmake", "cmake_find_package"
    requires = "zlib/0.1@xbuild/scenario"
    
    def configure(self):
        if hasattr(self, 'settings_target'):
            # We are using this recipe as a build-requires to cross-compile something to Android :D
            target_api_level = int(str(self.settings_target.os.api_level))
            if not 27 <= target_api_level < 30:
                raise ConanInvalidConfiguration("Valid Android API level range is [27, 29]: target.os.api_level is {}".format(target_api_level))

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

        if hasattr(self, 'settings_target'):
            target_api_level = int(str(self.settings_target.os.api_level))
            toolchain_file = os.path.join(self.package_folder, 'lib', 'toolchains', 'api_level_{}.cmake'.format(target_api_level))
            self.env_info.CONAN_CMAKE_TOOLCHAIN_FILE = toolchain_file
            self.output.info("Inject environment variable CONAN_CMAKE_TOOLCHAIN_FILE='{}'".format(toolchain_file))
