from flask import Flask, jsonify
from cache import ConsistentHashCache

app = Flask(__name__)

cache = ConsistentHashCache([
    "redis-1",
    "redis-2",
    "redis-3"
])


@app.route("/cache/<key>")
def get_cache(key):

    client = cache.get_client(key)

    value = client.get(key)

    if value:

        return jsonify({
            "key": key,
            "value": value,
            "source": "cache"
        })

    value = f"Generated value for {key}"

    client.set(
        key,
        value,
        ex=60
    )

    return jsonify({
        "key": key,
        "value": value,
        "source": "database"
    })


@app.route("/health")
def health():

    return jsonify({
        "status": "healthy"
    })


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000
    )
