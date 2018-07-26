def contruct_path(u, v, discovered):
    # empty path by default
    path = []
    if v in discovered:
        # we build list from v to u and then reverse it at the end
        path.append(v)
        walk = v
        while walk is not u:
            # find edge leading to walk
            e = discovered[walk]
            parent = e.opposite(walk)
            path.append(parent)
            walk = parent
        # reorient path from u to v        
        path.reverse()
    return path