{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "xrjo4ktmm4",
    "contentId": "builtin_single-choice-gMpyfe",
    "invalidContentId": "",
    "keywords": {
      "male": [
        "male",
        "man"
      ],
      "female": [
        "female",
        "woman"
      ]
    },
    "config": {
      "nbMaxRetries": 3,
      "repeatChoicesOnInvalid": false,
      "variableName": ""
    }
  },
  "nodes": [
    {
      "name": "entry",
      "onEnter": [
        "say #!builtin_single-choice-gMpyfe {\"skill\":\"choice\"}"
      ],
      "next": [
        {
          "condition": "true",
          "node": "parse"
        }
      ],
      "id": "446616"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"xrjo4ktmm4\",\"contentId\":\"builtin_single-choice-gMpyfe\",\"invalidContentId\":\"\",\"keywords\":{\"male\":[\"male\",\"man\"],\"female\":[\"female\",\"woman\"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-xrjo4ktmm4'] === true",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "invalid"
        }
      ],
      "triggers": [
        {
          "conditions": [
            {
              "id": "always"
            }
          ]
        }
      ],
      "onEnter": [],
      "id": "087808"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"xrjo4ktmm4\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-xrjo4ktmm4']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "840738"
    },
    {
      "name": "sorry",
      "onEnter": [],
      "next": [
        {
          "condition": "true",
          "node": "parse"
        }
      ],
      "id": "054518"
    }
  ]
}