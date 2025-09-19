from urllib.parse import urljoin

BASE_URL = 'https://stellarburgers.nomoreparties.site/'

LOGIN_URL = urljoin(BASE_URL, 'login')
REGISTER_URL = urljoin(BASE_URL, 'register')
PERSONAL_ACCOUNT_URL = urljoin(BASE_URL, 'account/profile')