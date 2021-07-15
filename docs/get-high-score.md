# Get High Scores From The Heroku Server

### /high-score
Returns a JSON array of the highest high score data for displaying the score board

**URL** : `/high-score`

**Method** : `GET`

**Auth required** : No

**Permissions required** : None

## Success Response

**Code** : `200 OK`

**Content examples**

Getting some amount of high scores as a JSON list of objects.

```json
[
    {
        "initials": "SDS",
        "score": 8
    },
    {
        "initials": "SDS",
        "score": 8
    },
    {
        "initials": "DSA",
        "score": 3
    },
    {
        "initials": "JBH",
        "score": 2
    },
    {
        "initials": "HSW",
        "score": 1
    }
]
```


