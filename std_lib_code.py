# Using std library from this file isn`t recomended,
# but if you forgot to put std.bino to folder with binarian executable
# it will be used

# This file can update not as frequently as std.bino in github repo

std_lib_code = \
"""
func xor : val1 val2 (
    return {not {or {and val1 val2} {not {or val1 val2}}}}
)

func add : num1 num2 (
    // Actually I created this language just to write this function. 
    set carry 0
    set ret []

    for dig {zip num1 num2} (
        set a {index dig [0]}
        set b {index dig [1]}

        set sum {xor {xor a b} carry}
        set carry {or {and carry {xor a b}} {and a b}}

        append ret sum
    )

    if carry (
        append ret carry
    )

    return ret
)
"""