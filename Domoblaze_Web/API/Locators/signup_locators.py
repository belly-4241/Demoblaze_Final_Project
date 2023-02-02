class   sign_up_API:
    url_sign_up = 'https://api.demoblaze.com/signup'
    data_valid = {"UserName": "belaytakele", "password": "cvbn1234"}
    data_invalid_password = {"UserName": "belaytakele", "password": "ccc1234"}
    data_invalid_email = {"UserName": "bely", "password": "cvbn1234"}
    data_invalid_password_and_email = {"UserName": "bely", "password": "ccc1234"}
    data_empty_UserName = {"UserName": "", "password": "cvbn1234"}
    data_empty_password = {"UserName": "belaytakele", "password": ""}
    data_empty_username_password = {"UserName": "", "password": ""}