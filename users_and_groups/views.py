from django.db.models import ProtectedError
from django.shortcuts import render, redirect
from .models import User, Group
from .forms import GroupForm, UserForm
from django.http import HttpResponseNotFound, HttpResponse
from django.views.generic import UpdateView
# Create your views here.


def main(request):
    return render(request, 'users_and_groups/index.html')


def users_list(request):
    users = User.objects.order_by('-date_created')
    return render(request, 'users_and_groups/users.html', {"users": users})


def groups_list(request):
    groups = Group.objects.order_by('name')
    return render(request, 'users_and_groups/groups.html', {"groups": groups})


def create_user(request):
    error_message = ""
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
        else:
            error_message = "Not valid data!"

    form = UserForm()
    data = {
        "form": form,
        "error_message": error_message
    }
    return render(request, 'users_and_groups/create_user.html', data)


def create_group(request):
    error_message = ""
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('groups')
        else:
            error_message = "Not valid data!"

    form = GroupForm()
    data = {
        "form": form,
        "error_message": error_message
    }
    return render(request, 'users_and_groups/create_group.html', data)


def action_delete(request):
    if request.method == "POST":
        action = request.POST.get("action")
        print(action)
        if action.startswith("delete_user_"):
            user_id = action.replace("delete_user_", "")
            try:
                User.objects.get(id=user_id).delete()
                # user_id_delete = User.objects.get(id=user_id)
                # user_id_delete.delete()
            except User.DoesNotExist:
                return HttpResponseNotFound("User not found")
            return redirect("users")
        elif action.startswith("delete_group_"):
            group_id = action.replace("delete_group_", "")
            try:
                Group.objects.get(id=group_id).delete()
                # group_id_delete = Group.objects.get(id=group_id)
                # group_id_delete.delete()
            except Group.DoesNotExist:
                return HttpResponseNotFound("Group not found")
            except ProtectedError:
                return HttpResponse("Cannot delete the group because it is not empty.")
            return redirect("groups")


class UserEditView(UpdateView):
    model = User
    template_name = "users_and_groups/edit_user.html"
    form_class = UserForm
    # redirect("users")


class GroupEditView(UpdateView):
    model = Group
    template_name = "users_and_groups/edit_group.html"
    form_class = GroupForm
    # redirect("groups")
