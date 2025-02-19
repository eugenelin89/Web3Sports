from rest_framework import permissions

# This permission class is for demo only.
# "Onwer" here actually referrs to the user that created the object.
# This is different from the definition of our system.
class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.created_by == request.user

# Created User: Created_By
# User handling the business: Owner
# class
class IsOwnerOrCreator(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        has_permission = False
        # obj is MyBusiness instance
        creator = obj.created_by
        if creator == request.user:
            has_permission = True
        else:
            # business_user is Business_User instance,
            # from reverse relationship of a MyBusiness instance
            for business_user in obj.related_users.all():
                if business_user.user == request.user:
                    has_permission =  True
                    break
        return has_permission 
