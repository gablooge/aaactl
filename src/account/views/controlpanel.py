from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.http import require_http_methods

import account.forms
from account.decorators import org_view

# Create your views here.


@login_required
def index(request):
    env = {}
    user = request.user

    form = account.forms.ChangeInformation(
        user,
        initial={
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
        },
    )

    invitation_form = account.forms.InviteToOrganization(initial=request.GET)
    create_org_form = account.forms.CreateOrganization()
    create_orgkey_form = account.forms.CreateOrgAPIKey()
    create_key_form = account.forms.CreateAPIKey()
    usercfg_form = account.forms.UserSettings(initial={"opt_promotions":user.usercfg.opt_promotions})

    if user.has_usable_password():
        change_pwd_form = account.forms.ChangePassword(user)
        edit_org_form = account.forms.EditOrganizationPasswordProtected(
            user,
            request.selected_org,
            initial={
                "name": request.selected_org.name,
                "slug": request.selected_org.slug,
            },
        )
    else:
        change_pwd_form = account.forms.ChangePasswordBase()
        env.update(initial_password=True)
        edit_org_form = account.forms.EditOrganization(
            request.selected_org,
            initial={
                "name": request.selected_org.name,
                "slug": request.selected_org.slug,
            },
        )
    env.update(
        change_user_info_form=form,
        change_pwd_form=change_pwd_form,
        create_org_form=create_org_form,
        edit_org_form=edit_org_form,
        invitation_form=invitation_form,
        create_orgkey_form=create_orgkey_form,
        create_key_form=create_key_form,
        usercfg_form=usercfg_form,
        can_invite=request.perms.check([request.selected_org, "users"], "c"),
    )

    return render(request, "account/controlpanel/index.html", env)

