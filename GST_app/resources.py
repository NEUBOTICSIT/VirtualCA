from import_export import resources
from GST_app.models import Member


class MemberResource(resources.ModelResource):
    class Meta:
        model = Member
