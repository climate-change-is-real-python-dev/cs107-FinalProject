# One way to do it
from socialAD import toydiff
if __name__ == "__main__":
    a = 2.0
    x = toydiff.AutoDiffToy(a)
    alpha = 2.0
    beta = 3.0
    f = alpha * x + beta
    print(f.val, f.der)

# Another way to do it
from socialAD.toydiff import AutoDiffToy
if __name__ == "__main__":
    a = 2.0
    x = AutoDiffToy(a)
    alpha = 2.0
    beta = 3.0
    f = alpha * x + beta
    print(f.val, f.der)

# If pip doesn't work
import toydiff
if __name__ == "__main__":
    a = 2.0
    x = toydiff.AutoDiffToy(a)
    alpha = 2.0
    beta = 3.0
    f = alpha * x + beta
    print(f.val, f.der)

# This way also if pip doesn't work
from toydiff import AutoDiffToy
if __name__ == "__main__":
    a = 2.0
    x = AutoDiffToy(a)
    alpha = 2.0
    beta = 3.0
    f = alpha * x + beta
    print(f.val, f.der)