from passlib.context import CryptContext


pass_ctx = CryptContext(schemes=['bcrypt'], deprecated = "auto")

class Hash():
    def bcrypt_password(password:str):
        return pass_ctx.hash(password)
    
    def verify_password(hassPassword, plainPassword):
        return pass_ctx.verify(plainPassword, hassPassword)
