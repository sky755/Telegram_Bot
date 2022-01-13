{
  "version": "0.0.1",
  "catchAll": {
    "onReceive": [],
    "next": []
  },
  "startNode": "choice-start1",
  "nodes": [
    {
      "id": "skill-730b2d",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-start1",
      "flow": "skills/choice-730b2d.flow.json",
      "next": [
        {
          "caption": "User picked [convers...]",
          "condition": "temp['skill-choice-ret-d8istasych'] == \"conversation\"",
          "node": "choice-Anonymous"
        },
        {
          "caption": "User picked [contacts]",
          "condition": "temp['skill-choice-ret-d8istasych'] == \"contacts\"",
          "node": "choice-yes"
        },
        {
          "caption": "User picked [General...]",
          "condition": "temp['skill-choice-ret-d8istasych'] == \"General-new-0\"",
          "node": "General.flow.json"
        },
        {
          "caption": "User picked [recomen...]",
          "condition": "temp['skill-choice-ret-d8istasych'] == \"recomendations\"",
          "node": "Exercises.flow.json"
        },
        {
          "caption": "User picked [feedback]",
          "condition": "temp['skill-choice-ret-d8istasych'] == \"feedback\"",
          "node": "feedbackNode"
        },
        {
          "caption": "On failure",
          "condition": "true",
          "node": ""
        }
      ],
      "onEnter": null,
      "onReceive": null
    },
    {
      "id": "skill-5f7c3b",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-yes",
      "flow": "skills/choice-5f7c3b.flow.json",
      "next": [
        {
          "caption": "User picked [thx]",
          "condition": "temp['skill-choice-ret-fo2qiofcca'] == \"thx\"",
          "node": "choice-begin_or_response"
        },
        {
          "caption": "On failure",
          "condition": "true",
          "node": ""
        }
      ],
      "onEnter": null,
      "onReceive": null
    },
    {
      "id": "skill-f54869",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-begin_or_response",
      "flow": "skills/choice-f54869.flow.json",
      "next": [
        {
          "caption": "User picked [toStart]",
          "condition": "temp['skill-choice-ret-3t681eqxuj'] == \"toStart\"",
          "node": "secondStart"
        },
        {
          "caption": "User picked [feedback]",
          "condition": "temp['skill-choice-ret-3t681eqxuj'] == \"feedback\"",
          "node": "feedbackNode"
        },
        {
          "caption": "On failure",
          "condition": "true",
          "node": ""
        }
      ],
      "onEnter": null,
      "onReceive": null
    },
    {
      "id": "skill-c8dc86",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-sex",
      "flow": "skills/choice-c8dc86.flow.json",
      "next": [
        {
          "caption": "User picked [manTest]",
          "condition": "temp['skill-choice-ret-0w25zlir01'] == \"manTest\"",
          "node": "Male.flow.json"
        },
        {
          "caption": "User picked [womenTe...]",
          "condition": "temp['skill-choice-ret-0w25zlir01'] == \"womenTest\"",
          "node": "Female.flow.json"
        },
        {
          "caption": "On failure",
          "condition": "true",
          "node": ""
        }
      ],
      "onEnter": null,
      "onReceive": null
    },
    {
      "id": "7602465ead",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-sex_2",
      "flow": "skills/choice-c8dc86.flow.json",
      "next": [
        {
          "caption": "User picked [manTest]",
          "condition": "temp['skill-choice-ret-0w25zlir01'] == \"manTest\"",
          "node": "Selftest_Male.flow.json"
        },
        {
          "caption": "User picked [womenTe...]",
          "condition": "temp['skill-choice-ret-0w25zlir01'] == \"womenTest\"",
          "node": "Selftest_Female.flow.json"
        }
      ],
      "onEnter": null,
      "onReceive": null
    },
    {
      "id": "skill-7af6c4",
      "type": "skill-call",
      "skill": "CallAPI",
      "name": "CallAPI-7af6c4",
      "flow": "skills/CallAPI-7af6c4.flow.json",
      "next": [
        {
          "caption": "On success",
          "condition": "temp.valid",
          "node": "choice-8bb99d"
        },
        {
          "caption": "On failure",
          "condition": "!temp.valid",
          "node": "choice-3d8d03"
        }
      ],
      "onEnter": null,
      "onReceive": null
    },
    {
      "id": "skill-3d8d03",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-3d8d03",
      "flow": "skills/choice-3d8d03.flow.json",
      "next": [
        {
          "caption": "User picked [toStart]",
          "condition": "temp['skill-choice-ret-kehwwy9p88'] == \"toStart\"",
          "node": "secondStart"
        }
      ],
      "onEnter": null,
      "onReceive": null
    },
    {
      "id": "a8a2e825a1",
      "name": "node-6780",
      "next": [
        {
          "condition": "true",
          "node": "node-2f48"
        }
      ],
      "onEnter": [
        "builtin/setVariable {\"type\":\"user\",\"name\":\"gender\",\"value\":\"{{event.preview}}\"}"
      ],
      "onReceive": null,
      "type": "standard"
    },
    {
      "id": "skill-444ded",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-444ded",
      "flow": "skills/choice-444ded.flow.json",
      "next": [
        {
          "caption": "User picked [male]",
          "condition": "temp['skill-choice-ret-xrjo4ktmm4'] == \"male\"",
          "node": "node-6780"
        },
        {
          "caption": "User picked [female]",
          "condition": "temp['skill-choice-ret-xrjo4ktmm4'] == \"female\"",
          "node": "node-6780"
        },
        {
          "caption": "On failure",
          "condition": "true",
          "node": ""
        }
      ],
      "onEnter": null,
      "onReceive": null
    },
    {
      "id": "5ddebd8796",
      "name": "node-2f48",
      "next": [
        {
          "condition": "true",
          "node": ""
        }
      ],
      "onEnter": [
        "say #!builtin_text-x-tNS-"
      ],
      "onReceive": null,
      "type": "standard"
    },
    {
      "id": "skill-7a1288",
      "type": "skill-call",
      "skill": "choice",
      "name": "secondStart",
      "flow": "skills/choice-7a1288.flow.json",
      "next": [
        {
          "caption": "User picked [convers...]",
          "condition": "temp['skill-choice-ret-5ktfibmrsy'] == \"conversation\"",
          "node": "choice-cc6418"
        },
        {
          "caption": "User picked [contacts]",
          "condition": "temp['skill-choice-ret-5ktfibmrsy'] == \"contacts\"",
          "node": "choice-yes"
        },
        {
          "caption": "User picked [General...]",
          "condition": "temp['skill-choice-ret-5ktfibmrsy'] == \"General-new-0\"",
          "node": "General.flow.json"
        },
        {
          "caption": "User picked [recomen...]",
          "condition": "temp['skill-choice-ret-5ktfibmrsy'] == \"recomendations\"",
          "node": "Exercises.flow.json"
        },
        {
          "caption": "User picked [feedback]",
          "condition": "temp['skill-choice-ret-5ktfibmrsy'] == \"feedback\"",
          "node": "feedbackNode"
        },
        {
          "caption": "On failure",
          "condition": "true",
          "node": ""
        }
      ],
      "onEnter": null,
      "onReceive": null
    },
    {
      "id": "skill-8bb99d",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-8bb99d",
      "flow": "skills/choice-8bb99d.flow.json",
      "next": [
        {
          "caption": "User picked [toStart]",
          "condition": "temp['skill-choice-ret-sl3mc31yzy'] == \"toStart\"",
          "node": "secondStart"
        },
        {
          "caption": "User picked [fk-4]",
          "condition": "temp['skill-choice-ret-sl3mc31yzy'] == \"fk-4\"",
          "node": "choice-990521"
        },
        {
          "caption": "On failure",
          "condition": "true",
          "node": ""
        }
      ],
      "onEnter": null,
      "onReceive": null
    },
    {
      "id": "c9991f42d5",
      "name": "feedbackNodeNext",
      "next": [
        {
          "condition": "event.nlu.intent.name === ''",
          "node": ""
        }
      ],
      "onEnter": [
        "say #!builtin_text-ULHz9v"
      ],
      "onReceive": null,
      "type": "standard"
    },
    {
      "id": "06551bb5bd",
      "name": "feedbackNode",
      "next": [
        {
          "condition": "true",
          "node": "CallAPI-7af6c4"
        }
      ],
      "onEnter": [
        "say #!builtin_text-QVRAze"
      ],
      "onReceive": [],
      "type": "standard"
    },
    {
      "id": "skill-990521",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-990521",
      "flow": "skills/choice-990521.flow.json",
      "next": [
        {
          "caption": "User picked [fk-3]",
          "condition": "temp['skill-choice-ret-7zmlvhulxy'] == \"fk-3\"",
          "node": "feedbackNode"
        },
        {
          "caption": "On failure",
          "condition": "true",
          "node": ""
        }
      ],
      "onEnter": null,
      "onReceive": null
    },
    {
      "id": "skill-d75aae",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-Anonymous",
      "flow": "skills/choice-d75aae.flow.json",
      "next": [
        {
          "caption": "User picked [nextTest]",
          "condition": "temp['skill-choice-ret-d6k1wh1jsb'] == \"nextTest\"",
          "node": "choice-sex"
        },
        {
          "caption": "On failure",
          "condition": "true",
          "node": ""
        }
      ],
      "onEnter": null,
      "onReceive": null
    },
    {
      "id": "skill-cc6418",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-cc6418",
      "flow": "skills/choice-cc6418.flow.json",
      "next": [
        {
          "caption": "User picked [anonim2]",
          "condition": "temp['skill-choice-ret-ja9i42kete'] == \"anonim2\"",
          "node": "choice-sex"
        },
        {
          "caption": "On failure",
          "condition": "true",
          "node": ""
        }
      ],
      "onEnter": null,
      "onReceive": null
    }
  ]
}