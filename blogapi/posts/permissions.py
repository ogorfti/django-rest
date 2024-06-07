from rest_framework import permissions

class testSec(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        # Grant permission for read-only requests SAFE_METHODS = ('GET', 'OPTIONS', 'HEAD')
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Write permissions are only allowed to the author of a post
        return obj.author == request.user