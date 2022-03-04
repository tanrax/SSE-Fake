const notyf = new Notyf({
  position: {
    x: 'right',
    y: 'top',
  }
});
const sse = new EventSource("/events/");

sse.onmessage = function(event) {
  const data = JSON.parse(event.data);
  console.log(data);

  switch (data.action) {
      case 'User connected':
          notyf.success(`Connected: ${data.name}`);
          break;
      case 'User disconnected':
          notyf.error(`Disconnected: ${data.name}`);
          break;
      case 'New message':
          notyf.success(`${data.name}: ${data.text.slice(0, 20)}...`);
          break;
  }
}