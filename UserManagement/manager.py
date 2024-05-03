from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    use_in_migrations: bool = True
    def create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError('The username must be set')
        user = self.model(username=username, **extra_fields)
        #STORES THE HASHED PASSOWRD
        user.set_password(password)
#using=self._db ensures that the save operation is executed on the database associated with the current database router.
        user.save(using=self._db)
        return user

