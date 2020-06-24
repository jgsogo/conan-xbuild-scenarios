#include <iostream>


#include "protobuf/lib.h"


int main() {
    std::cout << "> protoc: " << protobuf_MESSAGE << std::endl;
    
    protobuf_header(0);
    protobuf(0);
    
}
