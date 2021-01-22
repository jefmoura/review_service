from uuid import UUID

from fastapi import Request

from sdk_fastapi.views.permissions import BasePermission


class HasReferenceAccess(metaclass=BasePermission):
    """
    A permission class that checks for reference permissions.
    """

    def has_permission(self, request: Request, scopes: [str]):
        return True

    def has_object_permission(self, request: Request, scopes: [str], obj_id: UUID):
        return False
        # role_data: RoleData = RoleData()
        # for role in user.roles:
        #     if role.reference_id == obj_id:
        #         role_data = role
        #
        # if role_data.reference_id is None and role_data.scopes == []:
        #     return False
        #
        # for scope in scopes:
        #     if scope in role_data.scopes:
        #         return True
        #
        # return False
