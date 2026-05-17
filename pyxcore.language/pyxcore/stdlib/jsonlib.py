import json
def encode(value): return json.dumps(value,ensure_ascii=False)
def decode(value): return json.loads(value)
