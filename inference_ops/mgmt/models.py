from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Member(TimeStampMixin):
    class Meta:
        db_table = "member"
        # (optional) add indexes to speed up lookup
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.ForeignKey("Organization", on_delete=models.CASCADE)

    def __str__(self):
        ret = f"<username:{self.user.username}> \
                <email:{self.user.email}> \n"
        ret += f"<is_staff:{self.user.is_staff}"
        ret += f"<is_active:{self.user.is_active}>"
        return ret

class Organization(TimeStampMixin):
    class Meta:
        db_table = "organization"

    class ORG_STATUS(models.TextChoices):
        ACTIVE = "ACT", _('Active')
        INACTIVE = "INA", _("Inactive")
        SUSPENDED = "SUS", _("Suspended")

    id = models.AutoField(primary_key=True, db_column="org_id")
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    address = models.CharField(max_length=90)
    website = models.CharField(max_length=100)
    status = models.CharField(max_length=3, choices=ORG_STATUS, default=ORG_STATUS.ACTIVE)

    def __str__(self):
        ret = f"<id: {self.id} \
              name: {self.name} \
              email: {self.email}>" 
        return ret

class Project(TimeStampMixin):
    class Meta:
        db_table = "project"

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    licence = models.CharField(max_length=30)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        ret = f"<id: {self.id}>"
        ret += f"<title: {self.title}>"
        ret += f"<start_date: {self.start_date}>"
        ret += f"end_date: {self.end_date}"
        return ret

class ProjectMember(TimeStampMixin):
    pass

class Metric(TimeStampMixin):
    pass

class Llm(TimeStampMixin):
    class Meta:
        db_table = "llm"

    id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    provider = models.CharField(max_length=30)
    _model = models.CharField(max_length=30)
    version = models.CharField(max_length=30)
    apikey = models.CharField(max_length=100)

    def __str__(self):
        ret = f"<id: {self.id}>"
        ret += f"<provider: {self.provider}>"
        ret += f"<_model: {self._model}>"
        ret += f"<version: {self.version}>"
        return ret


class PromptTemplate(TimeStampMixin):
    pass


class Workflow(TimeStampMixin):
    pass


 