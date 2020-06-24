#include "protobuf/lib.h"

// Requires and build_requires (host)
#include "zlib/lib.h"

void protobuf(int tabs) {
    std::cout << std::string(tabs, '\t') << "> protobuf: " << protobuf_MESSAGE << std::endl;

    // Requires and build_requires (host)
    zlib_header(tabs+1);
    zlib(tabs+1);
}
