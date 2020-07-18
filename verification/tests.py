"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[0, 1, 2, 3, 4], [0, 2, 4]],
            "answer": [1, 3],
            "explanation": "[0, 1, 2, 3, 4]\n  ^     ^     ^"
        },
        {
            "input": [[1, 2, 1], [1]],
            "answer": [1, 2],
            "explanation": "[1, 2, 1]\n  ^  ^"
        },
        {
            "input": [[0, [0, 1], 'hello'], [[0, 1], 'hello']],
            "answer": [0],
            "explanation": "[0, [0, 1], 'hello']\n     ^       ^"
        },
        {
            "input": [[[0,0],[0,1],[1,0],[1,1]],[1,1]]
            "answer": [[0,0],[0,1],[1,0]],
            "explanation": "[0, [0, 1], 'hello']\n     ^       ^"
        }
    ],
    "Extra": [
        {
            "input": [[1,[],0],[1,0]],
            "answer": [[]],
            "explanation": "[1,[],0]\n  ^    ^"
        },
        {
            "input": [[[],0,[]],[[]]],
            "answer": [[],0],
            "explanation": "[[],0,[]]\n       ^"
        },
        {
            "input": [['a','b','c','d'],['a','b']],
            "answer": ['c','d'],
            "explanation": "['a','b','c','d']\n  ^   ^"
        },
        {
            "input": [[],[]],
            "answer": [],
            "explanation": "nothing added, nothing removed"
        },
        {
            "input": [[0],[0]],
            "answer": [],
            "explanation": "[0]\n  ^"
        }
    ]
}
