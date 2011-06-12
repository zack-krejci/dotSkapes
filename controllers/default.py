def index():
    output = {}
    output.update ({'geoserver': deployment_settings.geoserver})
    if check_logged_in ():
        output.update ({'side_bar': True, 'tool_list': dm.local_load ('tools').json (), 'tool_saved_results': dm.local_load ('results').json (), 'tool_saved_analyses': dm.local_load ('analyses').json (), 'maps_saved': dm.local_load ('maps').json ()})
        if check_role (dev_role):
            output.update ({'dev_tools': True, 'in_dev': dm.local_load ('dev_tools').json ()})
        else:
            output.update ({'dev_tools': False})
    else:
        output.update ({'side_bar': False, 'dev_tools': False})
    response.title = 'skapes'
    return(output)

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    form = auth ()
    response.title = 'Login'
    return dict(form=form)
