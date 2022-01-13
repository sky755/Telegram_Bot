{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "method": "post",
    "memory": "session",
    "body": "{\n\"describe\" : \"{{event.payload.text}}\",\n\"rate\" : \"2\"\n}",
    "headers": {
      "Content-type": "application/json"
    },
    "url": "http://127.0.0.1:8000/evaluations",
    "variable": "response",
    "invalidJson": false
  },
  "nodes": [
    {
      "name": "entry",
      "onEnter": [
        "basic-skills/call_api {\"url\":\"http://127.0.0.1:8000/evaluations\",\"method\":\"post\",\"body\":\"{\\n\\\"describe\\\" : \\\"{{event.payload.text}}\\\",\\n\\\"rate\\\" : \\\"2\\\"\\n}\",\"headers\":{\"Content-type\":\"application/json\"},\"memory\":\"session\",\"variable\":\"response\"}"
      ],
      "next": [
        {
          "condition": "true",
          "node": "#"
        }
      ],
      "id": "328907"
    }
  ]
}