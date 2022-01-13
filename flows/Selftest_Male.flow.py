{
  "version": "0.0.1",
  "catchAll": {},
  "startNode": "choice-entry",
  "description": "",
  "nodes": [
    {
      "id": "skill-50080c",
      "type": "skill-call",
      "skill": "choice",
      "name": "S1",
      "flow": "skills/choice-50080c.flow.json",
      "next": [
        {
          "caption": "User picked [A2]",
          "condition": "temp['skill-choice-ret-3e0z0n5mgc'] == \"A2\"",
          "node": "choice-ff39ae"
        },
        {
          "caption": "User picked [A3]",
          "condition": "temp['skill-choice-ret-3e0z0n5mgc'] == \"A3\"",
          "node": "S2"
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
      "id": "d9a83ae800",
      "name": "S_Exit1",
      "next": [
        {
          "condition": "true",
          "node": "main.flow.json#secondStart"
        }
      ],
      "onEnter": [
        "say #!builtin_text-BVJveT"
      ],
      "onReceive": null,
      "type": "standard"
    },
    {
      "id": "skill-c8e017",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-S0",
      "flow": "skills/choice-c8e017.flow.json",
      "next": [
        {
          "caption": "User picked [a1]",
          "condition": "temp['skill-choice-ret-ni8b6igxxs'] == \"a1\"",
          "node": ""
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
      "id": "skill-05e72c",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-S3",
      "flow": "skills/choice-05e72c.flow.json",
      "next": [
        {
          "caption": "User picked [A6]",
          "condition": "temp['skill-choice-ret-fbozlbprfp'] == \"A6\"",
          "node": "choice-ff39ae"
        },
        {
          "caption": "User picked [A7]",
          "condition": "temp['skill-choice-ret-fbozlbprfp'] == \"A7\"",
          "node": "S4-drugs"
        },
        {
          "caption": "User picked [A8]",
          "condition": "temp['skill-choice-ret-fbozlbprfp'] == \"A8\"",
          "node": "S_Exit1"
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
      "id": "skill-7fb7bb",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-entry",
      "flow": "skills/choice-7fb7bb.flow.json",
      "next": [
        {
          "caption": "User picked [nextTest]",
          "condition": "temp['skill-choice-ret-r3n7uea4p6'] == \"nextTest\"",
          "node": "S1"
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
      "id": "skill-ff39ae",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-ff39ae",
      "flow": "skills/choice-ff39ae.flow.json",
      "next": [
        {
          "caption": "User picked [contacts]",
          "condition": "temp['skill-choice-ret-jzezjki293'] == \"contacts\"",
          "node": "main.flow.json#choice-yes"
        },
        {
          "caption": "User picked [toStart]",
          "condition": "temp['skill-choice-ret-jzezjki293'] == \"toStart\"",
          "node": "main.flow.json#secondStart"
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
      "id": "skill-946e70",
      "type": "skill-call",
      "skill": "choice",
      "name": "S2",
      "flow": "skills/choice-946e70.flow.json",
      "next": [
        {
          "caption": "User picked [A4]",
          "condition": "temp['skill-choice-ret-w3k1uu30xl'] == \"A4\"",
          "node": "choice-ff39ae"
        },
        {
          "caption": "User picked [A5]",
          "condition": "temp['skill-choice-ret-w3k1uu30xl'] == \"A5\"",
          "node": "choice-S3"
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
      "id": "skill-c425c8",
      "type": "skill-call",
      "skill": "choice",
      "name": "S4-drugs",
      "flow": "skills/choice-c425c8.flow.json",
      "next": [
        {
          "caption": "User picked [A9]",
          "condition": "temp['skill-choice-ret-wqc4necowm'] == \"A9\"",
          "node": "S4-drugs-1"
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
      "id": "skill-4d3d96",
      "type": "skill-call",
      "skill": "choice",
      "name": "S4-drugs-1",
      "flow": "skills/choice-4d3d96.flow.json",
      "next": [
        {
          "caption": "User picked [A9-2]",
          "condition": "temp['skill-choice-ret-nderm7bfhn'] == \"A9-2\"",
          "node": "S4-drugs-2"
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
      "id": "skill-da1434",
      "type": "skill-call",
      "skill": "choice",
      "name": "S4-drugs-2",
      "flow": "skills/choice-da1434.flow.json",
      "next": [
        {
          "caption": "User picked [A9-3]",
          "condition": "temp['skill-choice-ret-lu2kwsf0kq'] == \"A9-3\"",
          "node": "choice-ff39ae"
        },
        {
          "caption": "User picked [toStart]",
          "condition": "temp['skill-choice-ret-lu2kwsf0kq'] == \"toStart\"",
          "node": "main.flow.json#secondStart"
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