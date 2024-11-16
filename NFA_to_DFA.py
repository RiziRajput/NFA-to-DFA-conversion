from collections import defaultdict

class NFA:
    def __init__(self, states, alphabet, transitions, start_state, final_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.final_states = final_states

    def epsilon_closure(self, state):
        closure = set([state])
        stack = [state]
        while stack:
            current = stack.pop()
            if ('', current) in self.transitions:
                for next_state in self.transitions[('', current)]:
                    if next_state not in closure:
                        closure.add(next_state)
                        stack.append(next_state)
        return closure

    def move(self, states, symbol):
        result = set()
        for state in states:
            if (symbol, state) in self.transitions:
                result.update(self.transitions[(symbol, state)])
        return result

class DFA:
    def __init__(self):
        self.states = set()
        self.alphabet = set()
        self.transitions = {}
        self.start_state = None
        self.final_states = set()

def nfa_to_dfa(nfa):
    start_closure = frozenset(nfa.epsilon_closure(nfa.start_state))
    dfa = DFA()
    dfa.start_state = start_closure
    dfa.alphabet = nfa.alphabet
    unprocessed_states = [start_closure]
    dfa.transitions = {}
    processed_states = set()
    
    while unprocessed_states:
        current = unprocessed_states.pop()
        processed_states.add(current)
        for symbol in nfa.alphabet:
            if symbol == '':  # Skip epsilon
                continue
            move_result = nfa.move(current, symbol)
            closure_result = frozenset(
                state for m in move_result for state in nfa.epsilon_closure(m)
            )
            if closure_result:
                dfa.transitions[(current, symbol)] = closure_result
                if closure_result not in processed_states:
                    unprocessed_states.append(closure_result)
                dfa.states.add(closure_result)
                
    dfa.final_states = {
        state for state in dfa.states if any(s in nfa.final_states for s in state)
    }
    return dfa

# Example usage
states = {'q0', 'q1', 'q2'}
alphabet = {'a', 'b'}
transitions = {
    ('a', 'q0'): {'q0', 'q1'},
    ('b', 'q1'): {'q2'},
    ('', 'q1'): {'q2'},
}
start_state = 'q0'
final_states = {'q2'}

nfa = NFA(states, alphabet, transitions, start_state, final_states)
dfa = nfa_to_dfa(nfa)

print("DFA Start State:", dfa.start_state)
print("DFA States:", dfa.states)
print("DFA Final States:", dfa.final_states)
print("DFA Transitions:")
for (state, symbol), next_state in dfa.transitions.items():
    print(f"{state} --{symbol}--> {next_state}")
            