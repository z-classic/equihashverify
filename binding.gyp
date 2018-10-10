{
    "targets": [
        {
            "target_name": "equihashverify",
            "dependencies": [
                "libequi",
            ],
            "sources": [
                "equihashverify.cc",
            ],
            "include_dirs": [
                "<!(node -e \"require('nan')\")"
            ],
            "defines": [
            ],
            "cflags_cc": [
                "-std=c++11",
                "-Wl,--whole-archive",
                "-fPIC",
            ],
            "link_settings": {
                "libraries": [
                    "-Wl,-rpath,./build/Release/",
                ]
            },
            'conditions': [
              ['OS=="openbsd" or OS=="freebsd"', {
                'include_dirs': [
                  '/usr/local/include'],
                 'libraries': [
                   '-L/usr/local/lib']
              }]     
            ]
        },
        {
            "target_name": "libequi",
            "type": "<(library)",
            "dependencies": [
            ],
            "sources": [
                "src/equi/equi.c",
                "src/equi/endian.c"
            ],
            "include_dirs": [
            ],
            "defines": [
            ],
            "cflags_c": [
                "-std=c11",
                "-Wl,--whole-archive",
                "-fPIC",
                "-Wno-pointer-sign",
                "-D_GNU_SOURCE"
            ],
            "link_settings": {
                "libraries": [
                    "-lsodium"
                ],
            },
            'conditions': [
              ['OS=="openbsd" or OS=="freebsd"', {
                'include_dirs': [
                  '/usr/local/include'],
                 'libraries': [
                   '-L/usr/local/lib']
              }]     
            ]
        }
    ]
}

