

def step_optimized(template, rules, n):
    seen = {}

    for stepnum in range(n):
            print(stepnum)

            new_template = []
            for i in range(len(template)-1):
                
                pair = template[i] + template[i+1]

                if (pair) in rules:
                    new_template.append(template[i])
                    new_template.append(rules[pair])
                
                seen[pair] = template[i] + rules[pair]
            
            new_template.append(template[-1])
            template = new_template

    c = Counter(new_template)
    
    quants = [c[k] for k in c]
    min_quant = min(quants)
    max_quant = max(quants)
    print(max_quant-min_quant)




def transpose(token, rules, limit, new_chars=None, i=0):
    print(i, token)

    if not new_chars:
        new_chars = []

    if i == limit:
        if token in rules:
            new_chars.append(rules[token])
        return new_chars

    if token in rules:
        new_token1 = rules[token] + token[1]
        new_token2 = token[0] + rules[token]
    
    new_chars.append(rules[token])
    result1 = transpose(new_token1, rules, limit, new_chars, i+1)
    result2 = transpose(new_token2, rules, limit, new_chars, i+1)
    
    return new_chars
    
def get_chars(template, rules, num_steps):
    all_chars = []
    for i in range(len(template)-1):
        current = template[i] + template[i+1]

        new_chars = transpose(current, rules, num_steps)
        all_chars.extend(new_chars)

    return all_chars


def calc_one(token, rules, n):

    queue = [token]
    letters = [letter for letter in token]

    for i in range(n):
        c = Counter(letters)
        print()
        print(i, c)
        
        # import pdb; pdb.set_trace()
        next_queue = []
        while True:
            current = queue.pop()
            if current in rules:
                letters.append(rules[current])
                new1 = current[0]+rules[current]
                new2 = rules[current]+current[1]
                next_queue.extend([new1, new2])
            if not queue:
                break
        queue = next_queue

    return letters

def get_template_rule(template, rules, n):
    letters = []
    for i in range(len(template)-1):
        token = template[i] + template[i+1]
        letters.extend(calc_one(token, rules, n))
    return letters






def get_letters(rules):

    letters = set()
    for k in rules:
        letters.update([k[0], k[1]])
        letters.add(rules[k])
    return letters

