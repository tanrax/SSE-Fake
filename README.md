# SSE Fake

Free fake Server-send Events for testing and prototyping.

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

## Docs (events)

https://sse-fake.andros.dev/

---

Made with ♥️, Django, Channels and Django EventStream.

Author: [Andros Fenollosa](https://andros.dev/)
