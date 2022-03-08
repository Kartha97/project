"""This test the homepage"""

def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a id="index" class="nav-link link-secondary" aria-current="page" href="/">Home</a>' in response.data
    assert b'<a id="Docker" class="nav-link link-secondary" href="/Docker">About Docker</a>' in response.data
    assert b'<a id="Git" class="nav-link link-secondary" href="/Git">About Git</a>' in response.data
    assert b'<a id="python-flask" class="nav-link link-secondary" href="/python-flask">About python/flask</a>' in response.data
    assert b'<a id="ci-cd" class="nav-link link-secondary" href="/ci-cd">About CI/CD</a>' in response.data

def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"This Page is about index page" in response.data

def test_request_about(client):
    """This makes the index page"""
    response = client.get("/Docker")
    assert response.status_code == 200
    assert b"This Page is about Docker" in response.data

def test_request_page2(client):
    """This makes the index page"""
    response = client.get("/Git")
    assert response.status_code == 200
    assert b"This Page is about Git" in response.data

def test_request_page3(client):
    """This makes the index page"""
    response = client.get("/python-flask")
    assert response.status_code == 200
    assert b"This Page is about Python/flask" in response.data

def test_request_page4(client):
    """This makes the index page"""
    response = client.get("/ci-cd")
    assert response.status_code == 200
    assert b"This Page is about CI/CD" in response.data

def test_request_page_not_found(client):
    """This makes the index page"""
    response = client.get("/page5")
    assert response.status_code == 404