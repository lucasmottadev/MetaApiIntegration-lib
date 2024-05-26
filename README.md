
This project came about as a way to improve integration with MetaApi, since after a lot of work I didn't find anything that could have the desired effect in projects where I worked, my mission is to be able to provide a solid integration library with MetaApi, adjusting the entire logic and need for new clients of the api.

## Create the client

Clone the project
``` 
cd base/keys
```

Write your token in txt file
```
nano access_token.txt
```

### Basically you can perform Graph connection in two ways

#### 1 -  With the explicit account ID and whether the mode of 'limited_resources_mode' on or off.

    api = GraphBaseMixin(account_id='act_12345', limited_resources_mode=True)

By default 'limited_resources_mode' is False 

OBS: Note that it is not necessary to add the access_token, as when you add the access_token to txt file, the GraphBase class, parent of GraphBaseMixin, already does the job...

#### 2 - Running within act_id and get the me/adaccounts values
    api_within_act_id = GraphBaseMixin()

OBS: Note that now, regardless of whether you pass or not, limited_resource_mode,
in all cases where you do not pass the act_id, it will be true, since you 
will not be able to pull the children, because it depends solely on an ad account
