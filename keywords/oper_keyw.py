from funcs.get_var import get_var
from funcs.exceptions import binarian_assert, throw_exception

def if_keyword(lexic : list[str], state, full_vars : dict[str : object]):
    binarian_assert("{" not in " ".join(lexic), 'Blocks must have starts and finishes matched with "{" and "}".', state)

    cond = bool(get_var(lexic[1], full_vars, state))
    state.allowed_blocks += cond

    state.opened_ifs.append((bool(cond), state.opened_blocks))

def else_keyword(lexic : list[str], state):
    binarian_assert("{" not in " ".join(lexic), 'Blocks must have starts and finishes matched with "{" and "}".', state)

    for j in state.opened_ifs:
        if j[1] == state.opened_blocks:
            if_ = j
            state.opened_ifs.remove(j)
            break
    else:
        throw_exception(f"If operator for else was not found.", state)

    if not if_[0]:
        state.allowed_blocks += 1

def elif_keyword(lexic : list[str], state, full_vars : dict[str : object]):
    binarian_assert("{" not in " ".join(lexic), 'Blocks must have starts and finishes matched with "{" and "}".', state)

    for j in state.opened_ifs:
        if j[1] == state.opened_blocks:
            if_ = j
            state.opened_ifs.remove(j)
            break
    else:
        throw_exception(f"If operator for elif was not found.", state)

    cond = bool(get_var(lexic[1], full_vars, state))

    state.opened_ifs.append((cond and if_[0], state.opened_blocks))  

    if not if_[0] and cond:
        state.allowed_blocks += 1