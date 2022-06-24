from rest_framework import serializers

from post.models import JobPostSkillSet as JobPostSkillSetModel
from post.models import JobPost as JobPostModel
from post.models import Company as CompanyModel
from post.models import BusinessArea as BusinessAreaModel
from post.models import JobType as JobTypeModel

class JobTypeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobTypeModel
        fields = ['__all__']

class BusinessAreaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessAreaModel
        fields = ['__all__']

class CompanyModelSerializer(serializers.ModelSerializer):
    business_area = BusinessAreaModel()

        # get_이름 의 함수를 정의 한다.
    def get_business_area(self, obj):
        # 축약식을 활용해서 카테고리의 정보를 카테고리 안에 담는다.
        return [BusinessArea.area for BusinessArea in obj.BusinessArea.all()]

    class Meta:
        model = CompanyModel
        fields = ['company_name', 'business_area', ]

class JobPostModelSerializer(serializers.ModelSerializer):
    job_type = JobTypeModelSerializer()
    company = CompanyModelSerializer()

    class Meta:
        model = JobPostModel
        fields = ['job_type', 'company', 'job_description', 'salary', ]

class JobPostSkillSetModelSerializer(serializers.ModelSerializer):
    
    job_post = JobPostModelSerializer()
    
    class Meta:
        model = JobPostSkillSetModel
        fields = ['skill_set', 'job_post', ]