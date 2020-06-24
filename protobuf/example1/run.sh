#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

rm -fr $DIR/_build
mkdir -p $DIR/_build
pushd $DIR/_build
    conan install ../conanfile.py example01/version@ --profile=$DIR/../../_profiles/build
    conan build ../conanfile.py
    #cmake .. -DCMAKE_MODULE_PATH=$DIR/_build
    #cmake --build .
popd

pushd $DIR/_build
    conan install ../conanfile.py example01/version@ --profile=$DIR/../../_profiles/build -g virtualrunenv
    source activate_run.sh
    ./bin/example01
    source deactivate_run.sh
popd
