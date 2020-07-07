Android NDK
===========

The package `android_ndk` provides the toolchain for different `os.api_level`, 
depending on that API level the environment has to be populated with different
values.

Challenges
----------
 * The proper value (`cmake_toolchain_file`) has to be selected in the recipe `android_ndk`
   based on the API level from the Android profile.
