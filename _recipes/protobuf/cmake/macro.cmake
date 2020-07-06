

# TODO: Check protobuf version compatibility


function(protobuf_generate_cpp OUTPUT_FILE)
    message(">>>>>>>>>>>>>> protobuf_generate_cpp <<<<<<<<<<<<<<<<<")
    message("Protobuf exported 'protobuf_generate_cpp'")
    message(" - output: ${OUTPUT_FILE}")
    message(" - path: $ENV{PATH}")
    message(" - environment: $ENV{DYLD_LIBRARY_PATH}")
    message(" - CMAKE_COMMAND: ${CMAKE_COMMAND}")
    message(" - CONAN_BUILD_DYLD: ${CONAN_BUILD_DYLD}")

    add_custom_command(
        OUTPUT ${OUTPUT_FILE}
        COMMAND env > ${OUTPUT_FILE}.env 2>&1
        COMMAND ${CMAKE_COMMAND} -E env "DYLD_LIBRARY_PATH=${CONAN_BUILD_DYLD}:$ENV{DYLD_LIBRARY_PATH}" protoc_exe > ${OUTPUT_FILE}.tt 2>&1
        #COMMAND protoc_exe > ${OUTPUT_FILE}.other 2>&1
        #COMMAND protoc_exe > ${OUTPUT_FILE} 2>&1
        #COMMAND ${CMAKE_COMMAND} -E env "DYLD_LIBRARY_PATH=${Protobuf_LIB_DIRS}:${CONAN_LIB_DIRS}" protoc_exe > ${OUTPUT_FILE} 2>&1
        COMMENT "Comments running 'protobuf_generate_cpp'"
        VERBATIM)
    message(">>>>>>>>>>>>>> protobuf_generate_cpp <<<<<<<<<<<<<<<<<")
endfunction()
