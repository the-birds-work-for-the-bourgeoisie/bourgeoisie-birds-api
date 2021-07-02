# Wake Up The Heroku Server

### /high-score
Inserts a score into the database and returns if there was an error

**URL** : `/high-score`

**Method** : `PUT`

**Auth required** : No

**Permissions required** : None

## Success Response

**Code** : `200 OK`

**Content examples**

Form data:
```
initials:HSW
score:9
```
Getting some amount of high scores as a JSON list of objects.

```json
{
    "message": "inserted"
}
```

## Error Responses

### SQL Error (not your fault)
**Code** : `200 OK`

**Content examples**
Something happended with the SQL (not your fault).
```json
{
    "message": "not inserted"
}
```

### Invalid Request (your fault)
**Code** : `400 Bad Request` (bad request)

**Content examples**

**Invalid request body**: This means that at least one of the keys in the request body is not present. For example:

The form data:
```
initials:HSW
```
Results with:
```json
{
    "errors": "Invalid request body"
}
```

**Invalid values for initials or score**: This means that one of the values is not correct. For example:

The form data:
```
initials:HSW
score:ABC
```
Results with:
```json
{
    "errors": "Invalid values for initials or score"
}
```