from rest_framework.permissions import BasePermission

# السماح فقط للسوبر يوزر و الموظف بالدخول للصفحة
class EmployeePermissions(BasePermission):
    edit_methods = ("PUT", "PATCH", "PUT", "DELETE")

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        
        if request.user.groups.filter(name="employee"):
            return True

        if request.user.is_authenticated and request.method == 'GET':
            return True
