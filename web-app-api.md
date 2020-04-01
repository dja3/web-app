# API Details #

All calls should use the same values for headers.
|  KEY         | VALUE                |
|--------------|----------------------|
| Content-Type | application/json     |

## Get all ideas ##
Returns `idea_count`, the number of ideas in the database, and `idea`, a list of all ideas in the database made up of the following fields:

`_id`: ObjectID  
`long_description`: string, detailed description of the idea  
`short_description`: string, few word description of the idea  
`value_in_billions`: integer, perceived value of the idea  
`origination_timestamp`: string, time the idea was first recorded in the database  

**Example request:**
`GET http://<IP or hostname>:80/api/v1/idea`

**Request body format:**
N/A

**Response code:** 200 on success, 404 if no values exist

**Response body format:**
```json
{
  "idea": [{
             "_id": "5e7c08511c9d4400004a46bb",
             "long_description": "Austin Olson is very smart and had an excellent idea to create software defined compute similar to how we have software defined storage and networking",
             "origination_timestamp": "Sun, 01 Sep 2019 20:24:26 GMT",
             "short_description": "software defined compute",
             "value_in_billions": 47
           },
           {
             "_id": "5e7c1fa2810921dd5598280d",
             "long_description": "like solid state disks, but liquid",
             "origination_timestamp": "2020-03-26 03:21:06.096381",
             "short_description": "liquid state disks",
             "value_in_billions": 100
           },
           {
             "_id": "5e7c206a810921dd55982810",
             "long_description": "like solid state disks, but gas",
             "origination_timestamp": "2020-03-26 03:24:26.367306",
             "short_description": "gaseous state disks",
             "value_in_billions": 200
           }],
  "idea_count": 3,
  "timestamp": "2020-04-01 13:21:16.082008"
}
```

## Get single idea ##
Returns a single `idea` which matches the supplied ObjectId, `_id`, in database made up of the following fields:

`_id`: ObjectID  
`long_description`: string, detailed description of the idea  
`short_description`: string, few word description of the idea  
`value_in_billions`: integer, perceived value of the idea  
`origination_timestamp`: string, time the idea was first recorded in the database  

**Example request:**
`GET http://<IP or hostname>:80/api/v1/idea/<_id>`

**Request body format:**
N/A

**Response code**: 200 on success, 404 if `ObjectId` doesn't existing in collection.

**Response body format:**
```json
{
  "idea": {
            "_id": "5e7c08511c9d4400004a46bb",
            "long_description": "Austin Olson is very smart and had an excellent idea to create software defined compute similar to how we have software defined storage and networking",
            "origination_timestamp": "Sun, 01 Sep 2019 20:24:26 GMT",
            "short_description": "software defined compute",
            "value_in_billions": 47
          },
  "timestamp": "2020-04-01 13:21:16.082008"
}
```

## Create a new idea ##
Creates a N idea entries in the database. `idea_list` must be a list even if it is only a single idea. 

**Example request:**
`POST http://<IP or hostname>:80/api/v1/idea`

**Request body format:**
```json
{
  "idea_list": [{
                  "long_description": "test1 test1 test1",
                  "short_description": "test1",
                  "value_in_billions": 100
                },{
                    "long_description": "test2 test2 test2",
                    "short_description": "test2",
                    "value_in_billions": 200
                }]
}
```

**Response code:** 200 on success, failure TBD

**Response body format:**  
TODO

## EVERYTHING ELSE IS UNDER CONSTRUCTION ##
