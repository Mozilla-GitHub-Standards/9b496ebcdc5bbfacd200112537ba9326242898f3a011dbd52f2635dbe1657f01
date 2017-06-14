#!/usr/bin/env python
# Simple script that list all Duo usrs and check if they are in any of the groups:
# `white_list_groups'. If not, they are added to `group_to_add_to'.
# This can be modified to do a variety of similar things
# It is currently ran manually and is not intended for automatic production purposes in it's current state.
import sys
import duo_client

admin_api = duo_client.Admin(
    ikey='',
    skey='',
    host='',
)

users = admin_api.get_users()
white_list_groups = []
group_to_add_to=''

for user in users:
    grp = admin_api.get_user_groups(user['user_id'])
    foundok = False
    for g in grp:
        if g['group_id'] in white_list_groups:
            foundok = True
            continue
    if not foundok:
        print("{} {} is in groups: {} but not in group {}, adding.".format(user['username'],
            user['user_id'], grp.__str__(), group_to_add_to))
        admin_api.add_user_group(user['user_id'], group_to_add_to)