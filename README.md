
# Private RSS Demo

This is a simple demonstration of how you can host a private RSS feed, gated by requiring a key in
the URL query parameters. This implementation uses FastAPI, but obviously this is just one possible
choice.

In a real application, you should probably put the keys in an actual database.

We store keys per-user (per-email-address in this case) to allow individual revocation of access.
This can also allow admins to know who might've shared the feed, if it gets out beyond the intended
invitees.

## Example Usage

First, you need to publish an actual RSS feed into the `feed.xml` file, on the server side.

Then, host this app using your chosen server setup.

If you hosted this app at `http://example.com/privaterssdemo/`, you would use the following URL (or
any other with a valid key) in your RSS reader to access the feed:

```
http://example.com/privaterssdemo/?key=3ae3d477038a787541e305acb004cddb5066a2ef
```

