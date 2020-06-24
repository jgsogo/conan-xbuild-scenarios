


function(protobuf_generate_cpp OUTPUT_FILE)
    message(">>>>>>>>>>>>>> protobuf_generate_cpp <<<<<<<<<<<<<<<<<")
    message("Protobuf exported 'protobuf_generate_cpp'")
    message(" - output: ${OUTPUT_FILE}")
    
    add_custom_command(
        OUTPUT ${OUTPUT_FILE}
        COMMAND protoc_exe > ${OUTPUT_FILE}.other 2>&1
        COMMAND protoc_exe > ${OUTPUT_FILE} 2>&1
        COMMENT "Comments running 'protobuf_generate_cpp'"
        VERBATIM)
    message(">>>>>>>>>>>>>> protobuf_generate_cpp <<<<<<<<<<<<<<<<<")
endfunction()
