from caesar_cipher.caesar_cipher import encrypt


def test_encrypt_shift_1():
    actual = encrypt("apple", 1)
    expected = "bqqmf"
    assert actual == expected

def test_encrypt_shift_10():
    actual = encrypt("apple", 10)
    expected = "kzzvo"
    assert actual == expected    

def test_uppercase():
    actual = encrypt("BANANA", 10)
    expected = "LKXKXK"
    assert actual == expected