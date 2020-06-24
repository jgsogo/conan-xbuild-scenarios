#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# Clean the cache
conan remove zlib/0.1@xbuild/scenario -f
conan remove protobuf/0.1@xbuild/scenario -f

# Populate the cache
conan export $DIR/../_recipes/zlib/conanfile.py zlib/0.1@xbuild/scenario
conan export $DIR/protobuf/conanfile.py protobuf/0.1@xbuild/scenario

# Build
conan install zlib/0.1@xbuild/scenario --build --profile $DIR/../_profiles/build
conan install protobuf/0.1@xbuild/scenario --build --profile $DIR/../_profiles/build


# Test
mkdir -p $DIR/_testing
pushd $DIR/_testing
conan install protobuf/0.1@xbuild/scenario -g virtualrunenv --profile $DIR/../_profiles/build
source activate_run.sh
protoc
source deactivate_run.sh
popd

