# Add a custom target to generate a commithash.h file in the output directory.
# This file will contain a decleration of a static const COMMIT_HASH.
add_custom_target(
    commithash
    COMMAND python
        ${CMAKE_CURRENT_LIST_DIR}/commithash.py
        ${CMAKE_CURRENT_LIST_DIR}/commithash.c.template
        -o ${CMAKE_CURRENT_BINARY_DIR}/commithash.c
    WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
)

set_source_files_properties(
    ${CMAKE_CURRENT_BINARY_DIR}/commithash.c 
    PROPERTIES GENERATED TRUE
)
