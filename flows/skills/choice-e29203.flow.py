{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "fip7cu8k27",
    "contentId": "builtin_single-choice-sQ8Wpq",
    "invalidContentId": "",
    "keywords": {
      "027": [
        "027",
        "Мені досі не допомогло"
      ],
      "toStart": [
        "toStart",
        "Зрештою, мені стало легше"
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
        "say #!builtin_single-choice-sQ8Wpq {\"skill\":\"choice\"}"
      ],
      "next": [
        {
          "condition": "true",
          "node": "parse"
        }
      ],
      "id": "114140"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"fip7cu8k27\",\"contentId\":\"builtin_single-choice-sQ8Wpq\",\"invalidContentId\":\"\",\"keywords\":{\"027\":[\"027\",\"Мені досі не допомогло\"],\"toStart\":[\"toStart\",\"Зрештою, мені стало легше\"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-fip7cu8k27'] === true",
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
      "id": "037332"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"fip7cu8k27\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-fip7cu8k27']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "358306"
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
      "id": "602669"
    }
  ]
}