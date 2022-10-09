import json

def load_candidates():
    with open('candidates.json', 'r', encoding = 'utf-8') as file:
        return json.load(file)


def get_candidates_all():
    return load_candidates()

def get_candidate_by_pk(pk):
    for candidate in load_candidates():
        if candidate['id'] == pk:
            return candidate

    return 'Not Found'

def get_candidates_by_skill(skill):
    result = []
    for candidate in load_candidates():
        if skill.lower() in candidate['skills'].lower().split(', '):
            result.append(candidate)

    return result