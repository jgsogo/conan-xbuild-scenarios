protobuf
========

Challenges:
 1. Protobuf package provides a library and an executable.
 1. Both versions should match!
    I think it is up to the consumer to run this check, it is the consumer the one that is
    requiring and build-requiring the package `protobuf` (maybe they want to mix versions).
    It is not a big deal to add these lines to the consumer recipe:
    ```
    version = self.run("protoc --version")
    assert version == self.deps_cpp_info["protobuf"].version
    ```

    We can relate this issue to the one for the new graph model: this is recite adding
    a constraint to a recipe somewhere else in the graph (https://github.com/jgsogo/conan-poc-graph/issues/1),
    although here the constraint is between contexts.

 1. There are CMake functions/macros provided by the library that use the executable.
 1. Macos and SIP: populate DYLD_LIBRARY_PATH before running commands

In order for this example to work, it requires the "wrappers" approach for executables: https://github.com/conan-io/conan/compare/develop...jgsogo:poc/xbuild-exec-wrapper


https://github.com/conan-io/conan/issues/7240
https://github.com/conan-io/conan/issues/6069


BUGS:
* `conan build ` doesn't modify value of `_conan_using_build_profile`