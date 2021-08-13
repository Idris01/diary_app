## Diary Api Usage

DiaryAPI is built to serve as an online Diary. 

### Usage
The BASE_URL is ``` https://cryptic-brook-44441.herokuapp.com/api/ ``` and following are the endpoint details:

1. CREATE user key
- ```END_POINT= 'acount/' ```
- Send POST request with the body having format
```{ "username": <username>, "password": <password>} ``` to ```https://cryptic-brook-44441.herokuapp.com/api/account/```

- If the POST request is succesfull, the response contains a unique ```diary_key``` for the account.
```{"key":<diary_key }```
>*Note*: Keep the diary_key safe because it will be used to access your Diary. it can be retrieved by resending the Post request with the same details.

2. CREATE  and RETRIEVE  Diary Contents
- ```END_POINT = 'diarys/<diary_key>/' ```
- Send a GET request to the url:
``` https://cryptic-brook-44441.herokuapp.com/api/diarys/<diary_key>/ ```
and a response containing the details of all diary contents is received. This is empty for a new user.

>```
 [
     { "id": "1",
	"title": <title>,
	"content": <content of diary>,
	"created_on":<date created>
	}
	{ "id": "2",
	"title": <title>,
	"content": <content of diary>,
	"created_on":<date created>
	}
	...
	} ```


- Send a POST request with the body content of format ``` { "title":<title of the entry> , "content": <contents of entry>} ```

if the request is sent successfully, a success message is received ```{ "msg":"Diary created" }```

3. UPDATE , DELETE and view details of Diary Content.

- ``` END_POINT = 'api/diarys/<diary_key>/<id>/' ```
- A get request to the END_POINT
``` https://cryptic-brook-44441.herokuapp.com/api/diarys/<diary_key>/<id>/ ```
Retrieves the dairy content of the specific id

- A PUT request with updated content to either of the diary details updates the diary details with the id

``` { "title" : <Updated title> , "content": <Updated content>}  ```

- A DELETE request deletes the content of the diary with the given id.

:sparkles: The Diary API is also browsable so you can check it out on your browser

:+1: Enjoy
