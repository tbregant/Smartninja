

def function_name(x, y):
    return x+y


rezultat = function_name(1,2)

print rezultat


def test_ime_funkcije():
    assert function_name(2,3) == 5
    print "test passed"


# executes only if this code is run primarily
if __name__ == "__main__":
    test_ime_funkcije()
    print __name__ # double underscorre "dunder" methods
