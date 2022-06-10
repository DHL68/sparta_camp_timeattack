from django.db import models

# Create your models here.

class Category(models.Model):
    class Meta:
        db_table = 'category'
        
    def __str__(self):
        return self.title

    title = models.CharField(max_length=100)

class Product(models.Model):
    class Meta:
        db_table = 'product'

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100, verbose_name="상품이름")
    category = models.ForeignKey('Category', verbose_name="카테고리", on_delete=models.CASCADE)
    img_url = models.CharField(max_length=256, default='')
    description = models.TextField(verbose_name="상세정보")
    price = models.IntegerField(verbose_name="가격")
    stock = models.IntegerField(verbose_name="재고량")

class OrderStatus(models.Model):
    user = models.ForeignKey('user.User', verbose_name = "사용자", on_delete = models.CASCADE)
    product = models.ForeignKey('Product',verbose_name = "상품", on_delete = models.CASCADE)
    registered_date = models.DateTimeField(auto_now_add=True, verbose_name="등록시간")
    quantity = models.IntegerField(verbose_name="수량")
    status = models.CharField(
    # 튜플 안에 튜플
    choices=(
        # DB에 저장될 값과 사용자에게 보여줄 값
        ('대기중', '대기중'),
        ('결제대기', '결제대기중'),
        ('결제완료', '결제완료'),
        ('환불', '환불'),
    ),
    default='대기중', max_length=32, verbose_name='상태'
    )

    def __str__(self):
        return str(self.user) + ' ' + str(self.product)
    
    class Meta:
        db_table = "Shoppingmall_Order"
        verbose_name = "주문"
        verbose_name_plural = "주문"