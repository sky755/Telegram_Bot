{
  "version": "0.0.1",
  "catchAll": {},
  "startNode": "choice-29e7c0",
  "description": "",
  "nodes": [
    {
      "id": "1aa9db7b6b",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-exercises_2",
      "flow": "skills/choice-329d63.flow.json",
      "next": [
        {
          "caption": "User picked [013]",
          "condition": "temp['skill-choice-ret-pkx9ao0q3p'] == \"013\"",
          "node": "choice-exercises_3"
        },
        {
          "caption": "User picked [014]",
          "condition": "temp['skill-choice-ret-pkx9ao0q3p'] == \"014\"",
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
      "id": "f18a3694a8",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-exercises_3",
      "flow": "skills/choice-64b373.flow.json",
      "next": [
        {
          "caption": "User picked [015]",
          "condition": "temp['skill-choice-ret-1yxb4taevs'] == \"015\"",
          "node": "choice-exercises_4"
        },
        {
          "caption": "User picked [016]",
          "condition": "temp['skill-choice-ret-1yxb4taevs'] == \"016\"",
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
      "id": "a4c1dd630a",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-exercises_4",
      "flow": "skills/choice-7ade3a.flow.json",
      "next": [
        {
          "caption": "User picked [017]",
          "condition": "temp['skill-choice-ret-cgauz31xji'] == \"017\"",
          "node": "choice-exercises_5"
        },
        {
          "caption": "User picked [018]",
          "condition": "temp['skill-choice-ret-cgauz31xji'] == \"018\"",
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
      "id": "90400da852",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-exercises_5",
      "flow": "skills/choice-ff9e3a.flow.json",
      "next": [
        {
          "caption": "User picked [019]",
          "condition": "temp['skill-choice-ret-rgyt9p9hft'] == \"019\"",
          "node": "choice-exercises_6"
        },
        {
          "caption": "User picked [020]",
          "condition": "temp['skill-choice-ret-rgyt9p9hft'] == \"020\"",
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
      "id": "8bd06986b7",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-exercises_6",
      "flow": "skills/choice-217db6.flow.json",
      "next": [
        {
          "caption": "User picked [021]",
          "condition": "temp['skill-choice-ret-szmed57u5n'] == \"021\"",
          "node": "choice-exercise_7"
        },
        {
          "caption": "User picked [022]",
          "condition": "temp['skill-choice-ret-szmed57u5n'] == \"022\"",
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
      "id": "56bf14c1a3",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-exercise_7",
      "flow": "skills/choice-d15775.flow.json",
      "next": [
        {
          "caption": "User picked [023]",
          "condition": "temp['skill-choice-ret-9tmmhvbe0y'] == \"023\"",
          "node": "choice-exercises_8"
        },
        {
          "caption": "User picked [toStart]",
          "condition": "temp['skill-choice-ret-9tmmhvbe0y'] == \"toStart\"",
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
      "id": "0a1f98bc3b",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-exercises_8",
      "flow": "skills/choice-3927b0.flow.json",
      "next": [
        {
          "caption": "User picked [025]",
          "condition": "temp['skill-choice-ret-85iuw6c9pn'] == \"025\"",
          "node": "choice-exercises_9"
        },
        {
          "caption": "User picked [toStart]",
          "condition": "temp['skill-choice-ret-85iuw6c9pn'] == \"toStart\"",
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
      "id": "a37d584545",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-exercises_9",
      "flow": "skills/choice-e29203.flow.json",
      "next": [
        {
          "caption": "User picked [027]",
          "condition": "temp['skill-choice-ret-fip7cu8k27'] == \"027\"",
          "node": "choice-exercises_10"
        },
        {
          "caption": "User picked [toStart]",
          "condition": "temp['skill-choice-ret-fip7cu8k27'] == \"toStart\"",
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
      "id": "56f74cb7ae",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-exercises_10",
      "flow": "skills/choice-748037.flow.json",
      "next": [
        {
          "caption": "User picked [029]",
          "condition": "temp['skill-choice-ret-m43vfxs2g0'] == \"029\"",
          "node": "choice-exercises_OpenDoors"
        },
        {
          "caption": "User picked [startEx...]",
          "condition": "temp['skill-choice-ret-m43vfxs2g0'] == \"startExercise\"",
          "node": "choice-exercises_2"
        },
        {
          "caption": "User picked [toStart]",
          "condition": "temp['skill-choice-ret-m43vfxs2g0'] == \"toStart\"",
          "node": "main.flow.json#secondStart"
        },
        {
          "caption": "On failure",
          "condition": "true",
          "node": "main.flow.json#secondStart"
        }
      ],
      "onEnter": null,
      "onReceive": null
    },
    {
      "id": "518a6e93b1",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-exercises_return",
      "flow": "skills/choice-9e199b.flow.json",
      "next": [
        {
          "caption": "User picked [toStart]",
          "condition": "temp['skill-choice-ret-mrbde7owp3'] == \"toStart\"",
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
      "id": "skill-29e7c0",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-29e7c0",
      "flow": "skills/choice-29e7c0.flow.json",
      "next": [
        {
          "caption": "User picked [startEx...]",
          "condition": "temp['skill-choice-ret-5sjmc5dsq2'] == \"startExercise\"",
          "node": "choice-exercises_2"
        },
        {
          "caption": "User picked [test-ne...]",
          "condition": "temp['skill-choice-ret-5sjmc5dsq2'] == \"test-new-0\"",
          "node": "main.flow.json#choice-sex_2"
        },
        {
          "caption": "User picked [toStart]",
          "condition": "temp['skill-choice-ret-5sjmc5dsq2'] == \"toStart\"",
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
      "id": "skill-1f0931",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-exercises_OpenDoors",
      "flow": "skills/choice-1f0931.flow.json",
      "next": [
        {
          "caption": "User picked [contacts]",
          "condition": "temp['skill-choice-ret-p5f50q9eq5'] == \"contacts\"",
          "node": "main.flow.json#choice-yes"
        },
        {
          "caption": "User picked [toStart]",
          "condition": "temp['skill-choice-ret-p5f50q9eq5'] == \"toStart\"",
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