{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "lu2kwsf0kq",
    "contentId": "builtin_single-choice-aV0p_e",
    "invalidContentId": "",
    "keywords": {
      "A9-3": [
        "A9-3",
        "То як мені звернутись до психолога?"
      ],
      "toStart": [
        "toStart",
        "Повернемося до початку розмови"
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
        "say #!builtin_single-choice-aV0p_e {\"skill\":\"choice\"}"
      ],
      "next": [
        {
          "condition": "true",
          "node": "parse"
        }
      ],
      "id": "605672"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"lu2kwsf0kq\",\"contentId\":\"builtin_single-choice-aV0p_e\",\"invalidContentId\":\"\",\"keywords\":{\"A9-3\":[\"A9-3\",\"То як мені звернутись до психолога?\"],\"toStart\":[\"toStart\",\"Повернемося до початку розмови\"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-lu2kwsf0kq'] === true",
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
      "id": "440356"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"lu2kwsf0kq\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-lu2kwsf0kq']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "788479"
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
      "id": "344733"
    }
  ]
}