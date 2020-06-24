
#pragma once

#include <iostream>
#include <string>
#include "protobuf.h"
#include "protobuf_export.h"

PROTOBUF_EXPORT void protobuf(int tabs);

static void protobuf_header(int tabs) {
    std::cout << std::string(tabs, '\t') << "> protobuf_header: " << protobuf_MESSAGE << std::endl;
}