# cmake-git-version
Example C / C++ project that uses CMake to build and git for version numbers

## Dependencies

* CMake
* Git
* Python (2.7 / 3.5)

## Usage

Create a build directory, generate the makefiles and build

    mkdir build
    cmake ..
    make

If the current working tree is dirty, it will be printed to the console when being built

![Dirty Tree](/images/dirty-tree.png)

To increase the version number, just tag the repository

    git tag -a "1.2.3"

Then, rebuild

    make

![New Tag](/images/new-tag.png)
