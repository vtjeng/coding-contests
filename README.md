# coding-contests

Template-based approach cribbed from [ecnerwala](https://github.com/ecnerwala); see [make_prob.sh](https://gist.github.com/ecnerwala/ffc9b8c3f61e87ca043393a135d7794d#file-make_prob-sh), [Makefile](https://gist.github.com/ecnerwala/a3c6332ac626bc448165).

## Getting Started

```sh
$ ./make_prob.sh folder/to/my/new/problem
Running setup
rm -f .precompiled_headers/bits/stdc++.h.gch
mkdir -p .precompiled_headers/bits/
g++ -std=c++17 -O2 -Wall -Wextra -pedantic -Wshadow -Wformat=2 -Wfloat-equal -Wconversion -Wlogical-op -Wshift-overflow=2 -Wduplicated-cond -Wcast-qual -Wcast-align -Wno-unused-result -Wno-sign-conversion -fsanitize=address -fsanitize=undefined -fsanitize=float-divide-by-zero -fsanitize=float-cast-overflow -fno-sanitize-recover=all -fstack-protector-all -D_FORTIFY_SOURCE=2 -D_GLIBCXX_DEBUG -D_GLIBCXX_DEBUG_PEDANTIC    -x c++-header "$(echo '#include<bits/stdc++.h>' | g++ -std=c++17 -O2 -Wall -Wextra -pedantic -Wshadow -Wformat=2 -Wfloat-equal -Wconversion -Wlogical-op -Wshift-overflow=2 -Wduplicated-cond -Wcast-qual -Wcast-align -Wno-unused-result -Wno-sign-conversion -fsanitize=address -fsanitize=undefined -fsanitize=float-divide-by-zero -fsanitize=float-cast-overflow -fno-sanitize-recover=all -fstack-protector-all -D_FORTIFY_SOURCE=2 -D_GLIBCXX_DEBUG -D_GLIBCXX_DEBUG_PEDANTIC    -H -E -x c++ - 2>&1 >/dev/null | head -1 | cut -d ' ' -f2)" -o .precompiled_headers/bits/stdc++.h.gch
g++ -std=c++17 -O2 -Wall -Wextra -pedantic -Wshadow -Wformat=2 -Wfloat-equal -Wconversion -Wlogical-op -Wshift-overflow=2 -Wduplicated-cond -Wcast-qual -Wcast-align -Wno-unused-result -Wno-sign-conversion -fsanitize=address -fsanitize=undefined -fsanitize=float-divide-by-zero -fsanitize=float-cast-overflow -fno-sanitize-recover=all -fstack-protector-all -D_FORTIFY_SOURCE=2 -D_GLIBCXX_DEBUG -D_GLIBCXX_DEBUG_PEDANTIC    -isystem .precompiled_headers moist.cpp   -o moist

$ cd folder/to/my/new/problem

# MANUAL: place sample input in std.in, sample output in std.out

# produces output in std.res and compares to std.out
$ make test
```
