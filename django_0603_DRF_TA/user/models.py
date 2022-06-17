from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

# custom user managers
class UserManager(BaseUserManager):
    # 사용자 계정 생성을 위한 관리 구성
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an username')
        user = self.model(
            email = email
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # 관리자의 계정 생성에 관한 관리 구성
    def create_superuser(self, email, password=None):
        user = self.create_user(
            email=email,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

# custom user model
class User(AbstractBaseUser):
    username = models.CharField("사용자 계정", max_length=50)
    password = models.CharField("사용자 비밀번호", max_length=200)
    email = models.EmailField("사용자 이메일", max_length=254, unique=True)
    join_date = models.DateField("가입일", auto_now_add=True)

    is_active = models.BooleanField("default=True")

    is_admin = models.BooleanField("default=False")

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return f"{self.email}"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin