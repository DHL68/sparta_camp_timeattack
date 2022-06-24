from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from .models import (
    JobPostSkillSet,
    JobType,
    JobPost,
    Company
)
from django.db.models.query_utils import Q


class SkillView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        skills = self.request.query_params.getlist('skills', '')
        print("skills = ", end=""), print(skills)

        return Response(status=status.HTTP_200_OK)


class JobView(APIView):

    def post(self, request):
        job_type = request.data.get("job_type", "")
        company_name = request.data.get("company_name", "")
        job_description = request.data.get("job_description", "")
        salary = request.data.get("salary", "")

        if not job_type:
            return Response({"error" : "job_type 이 테이블에 존재하지 않습니다."}, status=status.HTTP_400_BAD_REQUEST)

        post_job = JobPost(
            job_type=job_type,
            company=company_name,
            **request.data
        )
        post_job.save()

        post_job.job_type.add(*job_type)
        post_job.company.add(*company_name)

        return Response({"message": "성공!"},status=status.HTTP_200_OK)

