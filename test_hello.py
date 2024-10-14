from hello import my_name, my_friend


def test_hello():
    assert "Waleed Jabbar" == my_name()


def test_my_friend():
    assert "Ghouri" == my_friend()
