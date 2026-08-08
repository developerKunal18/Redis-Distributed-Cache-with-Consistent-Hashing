import hashlib
import redis


class ConsistentHashCache:

    def __init__(self, nodes):

        self.nodes = nodes
        self.ring = {}

        for node in nodes:

            hash_value = self.hash(node)

            self.ring[hash_value] = node

    def hash(self, key):

        return int(
            hashlib.md5(
                key.encode()
            ).hexdigest(),
            16
        )

    def get_node(self, key):

        key_hash = self.hash(key)

        sorted_nodes = sorted(
            self.ring.keys()
        )

        for node_hash in sorted_nodes:

            if key_hash <= node_hash:

                return self.ring[node_hash]

        return self.ring[
            sorted_nodes[0]
        ]

    def get_client(self, key):

        node = self.get_node(key)

        return redis.Redis(
            host=node,
            port=6379,
            decode_responses=True
        )
