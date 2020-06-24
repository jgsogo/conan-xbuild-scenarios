import os
from conans import ConanFile, CMake

class Recipe(ConanFile):
    name = "example01"

    settings = "os", "arch", "compiler", "build_type"
    generators = "cmake", "cmake_find_package"
    exports = "*"

    requires = "protobuf/0.1@xbuild/scenario"
    build_requires = "protobuf/0.1@xbuild/scenario"

    def build(self):
        # Log environment 
        self.output.info(">>>> os.environ[PATH]={}".format(os.environ.get("PATH")))
        self.output.info(">>>> os.environ[DYLD_LIBRARY_PATH]={}".format(os.environ.get("DYLD_LIBRARY_PATH")))
        # PATH will be available inside CMake, but we cannot propagate DYLD_LIBRARY_PATH because of SIP, alternatives:
        #   + propagate another var and transform
        #   + write values to a script (virtualrunenv) and wrap calls with it

        # Compile!
        cmake = CMake(self)
        cmake.definitions["CONAN_BUILD_DYLD"] = os.environ.get("DYLD_LIBRARY_PATH")
        cmake.configure()
        cmake.build()
