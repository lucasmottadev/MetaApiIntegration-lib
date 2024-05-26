from base.base import GraphBaseMixin

"""
Example as running the graph api client
"""

# 1 - Running with act_id directly

if __name__ == '__main__':

    api = GraphBaseMixin(account_id='act_12345', limited_resources_mode=True)
    """ 
    By default limited_resources_mode is False 
    
    Note that it is not necessary to add the access_token, as 
    when you add the access_token to txt.file, the GraphBase class, parent of 
    GraphBaseMixin, already does the job...
    
    """

# 2 - Running within act_id and get the me/adaccounts values

    api_within_act_id = GraphBaseMixin()

    """
    Note that now, regardless of whether you pass or not, limited_resource_mode,
    in all cases where you do not pass the act_id, it will be true, since you 
    will not be able to pull the children, because it depends solely on an ad account
    """