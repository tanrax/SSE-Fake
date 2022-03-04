# SSE Fake

Free fake Server-side Events for testing and prototyping.

## Try it

Run this code in JavaScript or from any site:

``` javascript
const sse = new EventSource("https://sse-fake.andros.dev/events/");

sse.onmessage = function(event) {
  console.log(event.data);
}
```

Or from the terminal:

``` bash
curl https://sse-fake.andros.dev/events/
```

## Events

Between 1 to 5 seconds, you will randomly receive one of the following messages:

- User connected

``` javascript
{
	"action": "User connected",
	"name": [random name]
}
```

- User disconnected

``` javascript
{
	"action": "User disconnected",
	"name": [random name]
}
```

- New message

``` javascript
{
	"action": "New message",
	"name": [random name],
	"text": [random text]
}
```

Made with ♥️, Django, Channels and Django EventStream.

Author: [Andros Fenollosa](https://andros.dev/)
