#include <iostream>


#include "android_ndk/lib.h"


int main() {
    std::cout << "> android_ndk_exe: " << android_ndk_MESSAGE << std::endl;
    
    android_ndk_header(0);
    android_ndk(0);
    
}
