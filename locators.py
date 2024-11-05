from selenium.webdriver.common.by import By

class Locators:
    TO_REG_PAGE_LINK = By.XPATH, "//*[contains(@href, 'register')]" # Ссылка на форму регистрации
    NAME_FIELD = By.XPATH, "//label[contains(text(),'Имя')]/following-sibling::input" # Поле "Имя"
    EMAIL_FIELD = By.XPATH, "//label[contains(text(),'Email')]/following-sibling::input" # Поле "Email"
    PASSWORD_FIELD = By.XPATH, "//label[contains(text(),'Пароль')]/following-sibling::input" # Поле "Пароль"
    REGISTER_BUTTON = By.XPATH, ".//button[text()='Зарегистрироваться']" # Кнопка "Зарегистрироваться"
    INVALID_PASS_TEXT = By.XPATH, "//*[contains(@class, 'input__error')]" # Текст "Некорректный пароль"
    TO_LOGIN_PAGE_BUTTON = By.XPATH, "//*[contains(@class, 'button_button_size_large')]" # Кнопка "Войти в аккаунт" на главной
    TO_ACCOUNT_PAGE_BUTTON = By.XPATH, "//*[contains(@href, 'account')]" # Кнопка "Личный кабинет"
    LOGIN_BUTTON = By.XPATH, "//*[contains(@class, 'button_button_size_medium')]" # Кнопка "Войти"
    TO_ORDER_BUTTON = By.XPATH, "//button[contains(text(),'Оформить заказ')]" # Кнопка "Оформить заказ" на главной
    TO_LOGIN_PAGE_LINK = By.XPATH, "//*[contains(@href, 'login')]" # Ссылка на форму авторизации
    TO_PASS_RECOVERY_PAGE_LINK = By.XPATH, "//*[contains(@href, 'forgot-password')]" # Ссылка на форму восстановления пароля
    TO_CONSTRUCTOR_BUTTON = By.XPATH, "//p[contains(text(),'Конструктор')]" # Кнопка "Конструктор" в меню
    LOGO_BUTTON = By.CLASS_NAME, "AppHeader_header__logo__2D0X2" # Кнопка Лого в меню
    LOGOUT_BUTTON = By.XPATH, ".//button[text()='Выход']" # Кнопка "Выход" в личном кабинете
    BUNS_SECTION = By.XPATH, "//span[contains(text(),'Булки')]/parent::div" # Раздел "Булки"
    SAUCES_SECTION = By.XPATH, "//span[contains(text(),'Соусы')]/parent::div"  # Раздел "Соусы"
    TOPPINGS_SECTION = By.XPATH, "//span[contains(text(),'Начинки')]/parent::div"  # Раздел "Начинки"