from pages.LoginPage import LoginPage

def test_valid_login(login_page):
  login_page.login("standard_user", "secret_sauce")
  assert "inventory" in login_page.driver.current_url

def test_invalid_login_page(login_page):
    login_page.login("non user", "fakepws")
    error =login_page.get_error()

    assert "Username and password do not match" in error