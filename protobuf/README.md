protobuf
========

Challenges:
 1. Protobuf package provides a library and an executable.
 1. Both versions should match!
 1. There are CMake functions/macros provided by the library that use the executable.
 1. Macos and SIP: populate DYLD_LIBRARY_PATH before running commands

In order for this example to work, it requires the "wrappers" approach for executables: https://github.com/conan-io/conan/compare/develop...jgsogo:poc/xbuild-exec-wrapper


https://github.com/conan-io/conan/issues/7240
https://github.com/conan-io/conan/issues/6069


BUGS:
* `conan build ` doesn't modify value of `_conan_using_build_profile`