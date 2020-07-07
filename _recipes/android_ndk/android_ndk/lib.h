
#pragma once

#include <iostream>
#include <string>
#include "android_ndk.h"
#include "android_ndk_export.h"

ANDROID_NDK_EXPORT void android_ndk(int tabs);

static void android_ndk_header(int tabs) {
    std::cout << std::string(tabs, '\t') << "> android_ndk_header: " << android_ndk_MESSAGE << std::endl;
}