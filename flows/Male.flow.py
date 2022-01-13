{
  "version": "0.0.1",
  "catchAll": {},
  "startNode": "choice-Male0",
  "description": "",
  "nodes": [
    {
      "id": "skill-a27c41",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-Male0",
      "flow": "skills/choice-a27c41.flow.json",
      "next": [
        {
          "caption": "User picked [eventPa...]",
          "condition": "temp['skill-choice-ret-k59r3efydw'] == \"eventPartisipant\"",
          "node": "choice-participant_1"
        },
        {
          "caption": "User picked [witness]",
          "condition": "temp['skill-choice-ret-k59r3efydw'] == \"witness\"",
          "node": "choice-witness_1"
        },
        {
          "caption": "User picked [aboutPr...]",
          "condition": "temp['skill-choice-ret-k59r3efydw'] == \"aboutProblem\"",
          "node": "General.flow.json"
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
      "id": "skill-e4adb7",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-participant_1",
      "flow": "skills/choice-e4adb7.flow.json",
      "next": [
        {
          "caption": "User picked [84]",
          "condition": "temp['skill-choice-ret-xxmk751qsc'] == \"84\"",
          "node": "choice-participant_2"
        }
      ],
      "onEnter": null,
      "onReceive": null
    },
    {
      "id": "skill-354e6b",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-participant_2",
      "flow": "skills/choice-354e6b.flow.json",
      "next": [
        {
          "caption": "User picked [84]",
          "condition": "temp['skill-choice-ret-wvexpnacxb'] == \"84\"",
          "node": "node-la_strada_1-02"
        },
        {
          "caption": "User picked [85]",
          "condition": "temp['skill-choice-ret-wvexpnacxb'] == \"85\"",
          "node": "choice-suicide_1"
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
      "id": "dbe5fbe19f",
      "name": "node-la_strada_1",
      "next": [
        {
          "condition": "true",
          "node": "main.flow.json#secondStart"
        }
      ],
      "onEnter": [
        "say #!builtin_text-CzDk7X"
      ],
      "onReceive": null,
      "type": "standard"
    },
    {
      "id": "skill-2829e6",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-suicide_1",
      "flow": "skills/choice-2829e6.flow.json",
      "next": [
        {
          "caption": "User picked [86]",
          "condition": "temp['skill-choice-ret-56g0a9eykt'] == \"86\"",
          "node": "choice-suicide_2"
        },
        {
          "caption": "User picked [87]",
          "condition": "temp['skill-choice-ret-56g0a9eykt'] == \"87\"",
          "node": "choice-participant_3"
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
      "id": "skill-38f121",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-suicide_2",
      "flow": "skills/choice-38f121.flow.json",
      "next": [
        {
          "caption": "User picked [88]",
          "condition": "temp['skill-choice-ret-y8jbmm3gfw'] == \"88\"",
          "node": "node-life_line-2"
        },
        {
          "caption": "User picked [89]",
          "condition": "temp['skill-choice-ret-y8jbmm3gfw'] == \"89\"",
          "node": "node-open_doors_1-02"
        },
        {
          "caption": "User picked [810]",
          "condition": "temp['skill-choice-ret-y8jbmm3gfw'] == \"810\"",
          "node": "node-open_doors_1-02"
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
      "id": "6c380a49bb",
      "name": "node-life_line",
      "next": [
        {
          "condition": "true",
          "node": "main.flow.json#secondStart"
        }
      ],
      "onEnter": [
        "say #!builtin_text-t9M7BH"
      ],
      "onReceive": null,
      "type": "standard"
    },
    {
      "id": "3c03aec720",
      "name": "node-open_doors_1",
      "next": [
        {
          "condition": "true",
          "node": "main.flow.json#secondStart"
        }
      ],
      "onEnter": [
        "say #!builtin_text-QHcr0i"
      ],
      "onReceive": null,
      "type": "standard"
    },
    {
      "id": "skill-42415d",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-participant_3",
      "flow": "skills/choice-42415d.flow.json",
      "next": [
        {
          "caption": "User picked [811]",
          "condition": "temp['skill-choice-ret-g4fa3t9gbm'] == \"811\"",
          "node": "choice-psy_1"
        }
      ],
      "onEnter": null,
      "onReceive": null
    },
    {
      "id": "skill-7e3f82",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-test",
      "flow": "skills/choice-7e3f82.flow.json",
      "next": [
        {
          "caption": "User picked [815]",
          "condition": "temp['skill-choice-ret-4zv6a8b6nl'] == \"815\"",
          "node": "Selftest_Male.flow.json"
        },
        {
          "caption": "User picked [816]",
          "condition": "temp['skill-choice-ret-4zv6a8b6nl'] == \"816\"",
          "node": "choice-rest"
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
      "id": "skill-f6e64f",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-rest",
      "flow": "skills/choice-f6e64f.flow.json",
      "next": [
        {
          "caption": "User picked [toLawyer]",
          "condition": "temp['skill-choice-ret-c6j8a7nd2t'] == \"toLawyer\"",
          "node": "Lawyer.flow.json"
        },
        {
          "caption": "User picked [contact...]",
          "condition": "temp['skill-choice-ret-c6j8a7nd2t'] == \"contactJurSotnya\"",
          "node": "choice-feedback-2"
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
      "id": "5793cdeaf6",
      "name": "node-sotnia",
      "next": [
        {
          "condition": "true",
          "node": ""
        }
      ],
      "onEnter": [
        "say #!builtin_text-KMXYT6"
      ],
      "onReceive": null,
      "type": "standard"
    },
    {
      "id": "skill-4a8edb",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-feedback",
      "flow": "skills/choice-4a8edb.flow.json",
      "next": [
        {
          "caption": "User picked [feedback]",
          "condition": "temp['skill-choice-ret-vb6aolw264'] == \"feedback\"",
          "node": "main.flow.json#feedback"
        },
        {
          "caption": "User picked [toStart]",
          "condition": "temp['skill-choice-ret-vb6aolw264'] == \"toStart\"",
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
      "id": "skill-a8bf61",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-witness_2",
      "flow": "skills/choice-a8bf61.flow.json",
      "next": [
        {
          "caption": "User picked [822]",
          "condition": "temp['skill-choice-ret-zq0lwvqinw'] == \"822\"",
          "node": "choice-witness_3"
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
      "id": "skill-59be99",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-witness_3",
      "flow": "skills/choice-59be99.flow.json",
      "next": [
        {
          "caption": "User picked [823]",
          "condition": "temp['skill-choice-ret-0nrl54fslg'] == \"823\"",
          "node": "choice-witness_3-1"
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
      "id": "skill-a7435f",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-witness_1",
      "flow": "skills/choice-a7435f.flow.json",
      "next": [
        {
          "caption": "User picked [821]",
          "condition": "temp['skill-choice-ret-l957c2v0hj'] == \"821\"",
          "node": "choice-witness_2"
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
      "id": "skill-b646b9",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-psy_1",
      "flow": "skills/choice-b646b9.flow.json",
      "next": [
        {
          "caption": "User picked [812]",
          "condition": "temp['skill-choice-ret-9aj1gzvblj'] == \"812\"",
          "node": "node-open_doors_1-02"
        },
        {
          "caption": "User picked [813]",
          "condition": "temp['skill-choice-ret-9aj1gzvblj'] == \"813\"",
          "node": "choice-rest"
        },
        {
          "caption": "User picked [814]",
          "condition": "temp['skill-choice-ret-9aj1gzvblj'] == \"814\"",
          "node": "choice-test"
        }
      ],
      "onEnter": null,
      "onReceive": null
    },
    {
      "id": "skill-0ba117",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-Male1",
      "flow": "skills/choice-0ba117.flow.json",
      "next": [
        {
          "caption": "User picked [eventPa...]",
          "condition": "temp['skill-choice-ret-t8dt08vnlr'] == \"eventPartisipant\"",
          "node": ""
        },
        {
          "caption": "User picked [witness]",
          "condition": "temp['skill-choice-ret-t8dt08vnlr'] == \"witness\"",
          "node": ""
        },
        {
          "caption": "User picked [aboutPr...]",
          "condition": "temp['skill-choice-ret-t8dt08vnlr'] == \"aboutProblem\"",
          "node": "General.flow.json"
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
      "id": "skill-c0908e",
      "type": "skill-call",
      "skill": "choice",
      "name": "node-la_strada_1-02",
      "flow": "skills/choice-c0908e.flow.json",
      "next": [
        {
          "caption": "User picked [contacts]",
          "condition": "temp['skill-choice-ret-w6gq0epryt'] == \"contacts\"",
          "node": "main.flow.json#choice-yes"
        },
        {
          "caption": "User picked [toStart]",
          "condition": "temp['skill-choice-ret-w6gq0epryt'] == \"toStart\"",
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
      "id": "skill-cda5e5",
      "type": "skill-call",
      "skill": "choice",
      "name": "node-life_line-2",
      "flow": "skills/choice-cda5e5.flow.json",
      "next": [
        {
          "caption": "User picked [contacts]",
          "condition": "temp['skill-choice-ret-5z3gyifk7a'] == \"contacts\"",
          "node": "main.flow.json#choice-yes"
        },
        {
          "caption": "User picked [toStart]",
          "condition": "temp['skill-choice-ret-5z3gyifk7a'] == \"toStart\"",
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
      "id": "skill-ff39e5",
      "type": "skill-call",
      "skill": "choice",
      "name": "node-open_doors_1-02",
      "flow": "skills/choice-ff39e5.flow.json",
      "next": [
        {
          "caption": "User picked [contacts]",
          "condition": "temp['skill-choice-ret-rlxmrjoit7'] == \"contacts\"",
          "node": "main.flow.json#choice-yes"
        },
        {
          "caption": "User picked [toStart]",
          "condition": "temp['skill-choice-ret-rlxmrjoit7'] == \"toStart\"",
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
      "id": "skill-c3b80d",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-feedback-2",
      "flow": "skills/choice-c3b80d.flow.json",
      "next": [
        {
          "caption": "User picked [feedback]",
          "condition": "temp['skill-choice-ret-gdr3ccmgcp'] == \"feedback\"",
          "node": "main.flow.json#feedbackNode"
        },
        {
          "caption": "User picked [contacts]",
          "condition": "temp['skill-choice-ret-gdr3ccmgcp'] == \"contacts\"",
          "node": "main.flow.json#choice-yes"
        },
        {
          "caption": "User picked [toStart]",
          "condition": "temp['skill-choice-ret-gdr3ccmgcp'] == \"toStart\"",
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
      "id": "skill-f8f8c5",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-witness_3-1",
      "flow": "skills/choice-f8f8c5.flow.json",
      "next": [
        {
          "caption": "User picked [823-1]",
          "condition": "temp['skill-choice-ret-actvnvwfkq'] == \"823-1\"",
          "node": "choice-witness_4-1"
        },
        {
          "caption": "User picked [823-2]",
          "condition": "temp['skill-choice-ret-actvnvwfkq'] == \"823-2\"",
          "node": "choice-witness-OpenDoors"
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
      "id": "skill-bfdebd",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-witness-OpenDoors",
      "flow": "skills/choice-bfdebd.flow.json",
      "next": [
        {
          "caption": "User picked [contacts]",
          "condition": "temp['skill-choice-ret-dqyvss0l77'] == \"contacts\"",
          "node": "main.flow.json#choice-yes"
        },
        {
          "caption": "User picked [toStart]",
          "condition": "temp['skill-choice-ret-dqyvss0l77'] == \"toStart\"",
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
      "id": "skill-4eb74d",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-witness_4-1",
      "flow": "skills/choice-4eb74d.flow.json",
      "next": [
        {
          "caption": "User picked [825]",
          "condition": "temp['skill-choice-ret-osn8x8i3cq'] == \"825\"",
          "node": "main.flow.json#secondStart"
        },
        {
          "caption": "User picked [feedback]",
          "condition": "temp['skill-choice-ret-osn8x8i3cq'] == \"feedback\"",
          "node": "main.flow.json#feedbackNode"
        },
        {
          "caption": "User picked [contacts]",
          "condition": "temp['skill-choice-ret-osn8x8i3cq'] == \"contacts\"",
          "node": "main.flow.json#choice-yes"
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