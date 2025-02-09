{
    "targets": [
        {
            "target_name": "roboticscape",
            "sources": [ "rc-node-bindings.cc" ],
            "cflags": [ "-Wall", "-g", "-std=c++1y" ],
            "cflags_cc!": [ "-fno-rtti", "-std=c++14" ],
            "libraries": [ "-lm", "-lrt", "-lpthread", "-lroboticscape" ],
            "include_dirs": [
                "<!(node -e \"require('nan')\")",
                "/usr/include/"
            ]
        }
    ]
}
