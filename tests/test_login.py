
def test_empty_login(login_page):
    login_page.login(" ", " ")
    error = login_page.get_error()
    
    assert "Username and password do not match any user in this service" in error
    assert "saucedemo" in login_page.driver.current_url

    assert "inventory" not in login_page.driver.current_url

def test_valid_login(login_page):
    login_page.login("standard_user", "secret_sauce")
    assert "inventory" in login_page.driver.current_url

def test_invalid_login_page(login_page):
    login_page.login("non user", "fakepws")
    error =login_page.get_error()

    assert "Username and password do not match" in error

    assert "saucedemo" in login_page.driver.current_url 

    assert "inventory" not in login_page.driver.current_url


def test_locked_user(login_page):
    login_page.login("locked_out_user", "secret_sauce")
    error = login_page.get_error()

    assert "Sorry, this user has been locked out." in error
    assert "saucedemo" in login_page.driver.current_url
    assert "inventory" not in login_page.driver.current_url


def test_only_username(login_page):
    login_page.login("standard_user", "")
    error = login_page.get_error()
    

    assert "Password is required" in error
    assert "saucedemo" in login_page.driver.current_url
    assert "inventory" not in login_page.driver.current_url
