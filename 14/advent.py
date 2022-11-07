from collections import Counter

def process(filename):
    f = open(filename)

    template = next(f).strip()
    
    next(f)

    rules = {}
    for line in f:
        pre, post = line.strip().split(' -> ')
        rules[pre] = post

    return template, rules

def step_all(template, rules, n):

    
    for stepnum in range(n):
        # print(stepnum)
        new_template = []
        for i in range(len(template)-1):
            pair = template[i] + template[i+1]
            if (pair) in rules:
                
                new_template.append(template[i])
                new_template.append(rules[pair])

        new_template.append(template[-1])

        
        template = new_template
        # print(len(template))

    c = Counter(new_template)


    quants = [c[k] for k in c]
    min_quant = min(quants)
    max_quant = max(quants)
    print(max_quant-min_quant)

    return "".join(new_template)


def stepn_part2(template, rules, n):
    counts = Counter()

    # setup initial counts with first template NNCB
    for i in range(len(template)-1):
        counts[template[i]+template[i+1]] = 1


    # add all new 2-letter counts for each step
    for j in range(n):
        # print('step', j)
        counts = step2(rules, counts)
    
    # tally individual letters
    letters = Counter()
    for k in counts:
        letters[k[0]] += counts[k]
        # letters[k[1]] += counts[k]


    # handle last letter
    letters[template[-1]] += 1


    # import pdb; pdb.set_trace()

    values_only = [letters[k] for k in letters]
    # import pdb; pdb.set_trace()
    print(max(values_only) - min(values_only))
    letters = letters.most_common()
    print(letters[0][1] - letters[-1][1])


def step2(rules, counts):
    new_counts = Counter()

    for twoletter in counts:
        first, second = twoletter
        current_count = counts[twoletter]

        new_counts[first + rules[twoletter]] += current_count
        new_counts[rules[twoletter] + second] += current_count

    return new_counts




if __name__ == "__main__":
    template, rules = process("input.txt")
    step_all(template, rules, 10)
    stepn_part2(template, rules, 40)


    
    
    


# 3885132354217
# 3885132354216