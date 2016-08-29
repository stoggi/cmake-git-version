# Add a custom target to generate a commithash.h file in the output directory.
# This file will contain a decleration of a static const COMMIT_HASH.
add_custom_target(
    commithash
    COMMAND python ${CMAKE_CURRENT_LIST_DIR}/commithash.py
    WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
)

set_source_files_properties(
    ${CMAKE_CURRENT_BINARY_DIR}/commithash.h 
    PROPERTIES GENERATED TRUE
)

set_source_files_properties(
    ${CMAKE_CURRENT_BINARY_DIR}/commithash.c 
    PROPERTIES GENERATED TRUE
)

# Add the output directories in the includes so that source files can include the commithash.h
include_directories(${CMAKE_CURRENT_BINARY_DIR})