import re

class AuthSystem:
    
    def __init__(self):
        """Define regex"""
        self.username_regex = re.compile(r'(?P<user_name>[A-Z][a-zA-Z]{5,11})')
        self.password_regex = re.compile(r"(?P<user_password>[a-z0-9]{6})")
    
    def _check_username(self, username):
        """Check username is valid or not"""
        if self.username_regex.search(username) is not None:
            print("Correct username")
            return True
        else: 
            print("Username format error! Your username is Tom")
            return False
        
    def _check_password(self, password):
        """Check password is valid or not"""
        if self.password_regex.search(password) is not None:
            print("Correct password")
            return True
        else:
            print("Welcome, Tom! Password format error! Your password is tom059357")
            return False
        
    def authenticate(self, username, password):
        """authenticate the user"""
        if not self._check_username(username):
            return
        
        if not self._check_password(password):
            return
        
        print("Valid user")

    
# Construct a object of type AuthSystem
auth = AuthSystem()

# authenticate the user's credentials
auth.authenticate("Tim", "tom059357")