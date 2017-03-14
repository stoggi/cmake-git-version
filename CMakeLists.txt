cmake_minimum_required (VERSION 2.8.12)
project (example C)

set(CMAKE_INCLUDE_CURRENT_DIR ON)

include(commithash.cmake)

# Add executable
add_executable (
    example

    main.c
    ${CMAKE_BINARY_DIR}/commithash.c
)

# Add the dependency to the commithash target so it always gets run before being linked
add_dependencies(
    example
    commithash
)