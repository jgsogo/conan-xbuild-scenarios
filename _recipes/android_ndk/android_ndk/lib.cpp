#include "android_ndk/lib.h"

// Requires and build_requires (host)
#include "zlib/lib.h"

void android_ndk(int tabs) {
    std::cout << std::string(tabs, '\t') << "> android_ndk: " << android_ndk_MESSAGE << std::endl;

    // Requires and build_requires (host)
    zlib_header(tabs+1);
    zlib(tabs+1);
}
