#!/bin/bash
set -e
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# Clean the cache
conan remove zlib/0.1@xbuild/scenario -f || true
conan remove protobuf/0.1@xbuild/scenario -f || true

# Populate the cache
pushd $DIR/../_recipes
    conan export zlib/conanfile.py zlib/0.1@xbuild/scenario
    conan export protobuf/conanfile.py protobuf/0.1@xbuild/scenario
popd


# Build
conan install zlib/0.1@xbuild/scenario --build --profile $DIR/../_profiles/build
conan install protobuf/0.1@xbuild/scenario --build --profile $DIR/../_profiles/build


# Test
mkdir -p $DIR/_testing
    pushd $DIR/_testing
    conan install protobuf/0.1@xbuild/scenario -g virtualrunenv --profile $DIR/../_profiles/build
    source activate_run.sh
    protoc_exe
    source deactivate_run.sh
popd

# Run examples
sh $DIR/example1/run.sh
