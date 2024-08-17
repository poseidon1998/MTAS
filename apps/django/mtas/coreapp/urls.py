# core/urls.py
from django.urls import path
from .views import (
    SignUpView,
    SignInView,
    ResetPasswordView,
    InviteMemberView,
    DeleteMemberView,
    UpdateMemberRoleView,
    RoleWiseUserStatsView,
    OrganizationWiseMemberStatsView,
    OrganizationWiseRoleWiseUserStatsView,
)

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset-password'),
    path('invite-member/', InviteMemberView.as_view(), name='invite-member'),
    path('delete-member/<int:pk>/', DeleteMemberView.as_view(), name='delete-member'),
    path('update-member-role/<int:pk>/', UpdateMemberRoleView.as_view(), name='update-member-role'),
    path('role-wise-user-stats/', RoleWiseUserStatsView.as_view(), name='role-wise-user-stats'),
    path('organization-wise-member-stats/', OrganizationWiseMemberStatsView.as_view(), name='organization-wise-member-stats'),
    path('organization-wise-role-wise-user-stats/', OrganizationWiseRoleWiseUserStatsView.as_view(), name='organization-wise-role-wise-user-stats'),
]
