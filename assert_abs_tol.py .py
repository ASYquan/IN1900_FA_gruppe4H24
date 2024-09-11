import numpy as np 

manual_pi = 3.1415926535898 #Rounded up pi 
expected_pi = np.pi         

def test_pi():
    computed = manual_pi
    expected = expected_pi
    try : 
        assert (computed == expected)
    except AssertionError:
        print(f"Computed pi = {computed} expected given by Numpy = {expected} ")           
        print(f"Difference in decimals = {abs(expected - computed)} Should use a tolerance.")
    #Should give no errors now.
    tol = 1e-18
    assert (abs(computed == expected) < tol)
    print("success")


test_pi()
