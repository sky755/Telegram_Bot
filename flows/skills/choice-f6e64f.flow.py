{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "c6j8a7nd2t",
    "contentId": "builtin_single-choice-dS2S2R",
    "invalidContentId": "",
    "keywords": {
      "toLawyer": [
        "toLawyer",
        "Ознайом мене з алгоритмом дій"
      ],
      "contactJurSotnya": [
        "contactJurSotnya",
        "Дай контакти юридичної сотні"
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
        "say #!builtin_single-choice-dS2S2R {\"skill\":\"choice\"}"
      ],
      "next": [
        {
          "condition": "true",
          "node": "parse"
        }
      ],
      "id": "229941"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"c6j8a7nd2t\",\"contentId\":\"builtin_single-choice-dS2S2R\",\"invalidContentId\":\"\",\"keywords\":{\"toLawyer\":[\"toLawyer\",\"Ознайом мене з алгоритмом дій\"],\"contactJurSotnya\":[\"contactJurSotnya\",\"Дай контакти юридичної сотні\"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-c6j8a7nd2t'] === true",
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
      "id": "510168"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"c6j8a7nd2t\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-c6j8a7nd2t']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "086145"
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
      "id": "881768"
    }
  ]
}