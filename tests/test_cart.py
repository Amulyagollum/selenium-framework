def test_add_to_cart(login_page):
    inventory = login_page.login("standard_user", "secret_sauce")

    inventory.is_loaded()

    inventory.add_item_to_cart("sauce-labs-backpack")

    cart = inventory.go_to_cart()

    assert cart.has_items(["Sauce Labs Backpack"])

def test_add_multiple_items(login_page):

    inventory = login_page.login("standard_user", "secret_sauce")

    items_to_add = [
        "sauce-labs-backpack",
        "sauce-labs-bike-light",
        "sauce-labs-bolt-t-shirt"
    ]

    inventory.add_mutiple_items_to_cart(items_to_add)

    cart = inventory.go_to_cart()

    expected_ui_names = [
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
        "Sauce Labs Bolt T-Shirt"
    ]

    assert cart.has_items(expected_ui_names)