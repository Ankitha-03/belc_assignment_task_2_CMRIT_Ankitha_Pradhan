from task2 import get_crease, fold_pattern
assert get_crease(1, 1) == "Valley"
assert get_crease(3, 6) == "Mountain"
assert get_crease(5, 16) == "Valley"
assert get_crease(8, 255) == "Mountain"


assert fold_pattern(1) == "V"
assert fold_pattern(2) == "VVM"
assert fold_pattern(3) == "VVMVVMM"
print("test cases passed")