def test_package_exposes_version():
    import litcomp

    assert isinstance(litcomp.__version__, str)
    assert litcomp.__version__
