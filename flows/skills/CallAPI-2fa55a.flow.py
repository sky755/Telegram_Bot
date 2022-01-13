{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "method": "get",
    "memory": "session",
    "headers": {
      "content-type": "application/json"
    },
    "url": "https://chat-bot-studio.herokuapp.com/questions/noanswer",
    "variable": "response",
    "invalidJson": false
  },
  "nodes": [
    {
      "name": "entry",
      "onEnter": [
        "basic-skills/call_api {\"url\":\"https://chat-bot-studio.herokuapp.com/questions/noanswer\",\"method\":\"get\",\"headers\":{\"content-type\":\"application/json\"},\"memory\":\"session\",\"variable\":\"response\"}"
      ],
      "next": [
        {
          "condition": "true",
          "node": "#"
        }
      ],
      "id": "106803"
    }
  ]
}