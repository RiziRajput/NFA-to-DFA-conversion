 # NFA to DFA Conversion

This Python program converts a Non-deterministic Finite Automaton (NFA) to a Deterministic Finite Automaton (DFA). The implementation uses the epsilon closure and transition functions to achieve the conversion, which is a key concept in compiler construction.

## Features
- **Epsilon Closure Calculation**: Computes the set of states reachable from a given state using epsilon (empty string) transitions.
- **Move Function**: Finds the set of states reachable from a given state on a specific symbol.
- **NFA to DFA Conversion**: Converts an NFA with epsilon transitions to its equivalent DFA.

## Requirements
- Python 3.x

## How It Works
1. The program takes an NFA as input, including:
   - States
   - Alphabet
   - Transitions
   - Start state
   - Final states
2. It calculates the epsilon closure for states and generates DFA states iteratively.
3. DFA transitions are built by processing unprocessed NFA states and symbols.
4. The final DFA is constructed with:
   - Deterministic states
   - Transitions
   - Start state
   - Final states

## Code Overview
### Classes
1. **NFA**: Represents the Non-deterministic Finite Automaton.
   - `epsilon_closure`: Computes the epsilon closure of a state.
   - `move`: Determines states reachable on a given symbol.
2. **DFA**: Represents the Deterministic Finite Automaton.
   - Contains attributes like states, alphabet, transitions, start state, and final states.

### Function
- `nfa_to_dfa(nfa)`: Converts the provided NFA object into its equivalent DFA.

## Example
### Input NFA
- **States**: `{'q0', 'q1', 'q2'}`
- **Alphabet**: `{'a', 'b'}`
- **Transitions**:
  ```python
  {
      ('a', 'q0'): {'q0', 'q1'},
      ('b', 'q1'): {'q2'},
      ('', 'q1'): {'q2'},
  }
