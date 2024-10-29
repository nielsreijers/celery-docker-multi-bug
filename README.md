# Usage

```
docker compose build
```

Start a worker normally one terminal:
```
docker compose up worker
```

Use it from another terminal:
```
docker compose run client
```
It should say '42'

Stop the worker, and start it using `celery multi start`:
```
docker compose up multi
```

The output says it's starting nodes, and a `ps | grep celery` shows it's running:
```
1732651 ?        R      0:29      \_ /usr/local/bin/python3.11 -m celery -A tasks worker --detach -n worker_a@a5af371f7cac --pidfile=/var/run/celery/worker_a.pid --logfile=/var/log/celery/worker_a%I.log --executable=/usr/local/bin/python3.11
```

But it seems to be stuck in a loop, taking 100% cpu on one core, and it doesn't respond. Doing another `docker compose run client` in the second terminal now gives an error: `celery.exceptions.TimeoutError: The operation timed out.`