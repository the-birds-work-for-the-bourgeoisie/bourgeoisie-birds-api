# Wake Up The Heroku Server

### /wake-up
Warm up the Heroku server so the game's request will be faster later

**URL** : `/wake-up`

**Method** : `GET`

**Auth required** : No

**Permissions required** : None

## Success Response

**Code** : `200 OK`

**Content examples**

```json
{
    "message": "awake"
}
```

## Notes

* When the Heroku server falls asleep, it takes about 10 seconds for it to wake up.