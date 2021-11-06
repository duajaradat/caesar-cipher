from caesar_cipher.caesar_cipher import encrypt


def test_encrypt_shift_1():
    actual = encrypt("apple", 1)
    expected = "bqqmf"
    assert actual == expected

