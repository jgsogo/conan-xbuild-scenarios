#!/bin/bash
set -e
set -x
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# Clean the cache
conan remove zlib/0.1@xbuild/scenario -f || true
conan remove android_ndk/0.1@xbuild/scenario -f || true

# Populate the cache
pushd $DIR/../_recipes
    conan export zlib/conanfile.py zlib/0.1@xbuild/scenario
    conan export android_ndk/conanfile.py android_ndk/0.1@xbuild/scenario
popd


# Build
conan install zlib/0.1@xbuild/scenario --build=zlib --profile $DIR/../_profiles/build
conan install android_ndk/0.1@xbuild/scenario --build=android_ndk --profile $DIR/../_profiles/build


# Run examples
# sh $DIR/example1/run.sh
conan install zlib/0.1@xbuild/scenario --build=zlib --profile:host=$DIR/../_profiles/android --profile:build=$DIR/../_profiles/build
