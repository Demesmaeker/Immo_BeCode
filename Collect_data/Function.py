def init_webdriver(is_firefox: bool = False) -> webdriver:
    if is_firefox:
        profile = webdriver.FirefoxProfile()
        # disable pictures
        profile.set_preference('permissions.default.image', 2)
        driver = webdriver.Firefox(firefox_profile=profile)
    else:
        options = webdriver.ChromeOptions()
        # hide pictures
        options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
        driver = webdriver.Chrome(options=options)
    return driver