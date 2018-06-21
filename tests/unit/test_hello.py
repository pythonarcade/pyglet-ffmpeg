from pyglet_ffmpeg import hello


def test_hello():
    actual = hello()
    assert 'World' == actual
