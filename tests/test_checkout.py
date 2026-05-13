def test_checkout_flow(login_page):

    inventory = login_page.login("standard_user", "secret_sauce")

    inventory.add_item_to_cart("sauce-labs-backpack")
    inventory.add_item_to_cart("sauce-labs-bike-light")

    cart = inventory.go_to_cart()

    cart.has_items([
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light"
        ])
    
    cart.remove_item("sauce-labs-bike-light")

    cart.has_items(["Sauce Labs Backpack"])

    inventory = cart.continue_shopping()

    inventory.add_item_to_cart("sauce-labs-bolt-t-shirt")

    cart= inventory.go_to_cart()

    checkout= cart.checkout()

    checkout.fill_details("Amulya", "test", "77777")

    checkout.continue_checkout()

    checkout.finish_checkout()