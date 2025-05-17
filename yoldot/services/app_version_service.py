from ..models import AppVersion

class AppVersionService:

    @staticmethod
    def get_all_versions():
        return AppVersion.objects.all()

    @staticmethod
    def get_version_by_platform(platform):
        return AppVersion.objects.filter(platform=platform).first()

    @staticmethod
    def create_version(data):
        return AppVersion.objects.create(**data)

    @staticmethod
    def update_version(platform, data):
        AppVersion.objects.filter(platform=platform).update(**data)
        return AppVersion.objects.get(platform=platform)

    @staticmethod
    def delete_version(platform):
        AppVersion.objects.filter(platform=platform).delete()
